import cv2

img_path = cv2.imread('mediapipe\Ham.png' , cv2.IMREAD_UNCHANGED)
img_path2 = cv2.imread('mediapipe\Snow.png' , cv2.IMREAD_UNCHANGED)

print('awdasdw :',img_path.shape)

width = 500
height = 500
dim = (width, height)
dim1 = (width, height)

resize = cv2.resize(img_path, dim, interpolation = cv2.INTER_AREA)
resize1 = cv2.resize(img_path2, dim1, interpolation = cv2.INTER_AREA)

cv2.imshow('Ham',resize)
cv2.imshow('snow',resize1)

cv2.waitKey(0)
cv2.destroyAllWindows()
