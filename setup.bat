:@echo OFF

echo Current version of Python:
python.exe --version

echo Create the local environment
python.exe -m venv localEnv

echo Activate the local environmentCALL localEnv\Scripts\activate.bat

echo Install the required dependencies for the project
pip install -r requirements.txt