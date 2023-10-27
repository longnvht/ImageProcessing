import cv2

#print(cv2.__version__)

img = cv2.imread('avatar.jpg')

(h, w, d) = img.shape

print("width={}, height={}, depth={}".format(w, h, d))

# Độ rộng và chiều cao mới của hình ảnh

new_width = 400
new_height = 600

# Thay đổi kích thước hình ảnh

resized_img = cv2.resize(img, (new_width, new_height))

cv2.imshow('Display Image', resized_img)


# Tọa độ góc trái trên và dưới phải của vùng bạn muốn cắt
x1, y1 = 120, 50  # Điểm trên cùng bên trái
x2, y2 = 300, 200  # Điểm dưới cùng bên phải


# Cắt hình ảnh để lấy vùng bạn quan tâm
cropped_img = resized_img[y1:y2, x1:x2]

cv2.imshow('Region Of Interest', cropped_img)

cv2.waitKey(0)


