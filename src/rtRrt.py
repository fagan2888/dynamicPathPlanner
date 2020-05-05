#!/usr/bin/env python
# license removed for brevity
# import rospy
# from std_msgs.msg import String
# from std_msgs.msg import Float64
import numpy
import matplotlib.pyplot as plot
import random
import time
import os
import math


def ros():
    pub1 = rospy.Publisher('/dynamicPathPlanner/world_base_1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/dynamicPathPlanner/world_base_2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('remote', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data1 = -10
        data2 = -10
        rospy.loginfo(data1)
        rospy.loginfo(data2)
        pub1.publish(data1)
        pub2.publish(data2)
        rate.sleep()


def get_inputs(obstaclex, obstacley):
    print("Enter the start node coordinates separated by spaces: ")
    Xstart, Ystart = list(map(int, input().split()))
    # Xstart, Ystart = obstaclex[0], obstacley[0]
    # while True:
    #     Xstart, Ystart = list(map(int, input().split()))
    #     if Xstart in obstaclex:
    #         if Ystart in obstacley:
    #             # print("Invalid goal node")
    #             continue
    #     break

    Xgoal, Ygoal = random.randint(0, 2000), random.randint(0, 2000)
    for i in range(0,2000):
        if Xstart == obstaclex[i] and Ystart == obstacley[i]:
            print("Input point in the obstacle space")
            os.abort()
        elif(Xstart != obstaclex[i] and Ystart != obstacley[i]):
            # print("Starting node exploration")
            pass

    print("The goal node coordinate is: ", Xgoal, Ygoal)
    print("Starting exploration!!!")

    return Xstart, Ystart, Xgoal, Ygoal


def obstacle_map():

    for x in range(-100,2100):
        for y in range(-100,2100):
            if (x >= 0 and x <= 2000) and (y >= -10 and y <= 0):
                obstaclex.append(x)
                obstacley.append(y)
            if (x >= -10 and x <= 0) and (y >= 0 and y <= 2000):
                obstaclex.append(x)
                obstacley.append(y)
            if (x >= 2000 and x <= 2010) and (y >= 0 and y <= 2000):
                obstaclex.append(x)
                obstacley.append(y)


    return obstaclex, obstacley

def distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def plotMap(obstaclex,obstacley, Xgoal, Ygoal, Xstart, Ystart, X, Y, X_, Y_, Qrandx, Qrandy, Qupdx, Qupdy, Qrandx1, Qrandy1):
    xrect1, yrect1 = (-10,0)
    xrect2, yrect2 = (2010, 0)
    xrect3, yrect3 = (-10, 2010)
    xrect4, yrect4 = (2010, 2010)

    plot.xlim(-100, 2100)
    plot.ylim(-100, 2100)
    plot.plot([xrect1,xrect2],[yrect1,yrect2], 'k-')
    plot.plot([xrect1,xrect3],[yrect1,yrect3], 'k-')
    plot.plot([xrect3, xrect4], [yrect3, yrect4], 'k-')
    plot.plot([xrect2, xrect4], [yrect2, yrect4], 'k-')
    plot.scatter(Xstart, Ystart, marker= '*')
    plot.scatter(Xgoal, Ygoal, marker='+')
    # plot.plot(obstaclex, obstacley, 'k')
    # plot.plot(X, Y,'r')
    # plot.plot(X_, Y_, 'g')
    # Qrandx = xstart
    # Qrandy = ystart


    for i in range(len(Qrandx)):
        plot.plot([xstart, Qrandx[i]], [ystart, Qrandy[i]], 'r-')

    for k in range(len(Qrandx1)):
        plot.plot([Qupdx[0], Qrandx1[k]], [Qupdy[0], Qrandy1[k]], 'r-')

    ############### to be corrected ######################
    for j in range(len(Qupdx)):
        # if (calc_distance(Qrandx[j],Qupdx[j], Qrandy[j], Qupdy[j]) < 50):
        plot.plot([Qrandx[j], Qupdx[j]], [Qrandy[j], Qupdy[j]], 'r-')
    ######################################################
    plot.pause(0.1)
    plot.show()

def obstacleMotion():
    X = []
    Y = []
    X_ = []
    Y_ = []
    c = 0
    while c < 10:
        Xrandom, Yrandom = random.randint(0, 2000), random.randint(0, 2000)
        Xrandom_, Yrandom_ = random.randint(0,2000), random.randint(0,2000)

        Xi, Yi = Xrandom, Yrandom
        Xi_,Yi_ = Xrandom_, Yrandom_
        if (Xi < 2000 and Yi < 2000) and (Xi_ < 2000 and Yi_ < 2000):
            # print("Xi, Yi: ", Xi, Yi)
            X.append(Xi)
            Y.append(Yi)
            X_.append(Xi_)
            Y_.append(Yi_)
        c += 1
    return X, Y, X_, Y_


####### random sampling #######
def lineto():
    return coordinates

def uniform():
    return coordinates

def ellipis():
    return coordinates

###############################

def realtimeRRT(xstart, ystart):

    """kmax = maximum numbers of neighbours around a node
        rs = maximum distance around a node in a tree
        kmax and rs control the tree density
        xrand = randomly generated nodes.
        xclosest = closest node to the root."""



    Qrandomx = []
    Qrandomy = []
    Qrandomx1 = []
    Qrandomy1 = []

    Qupdatedx = []
    Qupdatedy = []
    kmax = 0
    # generate random nodes
    while kmax < 10:
        Xrandom, Yrandom = random.uniform(xstart - 200, xstart + 200), random.uniform(ystart - 200, ystart + 200)

    # if math.sqrt((Xrandom - Xstart)**2 + (Yrandom-Ystart)**2) < 10:
        Qrandomx.append((Xrandom))
        Qrandomy.append((Yrandom))
        if math.sqrt((Xrandom - xstart) ** 2 + (Yrandom - ystart) ** 2) < 100:
            Xclosest = Xrandom
            Yclosest = Yrandom
            # debug
            print(Xclosest, Yclosest, math.sqrt((Xclosest - xstart) ** 2 + (Yclosest - ystart) ** 2))
            #######
            Xupdated = Xclosest + random.uniform(0, 200)
            Yupdated = Yclosest + random.uniform(0, 200)
            Qupdatedx.append(Xupdated)
            Qupdatedy.append(Yupdated)
            Xrandom1, Yrandom1 = random.uniform( 0, 200), random.uniform( 0, 200)
            Qrandomx1.append((Xrandom1))
            Qrandomy1.append((Yrandom1))


        kmax += 1

    # print(Qrandomx)
    # print(Qupdatedx)
    # print(len(Qrandomx))
    # print(len(Qupdatedx))
    # print("-------------------------")



    return Qrandomx, Qrandomy, Qupdatedx, Qupdatedy, Qrandomx1, Qrandomy1



    # random sampling
    # Pr = random.uniform(0,1)
    # if Pr > 1 - alpha:
    #     lineto()
    # if Pr <= (1 - alpha)/beta:
    #     uniform()
    # else:
    #     ellipis()




if __name__ == '__main__':
    # try:
    #     ros()
    # except rospy.ROSInterruptException:
    #     pass

    obstaclex = []
    obstacley = []
    alpha = 0.1
    beta = random.uniform(0,100)

    obstaclex, obstacley = obstacle_map()
    xstart, ystart, xgoal, ygoal = get_inputs(obstaclex,obstacley)
    X,Y, X_, Y_ = obstacleMotion()
    Qrandx, Qrandy, Qupx, Qupy, Qrandx1, Qrandy1 = realtimeRRT(xstart, ystart)
    plotMap(obstaclex, obstacley, xgoal, ygoal, xstart, ystart, X, Y, X_, Y_, Qrandx, Qrandy, Qupx, Qupy, Qrandx1, Qrandy1)

