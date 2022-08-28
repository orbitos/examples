from datetime import datetime
import json
import os
import shutil
import tempfile
from time import sleep
from traceback import print_exc
import zipfile

print("Starting payload!")

while True:
    try:
        print("Current location is ", os.system('cat /orbitos/sensors/location/current_value'))
        
        with tempfile.TemporaryDirectory() as tmpdir:
            shutil.copyfile('/orbitos/sensors/_aggregated/current_value', os.path.join(tmpdir, 'sensors.json'))

            with open(os.path.join(tmpdir, 'metadata.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps({
                    "test": True
                }))

            timestamp = datetime.utcnow().isoformat()
            archive_name = f"session-{timestamp}.zip"
            with zipfile.ZipFile(os.path.join(tmpdir, archive_name), mode="w") as archive:
                for file in ['metadata.json', 'sensors.json']:                     
                    archive.write(os.path.join(tmpdir, file), file)
                    
                archive.printdir()

            shutil.move(os.path.join(tmpdir, archive_name), os.path.join('/orbitos/comms/downlink', archive_name))
    except:
        print_exc()
        
    sleep(5)
