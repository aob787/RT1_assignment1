Python Robotics Simulator - Assignment 1 Research Track I
================================
Modified by Tachadol Suthisomboon
This repository was forked from the Reserch track 1 - assignment repository. The work is the part of Research track 1 course.

This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and the exercises have been modified for the Research Track I course

Tasks
--------------------
-Make the keep running in the arena with same direction (i.e., counter-clockwise or clockwise) with out touching gold boxes
-When the robot found the silver box, the robot should grab and place it behind itsself

Pseudocode
--------------------
```
While True:
    if there is silver box in front (from -90 degs to 90 degs) of robot in xx m:
        find the position and angle of box
        while distance of box > distance treshold and abs(angle of box) > angle treshold:
            if distance of box > distance treshold:
                drive(forward for a while)
            if abs(angle of box) > angle treshold and angle of box >= 0:
                turn(clockwise)
            if abs(angle of box) > angle treshold and angle of box < 0:
                turn(counter-clockwise)
        grab()
        turn(180degs)
        place()
        turn(180degs)
    elif there are no golden box in front (from -30 degs to 30 degs) of robot in xx m:
        drive(forward for a while)
    else:
        for i in range(90):
            if there are no golden box in i degs of robot in xx m:
                turn(to that direction (i))
            elif there are no golden box in -i degs of robot in xxm:
                turn(to that direction (-i)       

Function to find the box
def Find_box(angle, range, distance, type of box):
    for box in all of box that robot see:
        if box angle is between angle-range and angle+range and box distance is less than distance and box is the same type with type of box:
            return True
     return False
```
The pseudocode describe the algorithm that robot should do. Firstly, the robot finds silver box in front of itself. Secondly, the robot check the obstacle in front of it, if there are no obstacle robot will move forward. So, last statement is for find which way that robot should turn to by increasing the angles of scanning.

To implement this code, we have to do some experiment:
1. Play with turn fucntion to know how much should we use to turn in each degrees.
2. Play with the dist parameter of boxes. So, we can guess the initial value of detection range of robot.

Implemented code
--------------------

There are comments in code (assignment1.py). So, I have tuned some code and add some feature to get robot work reliably.


Installing and running
----------------------
To run this code
[python2 run.py assignment.py]

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

## Troubleshooting

When running `python run.py <file>`, you may be presented with an error: `ImportError: No module named 'robot'`. This may be due to a conflict between sr.tools and sr.robot. To resolve, symlink simulator/sr/robot to the location of sr.tools.

On Ubuntu, this can be accomplished by:
* Find the location of srtools: `pip show sr.tools`
* Get the location. In my case this was `/usr/local/lib/python2.7/dist-packages`
* Create symlink: `ln -s path/to/simulator/sr/robot /usr/local/lib/python2.7/dist-packages/sr/`

