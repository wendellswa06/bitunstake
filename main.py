import pexpect
import re
import sys
import time
import traceback
from datetime import datetime
import getpass

# configure options for your command
wallet = "JJcold"#"main-wallet"       # wallet name of your coldkey
# hotkeys = ["JJwarm", "JJhot", "JJa", "JJb", "JJc", "JJd", "JJe", "JJf", "JJg", "JJh", "JJi", "JJj"] #["mining-hotkey-2"]        # a list with the names of all the hotkeys you want to register
hotkeys = ["Zf"]
# print('Type in your password:')
password = str(getpass.getpass('Type in your password:'))        # password for your coldkey
iterate = True 

# start registraion bot
while True:
    for hotkey in hotkeys:
        while iterate:
            try:
                command = 'btcli stake remove --wallet.name {} --wallet.hotkey {}'.format(wallet, hotkey)
                
                # Format the time as HH:MM:SS
                formatted_time = datetime.now().time().strftime("%H:%M:%S")
                
                # Print the formatted time
                print("\nColdkey: ", wallet, "\nHotkey: ", hotkey, flush=True)
                print(formatted_time, flush=True)

                child = pexpect.spawn(command)                
                child.sendline('y')
                child.sendline('y')
                
                child.expect('Enter password to unlock key')
                child.sendline(password)
                child.sendline('y')
                print('unstake successfully')
                break
            except Exception as e:
                print("An error occured", e)
                print(traceback.format_exc())
                child.sendintr()             # Send Ctrl+C
                child.expect(pexpect.EOF)    # Wait for the command to exit
                if iterate:
                    break
                else:
                    continue
