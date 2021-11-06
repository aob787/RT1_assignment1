from __future__ import print_function

import time
from sr.robot import *
"""
To run this code use the following command
	$python2 run.py assignment1.py
Tachadol Suthisomboon 5240225
"""

# to intialize the variable for litmit the radius of detection

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity

    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity

    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest silver token

    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

def find_golden_token():
    """
    Function to find the closest golden token

    Returns:
	dist (float): distance of the clo# to intialize the variable for litmit the radius of detection
box_detection_r = 100;sest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
		return -1, -1
    else:
   		return dist, rot_y

	
"""
Basically, two of fuctions be low work in same algorithm. The first one for golded boxeso, and the secound for silver boxes.
It takes scanning_range and angle
for example scanning range is how for that boxes will be take into account.
scanning_angle is which angle that the robot will aimed for.
angle_range is plus and minus to scanning_angle to increse the range. Let's think if we use 15 degs and didn't + and - no boxes will be found it maybe but rarely

for example:
 scan_obstacal(1m, 0, 90)
 robot will find golden boxed in 1m from robot between -90 degs to 90 degs.
"""
def scan_obstacal(scaning_range, scaning_angle, angle_range):
	for token in R.see():
		if (token.dist < scaning_range and token.rot_y > scaning_angle-angle_range and token.rot_y < scaning_angle +angle_range and token.info.marker_type is MARKER_TOKEN_GOLD):
			#print(token.dist, token.rot_y)
			return True

	return False

def find_silver(scaning_range, scaning_angle, angle_range):
	for token in R.see():
		if (token.dist < scaning_range and token.rot_y > scaning_angle-angle_range and token.rot_y < scaning_angle +angle_range and token.info.marker_type is MARKER_TOKEN_SILVER):
			#print(token.dist, token.rot_y)
			return True

	return False


"""
----------------The program start below -------
"""

drive(100, 3) # just drive straight

while 1: # while loop for keep code running forever
	
"""
I implemented 3 condition
1. if there is silver box infront of the robot the robit will go to pick the box and place it behide the robot
2. if there are no golden box in front of robot (Let's say from -22.5 to 22.5 (this value obtain by tuning)) in 1.2 [unit]. 
   The robot will continue go straight 
3. if there are gold boxes the robot will find the direction that it has to turn.
   First the robot will check in length 3 [unit] from 0, -25, 25, -35, 35 to -100, 100.
   It can not find the free path the length will decrese to 2.5 and 1.5 (This prevent the case that we use far length and it stick in some corners
   But if we use small value at first the robot can get into wrong direction in some cases)
   *Note that the robot will turn proporsional to the angle that its found
   turn(34,0.01*i) <- this value obtain by trail and error, but the result is robot tend to turn to the desired path
"""
	if  (find_silver(1.2, 0, 90) == True):
		print("jer")
		dist, rot= find_silver_token()
		while (rot*rot > 0.1):
			dist, rot= find_silver_token()
			print(rot*rot)
			if rot < 0:
				turn(-30,0.01)
			else:
				turn(30,0.01)
		while (dist > 0.4):
			dist, rot= find_silver_token()
			drive(30,0.01)
		print("Grab")
		R.grab()
		turn(-34,0.01*180)
		R.release()
		turn(-34,0.01*180)

	elif (scan_obstacal(1.2, 0, 22.5) == False):
		drive(100, 0.1)

	else :
		h=3
		flag=True
		while(h>0.5 and flag == True):
			for i in range(25, 100, 10):
				if (scan_obstacal(h, -i, 15)== False):
					print(-i)
					turn(-34,0.01*i)
					flag = False
					break
				elif (scan_obstacal(h, i, 15)== False):
					print(i)
					turn(34,0.01*i)
					flag = False
					break
			h = h-1




"""
#This part is for calibrating the range of detection by print all of boxes
#So, we can know how the unit should we use
markers = R.see()
print ("I can see", len(markers), "markers:")
for m in markers:
	if m.info.marker_type in (MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER):
		print (" - Token {0} - {1} is {2} metres away".format( m.info.marker_type, m.info.offset, m.dist ))
	elif m.info.marker_type == MARKER_ARENA:
		print (" - Arena marker {0} is {1} metres away".format( m.info.offset, m.dist ))
"""
