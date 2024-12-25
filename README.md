## Prerequisites

Before starting, ensure the following are installed on your machine:

1. **Docker Desktop**:
   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system.
   - Follow the installation instructions for your OS.

2. **Python** (for running tests):
   - Download Python 3.10 or newer from [python.org](https://www.python.org/downloads/).
   - Install `pytest` for running tests:
     ```bash
     pip install pytest
     ```

---

## Docker Setup - Step by Step

### Step 1: Install Docker Desktop

1. Go to the [Docker Desktop website](https://www.docker.com/products/docker-desktop) and download Docker for your operating system.
2. Follow the installation steps:
   - **Windows**: Install Docker Desktop and enable the **WSL 2 backend** during installation. Restart your computer if prompted.
   - **Mac**: Install Docker Desktop and allow permissions when requested.
   - **Linux**: Install Docker Engine by following the [official instructions](https://docs.docker.com/engine/install/).
3. Launch Docker Desktop and ensure it's running.

---

### Step 2: Verify Docker Installation

To confirm Docker is installed, run the following command in your terminal:

```bash
docker --version


### Step 3: Pull the Docker Image

Download the necessary Docker image using the following command:

Always show details

docker pull mdsdockerfiles/mds-qa-test:latest

This will download the image mdsdockerfiles/mds-qa-test:latest to your local Docker environment.


### Step 4: Run the Docker Container

Start the Docker container using this command:

Always show details

docker run -d -p 8000:8000 mdsdockerfiles/mds-qa-test:latest

Explanation:

    -d: Runs the container in detached mode (in the background).
    -p 8000:8000: Maps port 8000 in the container to port 8000 on your local machine.

Once the container is running, the API will be accessible at:

Always show details
http://127.0.0.1:8000
