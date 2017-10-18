import cv2
import numpy as np

capture = cv2.VideoCapture(0)

tm = 100
w  = 640.0

last = 0
while True:
    ret, image = capture.read()

    img_height, img_width, depth = image.shape
    scale = w / img_width
    h = img_height * scale
    image = cv2.resize(image, (0,0), fx=scale, fy=scale)

    # Apply filters
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blured = cv2.medianBlur(grey, 5)

    sc = 1
    md = 30
    at = 40
    circles = cv2.HoughCircles(blured, cv2.HOUGH_GRADIENT, sc, md, tm, at)

    if circles is not None:
        # We care only about the first circle found.
        circle = circles[0][0]
        x, y, radius = int(circle[0]), int(circle[1]), int(circle[2])
        print((x / w, y / h, radius / w))

        # Highlight the circle
        cv2.circle(image, (x, y), radius, (0, 255, 0), 3)
        # Draw dot in the center
        cv2.circle(image, (x, y), 1, (0, 255, 0), 3)

    cv2.imshow('Image with detected circle', image)

    if cv2.waitKey(1) & 0xFF == 32:
        break
