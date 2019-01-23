from src.FallingObject import FallingObject
from random import randint


class ObjectsStateHandler:
    def __init__(self):
        self.FallingObjects = []  # all falling objects in frame
        self.fgbgThreshold = 180

    # it'll update falling objects state
    def update(self, frame, foreground_mask):
        frame_height, frame_width, _ = frame.shape  # get openCV frame
        for falling_object in self.FallingObjects:
            # check if falling object is out of bound (lower side of the frame) or not
            if falling_object.y + falling_object.height + falling_object.speed >= frame_height:
                self.FallingObjects.remove(falling_object)
            else:
                falling_object.update(foreground_mask=foreground_mask, fgbg_threshold=self.fgbgThreshold)

        # draw all objects
        self.draw_objects(frame=frame)
        # add from 0 to 1 new objects in each frame
        for i in range(randint(0, 1)):
            self.__add_object(total_width=frame_width - 100)

        print(self.FallingObjects.__len__())

    # it'll add new objects to the video
    def __add_object(self, total_width):
        # give new object random speed between 4,14 (it could be any other ints)
        speed = randint(4, 14)
        # give it random starting point between 0 and total width
        random_x = randint(0, total_width)
        # build new object with above values and append it to Falling Objects array
        new_object = FallingObject(x=random_x, y=0, speed=speed)
        self.FallingObjects.append(new_object)

    # draw all objects
    def draw_objects(self, frame):
        for falling_object in self.FallingObjects:
            falling_object.draw(frame=frame)
