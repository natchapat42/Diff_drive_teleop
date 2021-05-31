#!/usr/bin/env python3

import rospy

import getch

from geometry_msgs.msg import Twist

velocity = 1

angular = 0.2

msg = """

How to control this robot ?

Press W : Forward

Press A : Turn Right

Press S : Backward

Press D : Turn Left

Press X : Stop

Press E : + speed 0.2

Press R : - speed 0.2

"""

def teleop():

    global velocity

    global angular

    print(msg)

    # define node
    
    rospy.init_node('teleop', anonymous=True)

    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)

    message = Twist()

    while not rospy.is_shutdown():

        # Reset input from keyboard

        #char = ''

        # get input from keyboard

        char = getch.getch()

        # Front

        if char == 'w' :

            message.linear.x = velocity

            message.angular.z = 0

        # Right

        elif char == 'a' :

            message.linear.x = 0

            message.angular.z = angular

        # Stop

        elif char == 'x' :
    
            message.linear.x = 0

            message.angular.z = 0

        # Back

        elif char == 's' :
    
            message.linear.x = -velocity

            message.angular.z = 0

        # Left

        elif char == 'd' :
        
            message.linear.x = 0

            message.angular.z = -angular

        # Faster
            
        elif char == 'e' :

            velocity += 0.2

            print("Velocity = " + str(velocity))

        # Slower

        elif char == 'r' :
    
            velocity -= 0.2

            print("Velocity = " + str(velocity))

        # Publish message to /cmd_vel

        pub.publish(message)

if __name__ == '__main__':

    try:

        teleop()

    except rospy.ROSInterruptException:

        pass
