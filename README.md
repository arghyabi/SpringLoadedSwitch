# Spring Loaded Switch

SpringLoadedSwitch is a Python-based project that provides a web interface for simulating the behavior of a spring-loaded toggle switch. This project is useful for understanding the mechanics of such switches and can serve as an educational tool or a prototype for more complex simulations.

## Features

- **Web Interface**: Interactive web-based simulation of a spring-loaded toggle switch.
- **Python Backend**: Utilizes Python scripts to handle the logic and state management of the switch.
- **Educational Tool**: Demonstrates the principles of spring-loaded mechanisms in a user-friendly manner.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/arghyabi/SpringLoadedSwitch.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd SpringLoadedSwitch
   ```
3. **Install Dependencies**:

  Ensure you have Python installed. Then, install the required packages:
  ```bash
   pip install -r requirements.txt
  ```
## Usage
1. **Start the Web Server**:

  Execute the provided shell script to run the PHP server:
  ```bash
   ./runPhpServer.sh
  ```
2. **Access the Application**:
   Open your web browser and navigate to `http://localhost:8080` to interact with the simulation.

## Project Structure
```bash
SpringLoadedSwitch/
├── Script/
│   └── [Python scripts handling switch logic]
├── Web/
│   └── [HTML/CSS/JavaScript files for the web interface]
├── .gitignore
├── config.yaml
└── runPhpServer.sh
```
- **Script/**: Contains Python scripts that manage the switch's behavior and state.
- **Web/**: Includes the frontend components for the web interface.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **config.yaml**: Configuration file for setting up parameters.
- **runPhpServer.sh**: Shell script to initiate a PHP server for hosting the web interface.
