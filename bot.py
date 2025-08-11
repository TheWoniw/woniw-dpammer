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
    print("|---- ENTER MESSAGE ----|")
    message = str(input(f"||$||: "))
    data['user_message'] = message

    data['user_message'] = message
    save_json(data, json_path)


    return message
    
def find_cycles():
    print("|---- ENTER AMOUNT OF CYCLES ----|")
    cycles = int(input(f"||$||: "))
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

        if I == cycles:
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


def main():
    cycle = find_cycles()
    print("")
    time.sleep(1)
    print("")
    spam_message = user_inputs()
    time.sleep(5)
    print(f"{GREEN}|----- LOGS -----|")
    start_cycles(cycle, spam_message)


main()
#TODO
# - Lock onto discord message