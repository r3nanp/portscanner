from datetime import datetime

import sys, os, time

##### Color #####
R = '\033[31m'
G = '\033[32m'
#######

banner = '''[1] Start the scan
[2] Exit'''

###### Restart the program ####
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
######################

def exit():
    time.sleep(0.3)
    sys.exit(1)

### Code time ######
now = datetime.now()
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year
##################

       