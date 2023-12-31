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

## Development

To develop with this project, you can mount your local code into the Docker container. This allows you to make changes to your code and have those changes immediately reflected in the Docker container.

1. Build the Docker image:

```bash
docker build -t my-python-app .
```

2. Mount your local code and run the Docker container:

```bash
docker run -it --rm -v $(pwd):/app --name my-running-app my-python-app
```

This will start the Python application in a Docker container with your local code mounted. Any changes you make to your local code will be reflected in the Docker container.

## Running Tests

To run the tests for this project with more verbose output and in parallel, you can use the following command:

```bash
pytest -n auto -v src/test_main.py
```

This will run the `test_query_api` test case in the `test_main.py` file, display more detailed information about each test, and use as many workers as available CPU cores to run tests in parallel.

To run the tests using Docker with mounted local code, more verbose output, and in parallel, use the following commands:

1. Build the Docker image:

```bash
docker build -t my-python-app .
```

2. Mount your local code and run the tests in the Docker container:

```bash
docker run -it --rm -v $(pwd)/src:/app --name my-running-app my-python-app pytest -n 50 -v --durations=10 --json-report ./test_main.py
```

This will run the `test_query_api` test case in the `test_main.py` file in a Docker container with your local code mounted, display more detailed information about each test, and use as many workers as available CPU cores to run tests in parallel.
