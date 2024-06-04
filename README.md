# FantasyNSIC_Backend

## Description

This repository contains all of the backend application logic and api endpoints for the nsic fantasy application to be used for database access and manipulation, as well as any necessary calculations.

DISCLAIMER: This application and project is meant for recreational use and it not intended for mass distribution, as public access is regulated internally by the owners. It is not meant for turning a profit, nor is it used for gambling purposes. This is just for fun :D

## Installation

**Pre-Requisites**

Python 3.12: https://www.python.org/downloads/release/python-3120/  
Visual Studio Code: https://code.visualstudio.com/download  
GitHub Desktop (Optional): https://desktop.github.com/

**Development Environment Setup**
1. Install the above pre-requisites.
2. Clone the repository using GitHub Desktop or command line locally
3. Open the repository in Visual Studio Code
4. Ensure the following extensions are installed in VSCode
   
    **Python:** ms-python.python    
    **Python Debugger:** ms-python.debugpy  
    **Pylance:** ms-python.vscode-pylance  
    **iSort:** ms-python.isort  
    **autopep8:** ms-python.autopep8 
  
5. Open a new terminal and type the following commands in order to set up a virtual environment
   `python -m venv env`. If you have existing python versions installed, you can run `python3.12 -m venv env` to ensure you are using python 3.12. This is the same across Windows and Mac but the command to activate is different.
   **Windows:** `.\env\Scripts\activate`  
   **Mac:** `source venv/bin/activate`  

    You may get an error saying that access is restricted or unable to execute scripts. In this case run the following commands in powershell as administrator.  
    `Get-ExecutionPolicy`  
    If it says restricted or anything other than Remote-Signed then run the following command.  
    `Set-ExecutionPolicy RemoteSigned`  

    Now re-run the activate command in your terminal in VSCode and you should then get a green (env) in front of your terminal.

    **Ensure that the python interpreter is set to the virtual environment you just created.**  

6. Run `pip install -r requirements.txt` in the terminal.

## Usage

In order to hit the api endpoints locally Postman is used. 

1. Activate the virtual environment in the terminal if it is not already.
   
2. Add the following folder if it does not exist already to the root directory. `.vscode`
   
3. Add `launch.json` to the `.vscode` folder and put the following code inside of it.
   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Python Debugger: Module",
               "type": "debugpy",
               "request": "launch",
               "module": "src.main.api.scheduling_rest_api"
           }
       ]
   }
   ```

4. Now click the Run dropdown in VSCode and Start Debugging or press F5

    You should now see the API running in the terminal with the URL to use to hit any endoint.
