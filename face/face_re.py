import cv2
import face_recognition
import os

path="img"  #模型的路径
cap=cv2.VideoCapture(0) #指定电脑的摄像头
total_image_name=[]
total_face_encoding=[]
#去文件夹底下读图片的名字
for fn in  os.listdir(path):
    print(path+"/"+fn)
    total_face_encoding.append(
        face_recognition.face_encodings(face_recognition.load_image_file(path+"/"+fn))[0])
    fn=fn[:len(fn)-4]
    total_image_name.append(fn)#图片名字列表
while (1):
    ret,frame=cap.read()
    #视频的帧
    face_locations=face_recognition.face_locations(frame)
    face_encodings=face_recognition.face_encodings(frame,face_locations)
    #在这个视频帧中去遍历我们的人脸
    for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
        for i ,v in enumerate(total_face_encoding):
            match=face_recognition.compare_faces([v],face_encoding,tolerance=0.5)
            name="Unknown"
            if match[0]:
                name=total_image_name[i]
                break
        #画一个框来展示当前的脸
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        #画一个带名字的标签放在方框底下
        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
    #显示图像
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) &0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()