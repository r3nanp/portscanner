from datetime import datetime

import sys, os

##### Color #####
R = '\033[31m'
G = '\033[32m'
#######

banner = '''
[1] Start the scan
[2] Exit
'''

###### Restart the program ####
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
######################


### Code time ######
now = datetime.now()
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year
##################

       