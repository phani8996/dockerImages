import sys
from notebook.auth import passwd

default_passwd="tonystark"
args=sys.argv
if len(sys.argv) != 4:
   print("Invalid number of args. Run as python create_passwd.py <filename> <passwd> <base_url>")
   sys.exit(1)

def generate_passwd(pwd):
    return passwd(pwd)


jupyter_config="""
c.NotebookApp.allow_password_change = False                      
c.NotebookApp.password = '{}'
c.NotebookApp.password_required = True
c.NotebookApp.allow_root = True
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888                                             
c.NotebookApp.open_browser = False
c.NotebookApp.base_url='{}'
"""
filename=args[1]
jupyter_passwd = args[2]
base_url = args[3]
with open(filename, "w") as f:
    f.write(jupyter_config.format(generate_passwd(jupyter_passwd), base_url))
