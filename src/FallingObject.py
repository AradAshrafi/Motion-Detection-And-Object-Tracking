from src.lib.lib import FALLING_OBJECT_IMAGES_PATH
from random import randint
import cv2


class FallingObject:
    def __init__(self, x=250, y=0, speed=5):
        self.x = x  # x location from left
        self.y = y  # y location from top
        self.width = 15
        self.height = 15
        self.speed = speed  # speed of falling down
        # selecting random image between all images
        self.image_path = FALLING_OBJECT_IMAGES_PATH[randint(0, len(FALLING_OBJECT_IMAGES_PATH) - 1)]
        # cv2.circle(frame, (self.x, self.y), 10, [randint(0, 255) for i in range(3)], -1)

    # update object location
    def update(self, foreground_mask, fgbg_threshold):
        if foreground_mask[self.y, self.x] < fgbg_threshold:  # if object hasn't touched foreground update it's location
            self.y += self.speed

    # draw current object in frame
    def draw(self, frame):
        # cv2.circle(frame, (self.x, self.y), 10, [randint(0, 255) for i in range(3)], -1)
        # reading image from path
        image = cv2.imread(self.image_path)
        # resize image (snowflake) to small width*height images
        image = cv2.resize(image, (self.width, self.height))
        for i in range(self.width):
            for j in range(self.height):
                # Handling Image Transparency
                if image[j, i][0] != 255 & image[j, i][1] != 255 & image[j, i][2] != 255:
                    frame[self.y + j, self.x + i] = image[j, i]
