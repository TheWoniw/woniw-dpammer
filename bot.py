import pyautogui as pag
import time 

from json_management.json_functions import save_json

from banner import banner

from variables import json_path
from variables import data
from variables import RED

banner()

def user_inputs(cycle):
    message = str(input(f"{RED}Enter message:"))
    final_message = f"{message}"
    data['user_message'] = final_message
    save_json(data, json_path)

    return final_message
    
def find_cycles():
    cycles = int(input(f"{RED}How many cycles would you like to spam: "))
    return cycles

def start_cycles(cycles, spam_message):
    for I in range(cycles):
        #! setting message
        spam_message_complete = f"{spam_message} || **COUNT: {I}**"
        end_message_1 = "||note: Remon made me do this, dont blame me please||"
        end_message_2 = "||Woniw Dpmmer (made by:Woniw) ||"

        I += 1
        time.sleep(1)
        pag.write(spam_message_complete)
        pag.hotkey("enter")

        if I == cycle:
            pag.write(end_message_1)
            pag.hotkey("enter")
            pag.write(end_message_2)
            pag.hotkey("enter")

cycle = find_cycles()
time.sleep(1)
spam_message = user_inputs(cycle)
time.sleep(5)
start_cycles(cycle, spam_message)

#TODO
# - Lock onto discord message