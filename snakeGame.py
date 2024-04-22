# import modules necessary for the game
import random
import curses

# initialize the curses library to create our screen
screen = curses.initscr()

# hide the mouse cursor
curses.curs_set(0)

# get max screen height and width
height, width = screen.getmaxyx()

# create a new window
window = curses.newwin(height, width, 0, 0)

# allow window to receive input from the keyboard
window.keypad(1)

# set delay for updating the screen
window.timeout(125)

# set the x, y coordinates of the initial position of the sanke's head
snk_x = width // 4
snk_y = height // 2

# define the initial position of the snake's body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# create the food in the middle of the screen
food = [height // 2, width // 2]

# add the food by using DIAMOND character from curses module
window.addch(food[0], food[1], curses.ACS_DIAMOND)

# set initial movement direction to the right
key = curses.KEY_RIGHT

# create a game loop that loops forever untill player loses or quits the game
while True:

# get the next key that will be pressed by the user
    next_key = window.getch()

# if user doesn't input anything, key remains the same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key

# check if the snake collided with the walls or itself
    if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:

# close the window and exit the game if collided
        curses.endwin()
        quit()

# set the new position of the snake's head based on the direction
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

# insert the new head to the first position of snake's list
    snake.insert(0, new_head)

# check if the snake ate the food
    if snake[0] == food:

# remove food if the sanke ate it
        food = None

# while food is removed generate a new food in random position on the screen
        while food is None:
            new_food = [
                random.randint(1, height -1),
                random.randint(1, width -1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_DIAMOND)

# remove the tail if the sanke didn't eat the food
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

# update the position of the snake on the screen
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)