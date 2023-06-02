
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# FIRST WAY TO DO IT

# num_items = len(names)
# random_choice = random.randint(0, num_items -1)
# pagante = names[random_choice]

# SECOND WAY TO DO IT(EASIER)
pagante = random.choice(names)

print(pagante + " Will buy the meal today.")
