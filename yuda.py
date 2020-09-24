import time
import webbrowser

# settings
clear_screen_lines = 100
wait_time = 2

def dots(dots_wait_time = 0.5, iterations = 1):
    for i in range(iterations):
        print(".")
        time.sleep(dots_wait_time)
        print("..")
        time.sleep(dots_wait_time)
        print("...")
        time.sleep(dots_wait_time)

def clear_screen(lines):
    print("\n" * lines)

def google_search(food_to_search, location):
    return "http://www.google.com/search?q=" + food_to_search.replace(' ', '+') + "+deliveries" + "+in+" + location.replace(' ', '+')

clear_screen(clear_screen_lines)
name = input("Hi! What is your name? \n").strip().title()
clear_screen(100)

print("Hi {}! My name is Yuda.".format(name))
time.sleep(wait_time)
print("I'm the first virtual cat that\'s gonna help you get food fast and easy!")
time.sleep(wait_time*2)
print("please let me ask you some questions...")
time.sleep(wait_time)
dots()
food = input("{}, what would you like to eat?\n".format(name)).lower()
clear_screen(100)

print("Ahh, That\'s nice! I also like {}!".format(food))
time.sleep(wait_time)
location = input("{}, where are you?\n".format(name))
clear_screen(100)

print("I've found some results for {} deliveries in your area on google. let me show you them!".format(food))
time.sleep(wait_time*2)
webbrowser.open(google_search(food, location))

# credits
print("Created by Dan Koren")
time.sleep(wait_time)
print("Press Enter to exit")
input('')
