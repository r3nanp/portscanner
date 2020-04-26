from datetime import datetime
import sys, os, time

# Color
B = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'

### Code time ######
now = datetime.now()
minute = now.minute
hour = now.hour
day = now.day
month = now.month
year = now.year
##################

banner = '''[1] Start the scan
[2] Exit'''

verf = (B+G+'[!] The scan started on {0}:{1} | {2}-{3}-{4}'.format(hour, minute, day, month, year))

def wrongInput():
    print(R+'\n[!] There is an error')
    print('[!] Restarting...')
    time.sleep(1)
    restart_program()
            
###### Restart the program ####
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
######################
def exit():
    time.sleep(0.3)
    sys.exit(1)
    

      