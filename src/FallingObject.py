from src.lib.lib import SNOWFLAKE_IMAGE_PATH
import cv2


class FallingObject:
    def __init__(self, x=250, y=0, speed=5, image_path=SNOWFLAKE_IMAGE_PATH):
        self.x = x
        self.y = y
        self.speed = speed
        self.image_path = image_path

        # update object location

    def update(self, frame):
        self.y += self.speed
        self.__draw(frame)

    def __draw(self, frame):
        cv2.circle(frame, (self.x, self.y), 10, (255, 255, 255), -1)
