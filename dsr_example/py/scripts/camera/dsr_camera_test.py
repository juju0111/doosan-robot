#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import cv2,os,threading,time
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String

class img_test():
    def __init__(self):    
        self.bridge = CvBridge()
        self.subscribe_img = rospy.Subscriber('/camera/color/image_raw',Image, self.img_callback)

    def img_callback(self,data):

        cv_image = self.bridge.imgmsg_to_cv2(data,"bgr8")

        (rows,cols,channels) = cv_image.shape
        if cols > 60 and rows > 60:
            cv2.circle(cv_image, (50,50), 10, 255)
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)
 
        # try:
        #     self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        # except CvBridgeError as e:
        #     print(e)


def main():
    it = img_test()
    rospy.init_node("dsr_camera_test_py")
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
   
if __name__=="__main__":
    main()