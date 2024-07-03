# I'm still learning python. 
# Made by @Quinny-J
# 01/07/2024

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# OS Lib - https://docs.python.org/3/library/os.html

import os
from flask import Flask, request, render_template

app = Flask(__name__)
commands_ran = [] # Put all of our coammnds here in a list for later

@app.route('/')
def do_index():
    return render_template('index.html', commands_ran=commands_ran)

@app.route("/sh/", methods=['POST', 'GET'])
def do_command():
    command_user = request.form.get('cus_command')
    commands_ran.append(f'Ran Command: {command_user}')
    response_data = os.popen(command_user).read()
    #with open("commands_ran.txt", "a") as text_file:
    #    text_file.write("Ran Command: %s\n" % command_user)
    return render_template('index.html', response_data=response_data, command_user=command_user, commands_ran=commands_ran) 
