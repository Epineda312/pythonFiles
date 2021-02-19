#Hurdle_1
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    for step in range(3):
        turn_left()
        
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
  

#Hurdle_2
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    for step in range(3):
        turn_left()
        
while not at_goal():
    jump()

#Hurdle3
#What you need to know
#The functions move() and turn_left().
#The conditions front_is_clear() or wall_in_front(), 
#at_goal(), 
#and their negation.
#How to use a while loop and an if statement.
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    for step in range(3):
        turn_left()
        
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
