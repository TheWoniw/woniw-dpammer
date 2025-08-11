import pyautogui as pag
import random
import time 

from json_management.json_functions import save_json

from banner import banner

from variables import json_path
from variables import data
from variables import RED
from variables import GREEN

banner()

def random_dely_model_2():
    #! no numbers under 3
    possible_dely_times_1 = [3.5, 4.1, 4.8, 5.1, 5.7, 6.6, 6.7, 8.2]

    possible_dely_times_2 = [2.1, 2.4, 2.9, 2, 2.2, 2.7, 3.1, 2.5]

    random_dely_time_1 = random.choice(possible_dely_times_1)
    random_dely_time_2 = random.choice(possible_dely_times_2)

    final_random_dely_time_model_2 = random_dely_time_1 - random_dely_time_2
    return final_random_dely_time_model_2


def user_inputs():
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
        final_random_dely_time_model_2 = random_dely_model_2();

        #! setting message
        spam_message_complete = f"{spam_message}"
        end_message_1 = "||note: Remon made me do this, dont blame me please||"
        end_message_2 = "||Woniw Dpmmer (made by:Woniw) ||"
        end_message_3 = "||https://github.com/TheWoniw/woniw-dpammer||"
        end_message_completed_cycles = f"**{cycles} CYCLES COMPELTED**"

        I += 1
        #! LOG
        print(final_random_dely_time_model_2)
        
        pag.write(spam_message_complete)
        time.sleep(final_random_dely_time_model_2)
        pag.hotkey("enter")

        if I == cycle:
            pag.write(end_message_completed_cycles)
            pag.hotkey("enter")
            time.sleep(1)
            pag.write(end_message_1)
            pag.hotkey("enter")
            time.sleep(1)
            pag.write(end_message_2)
            pag.hotkey("enter")
            time.sleep(1)
            pag.write(end_message_3)
            pag.hotkey("enter")

cycle = find_cycles()
time.sleep(1)
spam_message = user_inputs()
time.sleep(5)
print(f"{GREEN}|----- LOGS -----|")
start_cycles(cycle, spam_message)

#TODO
# - Lock onto discord message