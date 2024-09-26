# In[ ]:## Read image and convert it to grayscale image
## Developed by : 
## Reg no : 
import numpy as np
import cv2
import matplotlib.pyplot as plt
#READ THE GRAY IMAGE USING IMREAD 
#READ THE COLOR IMAGE USING IMREAD
#CONVERT THE COLOR FROM BGR TO RGB
#CONVERT THE COLOR FROM GRAY TO RGB
gray = cv2.GaussianBlur(gray,(3,3),0)
plt.figure(figsize=(13,13))
plt.subplot(1,2,1)
plt.imshow(img_c)
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(gray)
plt.title("Gray Image")
plt.axis("off")
plt.show()

canny=cv2.Canny(gray,120,150)
#DISPLAY THE CANNY IMAGE 
plt.title("Canny Edge Detector")
plt.axis("off")
plt.show()

lines=cv2.HoughLinesP(canny,1,np.pi/180,threshold=80,minLineLength=50,maxLineGap=250)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img_c,(x1,y1),(x2,y2),(255,0,0),3)

plt.imshow(img_c)
plt.title("Result Image")
plt.axis("off")
plt.show()
## Display the result
## Developed by :
## Reg no : 


