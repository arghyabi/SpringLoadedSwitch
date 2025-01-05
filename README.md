# Spring Loaded Switch

SpringLoadedSwitch is a Python-based project that provides a web interface for simulating the behavior of a spring-loaded toggle switch. This project is useful for understanding the mechanics of such switches and can serve as an educational tool or a prototype for more complex simulations.

## Features

- **Web Interface**: Interactive web-based simulation of a spring-loaded toggle switch.
- **Python Backend**: Utilizes Python scripts to handle the logic and state management of the switch.
- **Educational Tool**: Demonstrates the principles of spring-loaded mechanisms in a user-friendly manner.

## Installation

### 1. Clone the Repository:

  ```bash
  git clone https://github.com/arghyabi/SpringLoadedSwitch.git
  ```
### 2. Navigate to the Project Directory:
  ```bash
  cd SpringLoadedSwitch
  ```
### 3. Install Dependencies:

  Ensure you have Python installed. Then, install the required packages:
  ```bash
  pip install -r requirements.txt
  ```
## Usage
### 1. Configure and Install Application:

  Execute the provided shell script to configure and install Python Server and PHP server:
  ```bash
  ./preConfig.sh
  ```

### 2. Access the Application:

  Open your web browser and navigate to `http://localhost:8080` to interact with the simulation.

### 3. Individually Configure and run Python Server:

  If the Python server already installed via `preConfig.sh` script then turn of the running server:
  ```bash
  sudo systemctl stop spring-loaded-switch-python.service
  ```
  If the server is not running then this step can be skipped and directly run the following connand to run the python server locally
  ```bash
  ./runPythonServer.sh
  ```

### 4. Individually Configure and run PHP Server:

  If the PHP server already installed via `preConfig.sh` script then turn of the running server:
  ```bash
  sudo systemctl stop spring-loaded-switch-php.service
  ```
  If the server is not running then this step can be skipped and directly run the following connand to run the php server locally
  ```bash
  ./runPhpServer.sh
   ```

## Project Structure
```bash
SpringLoadedSwitch/
├── Script/
│   └── [Python scripts handling switch logic]
├── Web/
│   └── [HTML/CSS/JavaScript files for the web interface]
├── .gitignore
├── config.yaml
├── preConfig.sh
├── requirements.txt
├── runPhpServer.sh
└── runPythonServer.sh
```
- **Script/**: Contains Python scripts that manage the switch's behavior and state.
- **Web/**: Includes the frontend components for the web interface.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **config.yaml**: Configuration file for setting up parameters.
- **preConfig.sh**: Shell script to Configure the env and install all the service file for both python and php server.
- **requirements.txt**: This will install all required python packages.
- **runPhpServer.sh**: Shell script to initiate a PHP server for hosting the web interface.
- **runPythonServer.sh**: Shell script to initiate a Python server to run the main logic code.
