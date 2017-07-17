start = '''
You're online searching for a plane ticket to your favorite place in the country! Do you save money and book a flight
in the back of the plane, or splurge and treat yourself to first class?
'''

front = '''
Welcome to first class! You take you window seat and recline your chair getting comfortable. A flight attendant comes by and hands
you a pillow and blanket. Pretty soon, you're in the air. You place your pillow behind your head and turn your head to look out the
window.
'''
view = '''
 Look down... hm, is that the Pacific Ocean or Lake Michigan?
 '''
surf = '''
You turn to your right when you feel someone tap your shoulder. You look at this man wondering what he wants. Is he, 1) A tall brunette in a winter coat or
2) A tan blonde with broad shoulders and long hair?
'''

back = '''
You make your way to the back of the plane, and find yourself sitting in the last row in the middle seat. The guy on your left smells
pretty bad, and you can barely see out the window- you're favorite part about flying! On top of the nasty smell coming from the man next
to you, you can also smell the stench comig from the bathroom. Is this even worth saving that money you could've spent for first class?
You see the flight attendant come by about an hour after takeoff, and hope that there's still some good food left after she went through
selling it to the whole plane.
'''

water = '''
The flight attendant approaches you! Does the flight attendant have water availible?
'''

city = '''
Ooh! We're getting closer to landing. You can make out a tower- but is it a skyscraper?
'''

california = '''
Rad! You're on your way to California. Enjoy the weather and the waves!
'''

chicago = '''
The windy city is waiting for you! You're on your way to Chicago. Enjoy the city!
'''
def views():
    print(view)
    done = False
    while not done:
        user_input = str (input("Type 'lake' if it's Lake Michigan or 'pacific' if it's the Pacific Ocean: "))
        if user_input == "lake":
            print(city)
            skyscraper()
            done = True
        elif user_input == "pacific":
            print(california)
            done = True
        else:
            print("Please type 'pacific' or 'lake'");
def water_question():
    print(water)
    done = False
    while not done:
        user_input = str (input("Type 'yes' if she has water for you or 'no' if she doesn't have water: "))
        if user_input == "yes":
            print(chicago)
            done = True
        elif user_input == "no":
            print(surf)
            surfer()
            done = True
        else:
            print("Please type 'yes' or 'no'");

def skyscraper():
    done = False
    while not done:
        user_input = str (input("Type 'skyscraper' if it's a skyscraper or 'tower' if it's just some lame tower: "))
        if user_input == "skyscraper":
            print(chicago)
            done = True
        elif user_input == "tower":
            print(surf)
            surfer()
            done = True
        else:
            print("Please type 'skyscraper' or 'tower'");

def surfer():
    done = False
    while not done:
        user_input = str (input("Type '1' if he matches description 1) or '2' if he matches description 2): "))
        if user_input == "1":
            print(chicago)
            done = True
        elif user_input == "2":
            print(california)
            done = True
        else:
            print("Please type '1' or '2'");


print(start)
done = False
while not done:
    user_input = str (input("Type 'front' to purchase a seat in the front of the plane or 'back' to purchase a seat in the back of the plane: "))
    if user_input == "front":
        print(front)
        views()
        done = True
    elif user_input == "back":
        print(back)
        water_question()
        done = True
    else:
        print("Please type 'front' or 'back'");

