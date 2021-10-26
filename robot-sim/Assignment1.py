from __future__ import print_function

import time
from sr.robot import *
"""
To run this code use the following command
	$python2 run.py assignment1.py
"""

# to intialize the variable for litmit the radius of detection


a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
""" float: Threshold for the control of the linear distance"""

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

drive(100, 3)

while 1:
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
#this part is for calibrating the range of detection by print all of boxes
markers = R.see()
print ("I can see", len(markers), "markers:")
for m in markers:
	if m.info.marker_type in (MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER):
		print (" - Token {0} - {1} is {2} metres away".format( m.info.marker_type, m.info.offset, m.dist ))
	elif m.info.marker_type == MARKER_ARENA:
		print (" - Arena marker {0} is {1} metres away".format( m.info.offset, m.dist ))
"""
