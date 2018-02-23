import subprocess

def get_from_pass(name):
    return subprocess.check_output("pass " + name, shell=True).splitlines()[0]
