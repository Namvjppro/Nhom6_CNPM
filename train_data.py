import cv2 as cv
import numpy as np
import os
from PIL import Image

path = "Nam"                        # thu muc luu anh train
pathfile_yml = "100.yml"            # Đường dẫn file yml sau khi train
recognizer = cv.face.LBPHFaceRecognizer_create()  #tao bien de train du lieu
List_Anh = os.listdir(path)
faces =[]
for anh in List_Anh:
    face_img = Image.open("Nam/"+anh).convert("L")
    faceNp = np.array(face_img,'uint8')
    faces.append(faceNp)
ID = [1 for i in range(0,len(faces))]
print(len(ID))
recognizer.train(faces,np.array(ID))
recognizer.save(pathfile_yml)
cv.destroyAllWindows()