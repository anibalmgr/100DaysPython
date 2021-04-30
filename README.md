# 100 days of python
Here I'll be uploading my Angela Yu's 100 days of code files. So far this is more like a diary that helps me to keep track of the learning process and to break down the logic of every exercise.

If you want to see my React code, [click here](https://github.com/anibalmgr/playground)

## [Day 23. Crossing Capstones](./day_23_crossing_capstone)

Another exercise based in the Turtle Module, is pretty much the same logic than the previous exercises but this time the challenge was to make it all by ourselves, just following a few hints. The game has to have a main.py and three classes: Player, Car_manager and  Scoreboard.

The [player](./day_23_crossing_capstone/player.py) is a Turtle that moves up when the space bar is pressed, it returns to its initial position when gets to the top of the screen. I modified a bit the position to create the effect that is the same turtle crossing the wall.

The [car manager](./day_23_crossing_capstone/car_manager.py) controls all the cars (turtles in my case). It has a car method that returns a car created in a random y axis position, and that moves through the screen. The class constantly creates new cars no every screen refresh, to control the amount of cars we generate a random number between 1 and 60 and we only create a car when this number is between 1 and 10. When the player reaches the top of the screen, the method increase_speed() increase the distance a car moves on every refresh and reduces the range of the random number for creating new cars, so we keep a similar amount of cars on the screen.

The [scoreboard](./day_23_crossing_capstone/scoreboard.py) writes the score in the top of the screen, keeps track of the score and calls a "game over" message if the player collisions with a car.

On the [main.py](./day_23_crossing_capstone/main.py) we have three functions, initiatise_screen, game and start game, we only call start_game() and it calls first initialiase_screen, resets the three other classes calling their reset methods, and calls the listen() method to move the turtle with the space bar and start over with "y". The game functions has all the logic of the game, there we detect collision with a car and when we reach the top of the screen, and it calls the respective methods.

### Day 22. [Pong Game](./day-22-pong-game)

We are still using the Turtle Module and we used that to make the [pong game](https://en.wikipedia.org/wiki/Pong). We made a main.py game and a ball, paddle and scoreboard classes. Today I just followed the instructions of the exercise, but I tried to go always one step ahead so I can see if my logic is right.

I am feeling pretty confident about classes and inheritance is making more sense.

### Day 20 and 21. Snake Game.

I decided to do one exercise per week, in order to have time to study react and other code things. I also decided to start writing a bit after every exercise, to get track of the process.

Today I didn't learn anything new, but I understood better how classes work and about inheritance. Also I was able to eliminate some duplicate code. Making the snake game also was fun, as someone that actually played that game a lot.
