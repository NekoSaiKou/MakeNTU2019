import cv2
import numpy as np
from opencv_color_masking import colorMasking2
from opencv_color_masking import imgProcess
from opencv_color_masking import roi
import random
# 開啟網路攝影機
cap = cv2.VideoCapture(1)#1'video1_Trim(2).mp4'
#cap = cv2.VideoCapture(0)
# 設定影像尺寸
width = 640
height = 480

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# 初始化平均影像
ret, frame = cap.read()
t0 = cv2.blur(frame,(4,4))


def diff(frame0,frame1):
    found = True
    copy = np.zeros_like(frame1)
    t0 = cv2.blur(frame0.copy(), (4, 4))
    t1 = cv2.blur(frame1.copy(), (4, 4))
    # 計算目前影格與平均影像的差異值
    diff = cv2.absdiff(t0,t1)
    frame0 = frame1
    black_white, canny = imgProcess(diff.copy(),30,150,50,3) #type 1: adptive 2: ostu 3: simple
    cnts,  hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    '''
    l2d = []
    for c in cnts:
        for d in c:
            l2d.extend(d.tolist())
            for k in d:
                cv2.circle(copy, (k[0],k[1]), 2, (0, 255, 0), 1)

    allcnt = np.array(l2d)
    #print(allcnt)
    center =(100,100)
    '''
    if len(allcnt)>0 and cv2.contourArea(allcnt) > 0:
        hull = cv2.convexHull(allcnt)
        cv2.drawContours(copy, [hull], -1,  (255,0,0), 2)
        m = cv2.moments(allcnt)
        center = (int(m["m10"]/m["m00"]),int(m["m01"]/m["m00"]))
    else:
        found = False
    if found:
        text = 'FIND'
    else :
        text = 'FALSE'
    cv2.circle(copy, center, 10, (255,255,255), -1)
    cv2.putText(copy,text, (int(frame.shape[1]/2)-500, int(frame.shape[0]/2)+200), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 5, cv2.LINE_AA)
    cv2.namedWindow('DIFF',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('DIFF',int(frame.shape[1]/2), int(frame.shape[0]/2))
    cv2.imshow('DIFF',copy)
    return frame0,frame1, center, found
    pass


while(cap.isOpened()):
    # 讀取一幅影格
    ret, frame = cap.read()
    mask = np.zeros_like(frame)
    if ret == False:
        break
    # 模糊處理
    #t1 = cv2.blur(frame.copy(), (4, 4))
    t1 = cv2.GaussianBlur(frame.copy(), (5, 5), 0)
    #_,t1 = colorMasking2(t1,(0,0,180),(132,25,255))
    
    
    # 計算目前影格與平均影像的差異值
    diff = cv2.absdiff(t0,t1)
    t0 = t1
    cv2.namedWindow('DIFF',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('DIFF',int(frame.shape[1]/2), int(frame.shape[0]/2))
    cv2.imshow('DIFF',diff)
    # 將圖片轉為灰階
    '''
    mask_blue, mask_green, mask_red, mask_white, mask_yellow=colorMasking(diff)
    res_white = cv2.bitwise_and(frame,frame, mask= mask_white)
    '''
    black_white, canny = imgProcess(diff.copy(),30,150,50,3) #type 1: adptive 2: ostu 3: simple
    #black_white = cv2.bitwise_not(black_white)
    cnts,  hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts, -1, (0,255,255), 2)

    '''
    l2d = []
    for c in cnts:
        for d in c:
            l2d.extend(d.tolist())
            for k in d:
                cv2.circle(mask, (k[0],k[1]), 50, (255, 255, 255), -1)
    
    black_white2, canny2 = imgProcess(mask,30,150,125,4)
    cnts2,  hierarchy = cv2.findContours(canny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in cnts2]
    if(len(areas)>0):
        max_index = np.argmax(areas)
        cnt=cnts2[max_index]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(mask,(x,y),(x+w,y+h), (0,255,0),2)
        cut = roi(frame,cnt)
    '''
    #cutReal = roi(frame,cnts)
    centers = []
    
    '''
    for c in cnts :
        color = [random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)]
        if cv2.contourArea(c) > 50:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),2)
    '''
    # 顯示偵測結果影像
    cv2.namedWindow('Output',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('Output',int(frame.shape[1]/2), int(frame.shape[0]/2))
    cv2.imshow("Output", frame)
    '''
    cv2.namedWindow('Output2',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Output2',int(frame.shape[1]/2), int(frame.shape[0]/2))
    cv2.imshow("Output2", cut)
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    
cap.release()
cv2.destroyAllWindows()
