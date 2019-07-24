import cv2
import numpy as np

img = cv2.imread('img/Before.png', -1)
specs = cv2.imread('img/glasses.png', -1)
mustache = cv2.imread('img/mustache.png',-1)

cv2.imshow('Original',img)

## For glasses

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes_cascade = cv2.CascadeClassifier('haarcascades/frontalEyes35x16.xml')
eyes = eyes_cascade.detectMultiScale(gray, 1.3, 5)

i = 0
for (x, y, w, h) in eyes:
    cv2.rectangle(gray, (x, y), (x+w, y+h ), (125, 155, 155), 3)
    i = 1
    break

if i == 0:
    print("not found")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
specs = cv2.resize(specs, (w+90, h+(-40)))

w, h, c = specs.shape

for i in range(0, w):
    for j in range(0, h):

        if specs[i, j][3] != 0:
            img[y + i, x + j] = specs[i, j]

## For mustache

mouth_cascade = cv2.CascadeClassifier('haarcascades/Nose18x15.xml')
mouth = mouth_cascade.detectMultiScale(gray, 1.3, 5)

i = 0
for (x, y, w, h) in mouth:
    cv2.rectangle(gray, (x, y), (x + w, y + h), (125, 255, 125), 3)
    i = 1

if i == 0:
    print("not found")
    exit()

mustache = cv2.resize(mustache,(w+(-20),h+(-20)))
w,h,c = mustache.shape

y+=int(h)
x+=int(w/2)

for i in range(0,w):
    for j in range(0,h):

        if mustache[i,j][3] !=0:
            img[y+i,x+j] = cigar[i,j]



cv2.imshow('output', img)
cv2.imwrite('outputfile.png',img)
cv2.waitKey(0)
