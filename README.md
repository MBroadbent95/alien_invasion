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

This bump in the road was the only real obstruction I faced during development, the rest of my experience was pleasantly straightforward.

Build/Code Process:

This project needed a good plan if I was to make it through to the end with any app to show for it. As such, my inner project manager took the wheel and I threw together a rough road map for the time ahead of me. Call it a quirk but I love to know where I am in the wider project picture and can't stand now knowing how much needs to be done in X time.
Please see my roadmap below, I added a couple of tasks as I went but the wider picture remained consistent.
![Project 4 Roadmap](https://i.imgur.com/JosN2xk.png)

Much like my previous projects, I decided it would be best to start out with a functional back end. Once that is up and tested, we would then proceed to create a front end and carry on.
My instructors had recently shown me how to test back end functions through automatic testing, this appeared to be a godsend with how much time it would save me testing each individual endpoint on Insomnia.
Once they were written, the tests returned with positive results, my endpoints were working as intended.
Tests are interesting pieces of code to write and execute, I know this is a practice which I will use in the future considering how useful it was.

Here are a couple of code snippets testing get and delete respectively, take a look!:
![Testing get and Delete](https://i.imgur.com/5xzZ1YS.png)

This was my first project using a Python, Flask & PostgreSQL back end, so being relatively new, i lifted a lot of the code from previous coursework and re-applied it to my current project, this worked like a charm and i was able to have my back end up, and tested before the end of the second day, a little behind schedule but the roadmap was optimistic.

At the start of the following week, I was to build my basic front end structure, frameworks and all, and get it talking with my backend so that I can start meaningfully assembling the UI.
In a previous project, I had started using TailwindCSS for my front end framework. TailwindCSS makes CSS styling so smooth and painless as possible, whilst TailwindCSS can be annoying to install correctly, I'm glad I used it in this project too.

On Tuesday I looked into enabling an image upload system so that my users could include a picture of their recipe.
Personally I rarely cook food from recipes without illustrations so this was essential.
Unfortunately this research proved to be much longer than anticipated and I couldn't get my head around the technology effectively.
At this time I was experiencing errors in other areas of the project, namely in the comments and recipe submission/ posting parts. In light of this, I decided it was best to keep the image upload system basic with Imgur links and focus on debugging my other components.
Moving forward I would be interested in learning the technology for image uploading and display, we all know that Imgur uploading is very clunky and not friendly towards the User Experience.

As I recall, on Wednesday I was experiencing persistent issues with my comments system which required attention. I had noticed that it stopped working once I modified my comments serializer on my back end to include Foreign Keys or include_fk. I needed the code to stay the same if I was to keep my Get_Comment function from breaking. I had a crazy idea to create a new comment serializer with everything the same except the include_fk. To my surprise this worked like a charm and whilst it feels like a hack, like a dumb solution, my instructor assured me that it was perfectly fine and in fact not a hack, but it sure feels like one.
See my 'hack' code below haha.
![Super Comment Serializer](https://i.imgur.com/22jV6NY.png)

Thursday was the day before deployment, so ideally MVP would be achieved in order for a smooth deploy process.
Since debugging was something I did as I went along, by midday of thursday, MVP was achieved and I could style, test any endpoints I felt anxious about, and finally populate my api with some tasty recipes.
Data population has always been a tedious part of the development process, so it was always gonna take a dedicated period of time to populate correctly. I decided on 8 recipes as a start to populate the page, 2 users, and 2 comments. We could always log in to add more manually, or even re-seed, I did re-seed a couple of times in this project, initially to check if everything was working as it should and then finally to populate.

![Seed](https://i.imgur.com/RWt8jEV.png)

The final couple of days I spent ad-hoc debugging and placing the finishing styles onto my front end.
The live URL is ![Tasteful Trove](https://main--tasteful-trove.netlify.app/)
Feel free to sign up, add a recipe and comments if you wish. I'm rather happy with the deployed result, there are many improvements to be made and a couple of bugs which I will discuss shortly.
![Tasteful Trove Webpage](https://i.imgur.com/yxnY0om.png)

Moving forward

Challenges:

- A lot of the way Flask works was confusing for me in the beginning, but the more I got my hands on it the more it seemed to make sense.

- One challenge was in the comment serializer, include_fk, this broke my comment system once I added it, and whilst there most certainly is going to be a more elegant solution, my solution was to just create another serializer for posting comments and keep the old one for GET requests. I created the SuperComment serializer which was literally the exact same minus the include_fk and a rename. Just one of those programming quirks which kind of disappoint you when they work.

- Model adjustment, despite saying in my mission statement that I was going to include image uploads, I actually forgot to include images in my initial recipe model, this wasn't super impactful over the span of the project but it does mean I need to bust my own ass to plan a bit more.

Wins:

- Making everything work together was the big victory here. Flask and SQLAlchemy work a bit differently to MongoDB and express, for example MongoDB gives you an id automatically but postgreSQL does not, this was initially rather annoying but I like that I was able to figure out a couple of these quirks throughout this project and make them work for what I wanted to achieve.
- Effective planning was also a considerable win here. Knowing at what stage I am at allows me to assess what to do next and how long I have to spend. Had I not had a roadmap, it is very possible I may have lost more time trying to integrate image uploads and fall behind schedule.

Key Learnings/Takeaways:

This project has helped me develop my confidence with utilising alternative backend frameworks and doing the necessary tasks to understand and integrate those newer frameworks, like Python & Flask, with older more familiar ones such as React.

I have demonstrated to myself that whilst my final product may not be perfect and could probably use stronger styles and a couple more features, I can certainly deliver a clean and functional full stack project within just over a week without asking for much help and assistance. This I am very proud of and brings me confidence moving into future employment.

Bugs:

- The option to delete your original user posted comment only appears after you navigate to another page and then return.
- Infrequently, the images of particular recipes will not load correctly.

Future Improvements:

- Favourites for users, would be awful nice if I could create a shortlist of recipes I like the look of instead of needing to find them every time. It's fine when there's a small number, but once we get over 30 recipes this will gradually make the user experience suffer.

- Admin User, An admin user would've been great to keep the page in check, this can be done with minimal adjustments but my roadmap demanded my attention in other areas.

- User Profile Page, this would have been a large undertaking from scratch and was unlikely to get finished in time if i wanted a smooth mvp, but ideally this feature would include the ability to delete your data, upload a profile picture to add to your comment along with your name, and possibly a dropdown menu to access your favourites.
