import cv2
import numpy as np
from opencv_color_masking import colorMasking
from opencv_color_masking import colorMasking2
from opencv_color_masking import imgProcess
from opencv_color_masking import roi
#from fieldRead import findMaxcontour
import random


def diff(frame0,frame1):
    found = True
    copy = np.zeros_like(frame1)
    t0 = cv2.blur(frame0.copy(), (4, 4))
    t1 = cv2.blur(frame1.copy(), (4, 4))
    # 計算目前影格與平均影像的差異值
    diff = cv2.absdiff(t0,t1)
    frame0 = frame1
    # 將圖片轉為灰
    black_white, canny = imgProcess(diff.copy(),30,150,50,3) #type 1: adptive 2: ostu 3: simple
    #black_white = cv2.bitwise_not(black_white)
    cnts,  hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #####################################################################################################
    
    l2d = []
    for c in cnts:
        for d in c:
            l2d.extend(d.tolist())
            for k in d:
                cv2.circle(copy, (k[0],k[1]), 2, (0, 255, 0), 1)

    allcnt = np.array(l2d)

    #####################################################################################################

    center =(100,100)
    areas = [cv2.contourArea(c) for c in cnts]
    if(len(areas)>0):
        max_index = np.argmax(areas)
        cnt=cnts[max_index]
        hull = cv2.convexHull(cnt)
        cv2.drawContours(copy, [hull], -1,  (0,0,255), 2)
        m = cv2.moments(cnt)
        if cv2.contourArea(cnt) > 0:
            center = (int(m["m10"]/m["m00"]),int(m["m01"]/m["m00"]))
        ################################################################
        '''
        if len(allcnt)>0 and cv2.contourArea(allcnt) > 0:
            hull = cv2.convexHull(allcnt)
            cv2.drawContours(copy, [hull], -1,  (255,0,0), 2)
        '''
        ###############################################################
    else:
        found = False
    if found:
        text = 'FIND'
    else :
        text = 'FALSE'
    cv2.circle(copy, pos, 10, (255,255,255), -1)
    
    pos_target = (int((int(frame.shape[0]/2)+pos[0])/2),100)
    cv2.circle(copy, pos_target, 20, (255,0,255), -1)

    cv2.putText(copy,text, (int(frame.shape[1]/2)-500, int(frame.shape[0]/2)+200), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 5, cv2.LINE_AA)
    cv2.namedWindow('DIFF',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('DIFF',int(frame.shape[1]/2), int(frame.shape[0]/2))
    cv2.imshow('DIFF',copy)
    return frame0,frame1, center, found
    pass

# 開啟網路攝影機
cap = cv2.VideoCapture(1)#'video1_Trim(3).mp4'
#cap = cv2.VideoCapture(0)
# 設定影像尺寸
width = 1024
height = 768

cen = [100,100]
pos = (0,0)

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# 初始化平均影像
ret, frame = cap.read()
copy = np.zeros_like(frame)

pos = (int(frame.shape[1]/2), int(frame.shape[0]/2))
#cut0 = frame[(pos[1]-100):(pos[1]+100),(pos[0]-100):(pos[0]+100)]
cut0 = frame
post_pos = pos

area_max = 0
area_tracking =0

while(cap.isOpened()):
    # 讀取一幅影格
    ret, frame = cap.read()
    if ret == False:
        break
    #cut1 = frame[(pos[1]-100):(pos[1]+100),(pos[0]-100):(pos[0]+100)]
    cut1 = frame
    cut0,cut1, centemp, found = diff(cut0,cut1)
    #cut1 = roi(frame,cnt) #場地
    #cut2 = roi(frame,circnt)
    # 將圖片轉為灰階
    weight = 0.7
    if found:
        cen = centemp
        #pos = 0.9*(cen[0]+pos[0]-100,cen[1]+pos[1]-100)+0.1*(int(post_pos[0]),int(post_pos[1]))
        pos_avg = (weight*(cen[0])+(1-weight)*post_pos[0],weight*(cen[1])+0.1*(post_pos[1]))
        pos = (int(pos_avg[0]),int(pos_avg[1]))

    post_pos = pos
    
    cv2.namedWindow('Output',cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('Output',int(frame.shape[1]/2), int(frame.shape[0]/2))
    cv2.imshow("Output", cut0)
    pos_target = (int((int(frame.shape[0]/2)+pos[0])/2),100)
    

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()