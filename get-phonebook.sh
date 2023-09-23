#!/bin/bash

# Navigate to the directory where your Python script is located
cd /home/pi/kurt

# Run the Python script to generate phonebook.xml
python3 kurt.py

# Move the generated phonebook.xml to the web server directory
#mv phonebook.xml /var/www/html/phonebook.xml
