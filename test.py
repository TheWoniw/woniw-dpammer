import random

def random_dely_model_2():
    #! no numbers under 3
    possible_dely_times_1 = [3.5, 4.1, 4.8, 5.1, 5.7, 6.6, 6.7, 8.2]

    #! no numbers above 2.3
    possible_dely_times_2 = [1.8, 2, 2.3, 1, 1.6, 1.8, 2.3, 1.2]

    random_dely_time_1 = random.choice(possible_dely_times_1)
    random_dely_time_2 = random.choice(possible_dely_times_2)

    final_random_dely_time_model_2 = random_dely_time_1 - random_dely_time_2
    return final_random_dely_time_model_2

def random_dely_model_1():
    possible_dely_times = [1, 1.5, 1.8, 2, 2.2]

    random_dely_time_model_1 = random.choices(possible_dely_times)
    return random_dely_time_model_1


random_dely_time_model_1 = random_dely_model_1()
final_random_dely_time_model_2 = random_dely_model_2()

print(f"MODEL 1: {random_dely_time_model_1}")
print(f"MODEL 2: {final_random_dely_time_model_2}")
