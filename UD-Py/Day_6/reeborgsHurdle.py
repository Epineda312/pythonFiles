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
        
for step in range(6):
    jump()
   
