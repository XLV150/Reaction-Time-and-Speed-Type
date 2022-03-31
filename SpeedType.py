import time
import random

sentences = ["How fast are you really?",
             "When last have you typed for pure speed and accuracy?",
             "I can type extremely fast."]

print("This will test how fast you can correctly type a sentence that is shown to you.")
print()
time.sleep(1)
print("A sentence will now be shown to you within 1 to 5 seconds. Type it out and hit enter. *MATCH EVERY ASPECT OF THE SENTENCE*")
print()
input("Press enter to start! ")
time.sleep(random.randint(1, 5))
choice = random.choice(sentences)
print(choice)
start = time.perf_counter()
user_input = input("TYPE HERE ---->")
finish = time.perf_counter()
timespent_1 = finish - start
print()

if user_input == choice:
    print("Well done you typed the sentence correctly, it took you {} seconds.".format(timespent_1))
else:
    print("You typed it incorrectly, your irrelevant time was {} seconds.".format(timespent_1))