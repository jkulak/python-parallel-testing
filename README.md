# Project Title

This is a simple Python project that queries an API based on user input.

## Running the project in a Docker container

1. Build the Docker image:

```bash
docker build -t my-python-app .
```

2. Run the Docker container:

```bash
docker run -it --rm --name my-running-app my-python-app
```

This will start the Python application in a Docker container. The application will prompt for user input and then query the API with the input.
