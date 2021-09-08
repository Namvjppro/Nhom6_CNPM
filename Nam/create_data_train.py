import cv2 as cv
import os
path_save = "Nam"              #Đường dẫn thư mục lưu các ảnh để train
path_video_train = 0  #Đường dẫn file video để tạo ảnh train
face = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(path_video_train)
n = 0
while True:
    ret, frame=cap.read()                 # ret tra ve true neu truy cap dc, frame: data lay tu webcam
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,225))
        n+=1
        cv.imwrite(path_save+"/user11_"+str(n)+".jpg",gray[y:y+h,x:x+w])
    cv.imshow("Video_webcam",frame)
    cv.waitKey(1)
    if n>500:
        break
cap.release()
cv.destroyAllWindows()

