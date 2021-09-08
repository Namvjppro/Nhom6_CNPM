import time
from types import new_class
import cv2 as cv
import numpy as np
from PIL import Image
from connect_Sql_Server import connectSQL
from requests import get

con = connectSQL()

def download(url, file_name):
    # open in binary mode
    if not os.path.exists(file_name):
        with open(file_name, "wb") as file:
            response = get(url)
            file.write(response.content)

def one(username):
    x = con.read("select thoi_gian_online,note from  Danh_Sach_Sv_learning where MaSV = '%s';"%(username))
    l = [i for i in x]
    start = time.time()
    Check = 0
    old = 0
    if len(l)==0:
        Check = 0
        con.insert("insert into  Danh_Sach_Sv_learning values('%s',%s,%s)"%(username,0,0))
    else:
        Check = l[0][1]
        old = l[0][0]
    pathfile_yml = "%s.yml" %(username)
    path_video = 0 
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read(pathfile_yml)
    cap = cv.VideoCapture(path_video)

    while True:
        ret,frame = cap.read()
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray)
        for x,y,w,h in face:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
            roi_gray = gray[y:y+h,x:x+w]
            id,so_chinh_xac = recognizer.predict(roi_gray)
            if so_chinh_xac<40 :
                cv.putText(frame,"Nam",(x+10,y+30),cv.FONT_HERSHEY_PLAIN, 1 ,(0,255,0),2)
                Check+=1
                con.insert("update Danh_Sach_Sv_learning set Note = %s where MaSV = '%s'" %(str(Check),username))
        cv.imshow("cam",frame)
        con.insert("update Danh_Sach_Sv_learning set thoi_gian_online = %s where  MaSV = '%s'"%(str(time.time() - start+old),username))
        if cv.waitKey(1) & 0xff ==ord("q"):
            break
    cap.release()
    cv.destroyAllWindows()

n=1 
while n==1:
    while True:
        username = input("MaSv: ")
        password = input("password: ")
        l = con.read("select * from Sv where MaSv = '%s';" %(username))
        if len(l)==0:
            print("Sai ma SV hoac mk")
        else:
            if l[0][0] == username:
                if l[0][1] == password:
                    break
                else:
                    print("Sai ma SV hoac mk")
            else:
                print("Sai ma SV hoac mk")
    while True:
        print("Menu")
        print("1: Vào lớp học\n2: Xem Điểm\n3: Đổi mk\n4: Đăng xuất\n5: Thoát")
        choice = input("Nhap lua chon: ")
        if choice == '1':
            one(username)
        elif choice == '2':
            print(2)
        elif choice == '3':
            while True:
                new_pass = input("Nhập mk mới: ")
                if new_pass =="":
                    break
                check_new_pass = input("Nhập lại mk: ")
                if new_pass == check_new_pass:
                    con.update("update SV set Mk = '%s' where MaSv = '%s';"%(new_pass,username))
                    print("Thay đổi mk thành công")
                    break
                else:
                    print("Mk không khớp.Hãy nhập lại! ")
        elif choice == '4':
            break
        elif choice =='5':
            n=0
            break
        else:
            continue

#download(l[0][3],username+".yml")


'''pathfile_yml = "phong.yml"
name = "Phong_vip_pro"       #Tên người cần nhận diện 
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read(pathfile_yml)
cap = cv.VideoCapture("phong2.mp4")

while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray)
    for x,y,w,h in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
        roi_gray = gray[y:y+h,x:x+w]
        id,so_chinh_xac = recognizer.predict(roi_gray)
        if so_chinh_xac<40 :
            cv.putText(frame,name,(x+10,y+30),cv.FONT_HERSHEY_PLAIN, 1 ,(0,255,0),2)
    cv.imshow("cam",frame)
    if cv.waitKey(1) & 0xff ==ord("q"):
        break
cap.release()
cv.destroyAllWindows()'''