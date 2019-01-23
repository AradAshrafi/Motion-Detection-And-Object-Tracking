from src.lib.lib import SNOWFLAKE_IMAGE_PATH
import cv2


class FallingObject:
    def __init__(self, x=250, y=0, speed=5, image_path=SNOWFLAKE_IMAGE_PATH):
        self.x = x
        self.y = y
        self.speed = speed
        self.image_path = image_path

        # update object location

    def update(self, frame, foreground_mask, fgbg_threshold):
        if foreground_mask[self.y, self.x] < fgbg_threshold:
            self.y += self.speed

        self.__draw(frame)

    def __draw(self, frame):
        # cv2.circle(frame, (self.x, self.y), 10, (255, 255, 255), -1)
        # reading image from path
        image = cv2.imread(self.image_path)
        # resize image (snowflake) to small width*height images
        width = 25
        height = 25
        image = cv2.resize(image, (width, height))
        for i in range(width):
            for j in range(height):
                frame[self.y + j, self.x + i] = image[j, i]

        # i don't understand why i should do followings,and instead i wrote code above ----> :-?
        # rows, cols, channels = image.shape
        # roi = frame[self.y:self.y + height, self.x:self.x + width]
        # ret, mask = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)
        # mask_inv = cv2.bitwise_not(mask)
        #
        # # Now black-out the area of logo in ROI
        # frame_change = cv2.bitwise_and(roi, roi, mask=mask_inv)
        #
        # # Take only region of logo from logo image.
        # obj_fg = cv2.bitwise_and(image, image, mask=mask)
        #
        # # Put logo in ROI and modify the main image
        # dst = cv2.add(frame_change, obj_fg)
        # frame[roi[0], roi[1]] = dst
