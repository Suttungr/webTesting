# Testing with Selenium and Python
==================================

This little project contains scripts to test web pages. We have done this before but in the Java language. I have decided to move to Python
as it is easier to understand, in my opinon at least.

## Requirements

This project uses Selenium as the main testing framework and uses a Python virtual environment. The following will guide you to setup this project.

### Download Python

If you have Python already installed or you are on a Mac, ignore this part. You can download the latest version of Python [here](https://www.python.org/downloads/)

### Download virtualenv

You can use the virtualenv package to start the project. use *pip install virtualenv* to install the package on your machine.

### Download The Webdrivers

In order for Selenium to work on browsers, we need to install the respective drivers for a web browsers. I have some popular drivers listed below
along with the download.

* Chrome: [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)
* Firefox: [geckodriver](https://github.com/mozilla/geckodriver/releases)
* Opera: [operariver](https://github.com/operasoftware/operachromiumdriver/releases)
* Edge: [edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

Make sure to add the folder that contains the drivers into your machine's path.

### Download The Project From GitHub

Make sure to clone / download the project into the directory you want by using the command line or terminal. 
Once you are in the directory you want the project to be in, type *git clone https://github.com/Suttungr/webTesting.git* .
Or you can go to the [GitHub page](https://github.com/Suttungr/webTesting) and download the project by clicking the green button, 
and select "Download ZIP".

## Setup The Project

Because this project is based in a little bubble of Python, we're gonna have to activate the environment and download the requirements.

### Activate The Virtual Environment

Once the project is downloaded, make sure to start the virtual environment. 

1. Navigate to the *webTesting* directory
2. Type *venv\Scripts\activate* to activate the virtual environment

You can tell if the environment is active if at the beginning of the prompt has this text: *(venv)* . In order to deactivate the environment,
just type *deactivate* .

### Download The Requirements

There is a file present called *requirements.txt* that we will use to download the necessary requirements.
Simply type *pip install -r requirements.txt* to download all the necessary requirements. Make sure the environment is active.

## Run The Script

Once the venv (virtual environment) is active, type *python main.py* to run the script.
Make sure to go into the "main.py" file to change the test URL and browser if need be.
