This project contains automated tests using Selenium and pytest, running in a Docker environment. Additionally, Allure reports are generated to visualize test results.

1. Clone the Repository
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/valeriu-birladeanu/Demo_QA.git 
```

2. Change to the Project Directory
After cloning, change the current directory to the project folder:
```bash
cd Demo_QA
```
3. Run Tests with Docker Compose
To build the Docker image and start the container that runs the tests, use Docker Compose:
```bash
docker-compose up
```
This command will build the Docker image according to the configuration in the Dockerfile and docker-compose.yml, and then execute the defined tests. Ensure that Docker and Docker Compose are installed on your machine.

4. Generate and View Allure Report
After the tests have been executed, you can generate and view the Allure report using the following command:
```bash
allure serve allure-results
```
This command will start a local server and display the Allure report in a web browser. Ensure that Allure Commandline is installed on your machine to use this feature.
