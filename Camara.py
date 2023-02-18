from tkinter import *
#LIBRERIA PIL
try:
    from PIL import Image, ImageTk
except:
    import pip
    print ('Instalando libreria Pillow')
    pip.main(['install','Pillow'])
    from PIL import Image, ImageTk
#LIBRERIA OPENCV      
try:
    import cv2
except:
    import pip
    print ('Instalando libreria OpenCV')
    pip.main(['install','opencv-contrib-python'])
    import cv2
    
    
import sys

def onClossing():
    root.quit()
    cap.release()
    print("Camara desconectada")
    root.destroy()
    
    
def callback ():
    
    ret, frame = cap.read()
    
    if ret:
         img = cv2.cvtColor  (frame, cv2.COLOR_BGR2RGB)
         img = Image.fromarray(img)
         img.thumbnail((400,400))
         tkimage = ImageTk.PhotoImage(img)
         label.configure(image = tkimage)
         label.image = tkimage
         root.after(1,callback)
    else:
        onClossing()
url = "http://192.168.0.108:4747/video"
#url = "rtsp://Usuario:Password@192.168.0.0/video"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("CAMARA CONECTADA")
else:
    sys.exit("CAMARA DESCONECTADA")
    
root = Tk()
root.protocol("WM_DELETE_WINDOW",onClossing)
root.title("CAMARA")

label = Label(root)
label.grid(row=0)

root.after(1,callback)
root.mainloop()