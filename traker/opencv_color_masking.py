
import cv2
import numpy as np

# HSV format(8 bytes) => [ 0~180, 0~255, 0~255]

# define range of blue color in HSV
lower_blue = np.array([110,50,50]) #lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])#upper_blue = np.array([130,255,255])

# define range of green color in HSV 
lower_green = np.array([50,50,100])
upper_green = np.array([70,255,255])

# define range of red color in HSV 
lower_red = np.array([-10,100,100])
upper_red = np.array([10,255,255])

# define range of white color in HSV 
lower_white = np.array([0,0,240])
upper_white = np.array([150,5,255])

# define range of yellow color in HSV 
lower_yellow = np.array([20,50,100])
upper_yellow = np.array([40,255,255])

def colorMasking(frame):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    # Threshold the HSV image to get only green colors
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    # Threshold the HSV image to get only red colors   
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    # Threshold the HSV image to get only red colors   
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    # Threshold the HSV image to get only red colors   
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    return mask_blue, mask_green, mask_red, mask_white, mask_yellow
    pass

def colorMasking2( frame, lower,upper):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Threshold the HSV image to get only blue colors
    mask_color = cv2.inRange(hsv, lower, upper)
    res_img = cv2.bitwise_and(frame,frame, mask= mask_color)
    return mask_color, res_img
    pass

def imgProcess(frame,t1,t2,bw,type):
    #模糊化
    #result = cv2.blur(frame, (5,5))
    
    if type ==2:
        _,frame = colorMasking2(frame,(0,0,80),(180,255,255))
    
    result = cv2.GaussianBlur(frame, (5, 5), 0)
    #result = cv2.medianBlur(frame, (5,5))
    #灰階
    gray=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    if type == 1 :
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    elif type == 2:
        ret2,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #print (ret2)
    elif type == 4:
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    elif type == 3:
        ret, thresh = cv2.threshold(gray, bw, 255, cv2.THRESH_BINARY)
    else:
        ret, thresh = cv2.threshold(gray, bw, 255, cv2.THRESH_BINARY)
    # 使用型態轉換函數去除雜訊
    kernel = np.ones((2, 2), np.uint8)
    if type == 4 :
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
        thresh = cv2.dilate(thresh, kernel, iterations=1)
        thresh = cv2.bitwise_not(thresh)
    else :
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    #cv2.imshow('black_white',thresh)
    #param1的具體實現，用於邊緣檢測
    canny = cv2.Canny(thresh, t1, t2, apertureSize = 3)   #image src: frame or thresh
    #cv2.imshow('edges', canny)
    return thresh, canny
    pass

def imgProcess2(frame):
    cut = cv2.GaussianBlur(frame, (5, 5), 0)
    gray=cv2.cvtColor(cut,cv2.COLOR_BGR2GRAY)
    ret2,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel1 = np.array([[0, 0, 1, 1, 0],
                        [1, 1, 1, 1, 0],
                        [1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 1],
                        [0, 1, 1, 0, 0]], dtype= "uint8")
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel1, iterations=4)
    kernel = np.array([ [0, 1, 1, 0, 0],
                        [0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 0],
                        [0, 0, 1, 1, 0]], dtype= "uint8")
    thresh= cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    canny = cv2.Canny(thresh, 30, 150, apertureSize = 3)  
    cnts,  hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return cnts
    pass
    
def roi(img,vertices):
    # blank mask:
    mask = np.zeros_like(img)
    #mask = cv2.bitwise_not(mask)
    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillConvexPoly(mask, vertices, (255,255,255))
    # returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked
    
