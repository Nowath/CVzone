import cv2

image = 'mediapipe\Snow.png'

img = cv2.imread(image,cv2.IMREAD_UNCHANGED)

print('sdrgr :',img.shape)

x,y,w,h = 125,125,200,225
color = (0,0,0)

width = 500
height = 500
dim = (width,height)

text = 'Hello SnowMan!'
font = cv2.FONT_HERSHEY_SIMPLEX
color_font = (172,114,250)
font_sacle = 1

resize = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

cv2.rectangle(resize,(x,y),(x+w,y+h),color,thickness = 2)
cv2.putText(resize,text,(105,123),font,font_sacle,color_font,thickness = 2)
cv2.imshow('Snow',resize)

cv2.waitKey(0)
cv2.destroyAllWindows()