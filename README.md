# Examples

# Simple payload

contains two services, one which comes up immediately, and another that operates on a schedule

## Development

Make sure you have *Tilt*, *Docker* and a *Python3* installed
```
# Get the orbitos and poetry tool
$ pip install poetry orbitos
$ poetry install 

# Create a development docker-compose.yml from the project's orbitos.yml
$ orbitctl generate --dev

# Use tilt to run the environment in development mode
$ tilt up
```