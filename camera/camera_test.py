import time
import cv2

import math
#print(round(1.0))

Camera_source = 1
Resolution_X, Resolution_Y = 960, 540
Scale = 1 
# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)
print(cv2.getBuildInformation())
cap.set(cv2.CAP_PROP_FRAME_WIDTH, Resolution_X)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Resolution_Y)
#print(cap.get(cv2.CAP_PROP_FPS))
while(True):
  # 從攝影機擷取一張影像
  tstart = time.time()
  ret, frame = cap.read()
  #frame = cv2.resize(frame, (960 , 540))
  #tget1 = time.time()

  # 顯示圖片
  cv2.imshow('frame', frame)
  #tget2 = time.time()
  #print('time1 ',round(tget1-tstart,2),'time2 ',round(tget2-tget1,2))

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()


    #Set Resolution     Real size is determined by EX width and height
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, Resolution_X)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Resolution_Y)
    #real_cam_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    #real_cam_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #print('Size Width: ',real_cam_width,' Length: ',real_cam_height)
    #cap.set(cv2.CAP_PROP_FPS, 30)
