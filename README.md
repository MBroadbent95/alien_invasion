ReadMe Sections

Description

- In Alien Invasion, the player controls a rocket ship that appears
  at the bottom center of the screen. The player can move the
  ship right and left using the arrow keys and shoot bullets using
  the spacebar. When the game begins, a fleet of aliens fills the
  sky and moves across and down the screen. The player shoots
  and destroys the aliens. If the player shoots all the aliens, a new
  fleet appears that moves faster than the previous fleet. If any
  alien hits the player’s ship or reaches the bottom of the screen,
  the player loses a ship. If the player loses three ships, the game
  ends.

- This was my first independant project since completing my bootcamp at the start of the year. I completed this project solo, over the course of a 1 month whilst balancing both professional and social obligations.
  My main goal was to increase my proficiency with Python, gaining more confidence and programming experience is essential for an up and coming junior/ graduate looking to break into the industry.

My thought process was, since I had previously completed a similar project in vanilla JavaScript to cut my teeth on said software, then it would be good practice to see if i could do something similar on this alternate and in demand programming language.
In a nutshell, this is the classic Space Invaders. Constructed in vanilla Python with the aid of PyGame.

Deployment link

tbc ---------------------------------------------WATCH THIS SPACE-------------------------------------------

Instructions

Here include the information on where the deployed project can be found. If login details are needed to access the full project, make sure you include them.

- Here is the deployment link to my project
  [Link](INSERT LINK HERE)

  Getting Started/Code Installation:

- Feel free to access my code via my GitHub repository:
  Alien Invasion - ------------------ WATCH THIS SPACE ----------------------------------------------
  Necessary Installations are as follows:
  Python
  Pygame

Timeframe & Working Team (Solo/Pair/Group):

- This project was completed solo over the course of just over a month.
  Officially starting on July 22, and achieving MVP on August 27.

Technologies Used:

Python
Pygame

Brief:

- Build a robust and functional variant of the classic Space Invaders game using Python.

Planning:

For this project, I followed the guide provided to me by the extremely helpful and well written "Python Crash Course 3rd Edition" by the talented Eric Matthes. Like with documentation, I would read the plan provided by PCC and then implement it piece by piece.
There were complications along the way, such as filepath planning for reading documents.
This clearly was not a problem for the author but just needed a workaround for my experience, you will see from the image below, my solution.

![Filepath Trouble](-----------------------------------------------------------------------------------------)

This bump in the road was the only real obstruction I faced during development, the rest of my experience was  straightforward.

Build/Code Process:

As mentioned before, this project was primarily guided with the aid of the "Python Crash Course 3rd Edition" by Eric Matthes.
My build process revolved around following the helpful steps laid out before me.

The code process itself took place just over a month in length, which is far less than it felt like.

Because this was not necessarily my designed code, as a good student, I would attempt to understand it at each step of the way. Much of the game's methods were implemented via pygame - which is an open source library of python modules designed for writing video games. Whilst I may have not known how each module was exactly written, I could see them being used very effectively by Mr Matthes. This brought me great confidence to infer what exactly each component was doing and understand why the game was written as it was.
For example, throughout the game you would need to define both the internal score number, and then in order to display it, you would need to create a new image each time the score updated and project that onto the player's screen. This can be seen from the below code snippet.
![Score Image Conversion]()


Building Alien Invasion in python has given me a more in depth understanding of the popular industry practice, object oriented programming.

Just from scroilling alone, you can see how much more clean and easier to read everything is when compared to my first attempt at alien invaders back for my first project in vanilla JavaScript.
![Vanilla JS from Proj 1]()

![Alien Invasion Clean OOP]()

In the months leading up to assembling the project, I was working my way through the crash course book.
This was a very convenient way of expanding what I had previously learned about python whilst also balancing my obligations.
At about 80% of the way through this project, I had landed a new job and could not spend as much time on development as I had previously.
This resulted in the final stages of the project feeling a lot more longer than they actually were. In light if this, I am rather proud that I was able to progress the project despite my higher priority obligations. 


Challenges:

- It took me a short moment to understand what Mr Matthes was assembling with each part and how it was relevant to the wider project. I am confident that this is a common feeling with Junior's getting to grips with the finer aspects of project design.

- A challenge previously mentioned was the need to specify my file path in order to write files. During my self education in the previous chapters of the Crash Course book, the advised code did not work on my device. In light of this, I searched for a work around and found an appropriate solution. This solution involved importing os at the top, defining a filepath and using that in my module. This solved the problem and provided me a solution to call upon should this problem occur again in future.

Wins/ Key Learnings/ Takeaways:

- I managed to follow the documantation to the letter and adapt appropriately whenever something did not go as planned. I am confident that this demonstrates my problem solving ability as a Junior and would look good to prospective employment.
- My ability to program using Python has grown, my confidence will reflect this.

Bugs:

- During development I have not become aware of any substantial bugs. Should any occur, please reach out to me.

Future Improvements:

- Power ups, occasionally a power up would drop from the top of the screen which would enhance the player. This could include anything from increasing the width of the bullet 'WIDE SHOT', to increasing the rate of fire with unlimited shots (currently the shot limit is 3).

- The aliens could start to drop bombs. Currently the only win condition for the aliens is to reach the bottom of the screen. This would add an additional layer of difficulty and increase player engagement.