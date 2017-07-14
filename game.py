start = '''
You're online searching for a plane ticket to your favorite place in the country! Do you save money and book a flight
in the back of the plane, or splurge and treat yourself to first class?
'''

front = '''
Welcome to first class! You take you window seat and recline your chair getting comfortable. A flight attendant comes by and hands
you a pillow and blanket. Pretty soon, you're in the air. You place your pillow behind your head and turn your head to look out the
window. You're close to your destination, so you can see a few skyskrapers if you really try. You think about how much the Willis
Tower in Chicago and the Wilshire Grand Center Tower in California look kind of similar from this high up. 
'''

back = '''
You make your way to the back of the plane, and find yourself sitting in the last row in the middle seat. The guy on your left smells
pretty bad, and you can barely see out the window- you're favorite part about flying! On top of the nasty smell coming from the man next
to you, you can also smell the stench comig from the bathroom. Is this even worth saving that money you could've spent for first class?
You see the flight attedant come by about an hour after takeoff, and hope that there's still some good food left after she went through 
selling it to the whole plane. Finally she approaches you. 
'''

print(start)
done = False
while not done:
    user_input = input("Type 'front' to purchase a seat in the front of the plane or 'back' to purchase a seat in the back of the plane: ")
    if user_input == "front":
        print(front)
        done = True
    elif user_input == "right":
        print(right_hallway)
        print(common_point)
        done = True
    else:
        print("Please type 'front' or 'back'");
        
print(window)
done = False
while not done:
  user_input = input("Type 'wilshire' if you believe that's the tower you see or 'willis' if you believe that's the tower you see. ")
  if user_input == "wilshire":
    print(wilshire)
    done = True
  elif user_input == "willis":
    print(willis)
    done = True
  else:
    print("Please type 'wilshire' or 'willis'");
