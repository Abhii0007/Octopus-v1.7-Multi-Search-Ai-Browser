@echo off
REM Change to the directory containing the virtual environment
cd /d "C:\\Projects\\Octopus 1.3\\Octopus v1.3\\abhi\\Scripts"

REM Activate the virtual environment
call activate.bat

REM Change to the desired directory after activation
cd /d "C:\\Projects\\Octopus 1.3\\Octopus v1.3"

REM Run the Python script
python main.py

REM Optional: Run additional commands here
REM Example: python your_script.py

REM Keep the command prompt open
cmd /k
