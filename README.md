# AWS DeepRacer Starter Project

Download the instructions for the AWS DeepRacer Evo and Sensor Kit here:  
https://aws.amazon.com/deepracer/getting-started/

This project contains a simple script to set up your creds.   
`python script.py wifi`

Just copy over the wifi-creds.txt file onto your USB & plug into your DeepRacer car!

After it finishes connecting to your wifi, retrieve the device-status.txt file from the USB. It contains the IP address & insert into your browser

### Build reward functions & test them out!

Run unit tests against the reward functions by running:  
`python -m unittest`

### Starting a new python project? 
Install pipenv  
`sudo apt install pipenv`

Run pipenv install  
`pipenv install --python 3.8`

The Pipfile & Pipfile.lock files will be created (& even auto-generate if a requirements file already exist)

Install libraries easily like below, & just add the --dev flag for dev dependencies  
`pipenv install flask`  
`pipenv install --dev pytest`

Find your next lib here!   
https://pypi.org/
