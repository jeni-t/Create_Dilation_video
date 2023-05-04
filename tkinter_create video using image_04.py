import os
import cv2
import numpy as np
from functools import partial
from PIL import Image
import easygui as eg
import tkinter as tk

root = tk.Tk()
root.title("Image Dilation")
root.geometry('320x50')

def call_result():
    output_path =  eg.fileopenbox(title='Select image file')
    kernel = np.ones((5, 5), np.uint8)
    for file in os.listdir('.'):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            im = Image.open(output_path)
            width, height = im.size
            im = im.resize((int(width/2), int(height/2))) # resize the image
            im.save(file, 'JPEG', quality=95)
    #image_folder = '.' # make sure to use your folder
    #video_name = 'mygeneratedvideo.avi'
    output_path1 = eg.filesavebox(title='Save file to..')
    os.chdir("F:\\python\\AI program\\AI project\\create video")
	
    images = [img for img in os.listdir()
              if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_path1+'.avi', 0, 1, (width, height))
    for image in images:
        for i in range(5, -1, -1):
            img = cv2.imread(image)
            img_dilation = cv2.dilate(img, kernel, iterations=i)
            video.write(img_dilation)
    cv2.destroyAllWindows()
    video.release()
    message_label = tk.Label(root, font=('arial',12,'bold'),text="video created")
    message_label.grid(row=3, column=1)
   
buttonCal = tk.Button(root, text="Upload one image", width=14,height=3,command=call_result).grid(row=3, column=0)


