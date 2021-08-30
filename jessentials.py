# GitHub repository: https://github.com/Jean28518/jtools-unix-python
# License: Apache License 2.0

import errno
import os
import subprocess
import sys
import shlex

def ensure_root_privileges():
    if not is_script_running_as_root():
        fail("This script must run as root! Try adding sudo before your command.", errno.EACCES)

def is_script_running_as_root():
    return os.geteuid() == 0

def does_file_exist(file_path):
    return os.path.exists(file_path)

def replace_tilde_to_home(folder_path):
    return folder_path.replace("~", os.environ['HOME'])

# example for enviroment={'DEBIAN_FRONTEND': 'noninteractive'}
# if return_output==true: function returns a array of strings
def run_command(command, print_output=True, return_output=False, enviroment = {}):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, env=enviroment)
    output_lines = [] # In this the output is saved line per line
    if print_output or return_output:
        while True:
            output = process.stdout.readline()
            output = output.decode("utf-8")
            if output == "" and process.poll() is not None:
                break
            if output:
                if print_output:
                    print(output.strip())
                if return_output:
                    output_lines.append(output.strip())
        if return_output:
            return output_lines
        else:
            return process.poll()
    else:
        process.communicate()
        return process.poll()

def get_arguments():
    return sys.argv

def get_value_from_arguments(value_key, default=None):
    args = get_arguments()
    for arg in args:
        if arg.startswith("--" + value_key + "="):
            if len(arg) <= len(value_key)+3: # if line: "value_key="
                return default
            return_value = arg[len(value_key)+3:]
            return return_value
    return default

## short code: -h   long code: --help
def is_argument_option_given(long_code="", short_code=""):
    args = get_arguments()
    for arg in args:
        if arg.startswith("-") and not arg.startswith("--") and not short_code=="": ## Short code
            if short_code in arg:
                return True
        if arg == "--" + long_code and not long_code == "": ## Long code
            return True
    return False

# TODO: Implement Errno
def fail(error_message="", errno=-1):
    if (error_message != ""):
        print(error_message)
    else:
        print("Script failed!")

    sys.exit()

def remove_duplicates(array = []):
    return_array = []
    for element in array:
        if not is_element_in_array(return_array, element):
            return_array.append(element)
    return return_array

def is_element_in_array(array, element):
    for e in array:
        if e == element:
            return True
    return False
