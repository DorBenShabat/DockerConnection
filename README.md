# DockerConnection 

The DockerConnection project demonstrates a simple client-server communication setup using Docker containers. It consists of two services, container_a and container_b, where container_a serves as a server running a Flask application, and container_b serves as a client making requests to container_a.

## Project Structure

The project structure is as follows:

- `a` directory: Contains the server-side code.
  - `app.py`: Flask application that serves requests.
  - `Dockerfile`: Dockerfile for building the server container.
  - `requirements.txt`: Required Python packages for the server.

- `b` directory: Contains the client-side code.
  - `client.py`: Flask application that sends requests to the server.
  - `Dockerfile`: Dockerfile for building the client container.
  - `requirements.txt`: Required Python packages for the client.

- `docker-compose.yml`: Docker Compose file defining the services and their configurations.

## Usage

To run the project, follow these steps:

1. Install Docker on your system if you haven't already.

2. Navigate to the root directory of the project where the `docker-compose.yml` file is located.

3. Open a terminal and run the following command:

   ```bash
   docker-compose up
This command will build and start the containers defined in the docker-compose.yml file.

1. Access the application by opening a web browser and visiting:

 - Server (container_a): http://localhost:8081/
 - Client (container_b): http://localhost:8082/
   
2. You should see the server and client applications running and interacting with each other.

## Docker Compose Configuration
The docker-compose.yml file defines the services and their configurations:

 - container_a: Builds the server container based on the a/Dockerfile and exposes port 8080.
 - container_b: Builds the client container based on the b/Dockerfile and exposes port 8080.
