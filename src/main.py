from src.ObjectsStateHandler import ObjectsStateHandler
from src.lib.lib import INPUT_VIDEO_LOC
from src.lib.lib import SAVING_OUTPUT_VIDEO_LOC
import cv2


# get video mode from user
# if 1 is web cam
# if 2 is offline location
def __get_video_mode():
    user_selected_mode = int(input("select your mode :\n1 - webcam\n2 - dataset video\n"))
    return user_selected_mode


# create video writer to write whole process with it
def __create_video_writer():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # we know that the frame size width is 640 and height is 480
    # ------important reminder------- if frame size changed,note that you must change 640,480 in following sentence too
    return cv2.VideoWriter(SAVING_OUTPUT_VIDEO_LOC, fourcc, 20.0, (640, 480))


def main():
    # determine user desired mode
    user_selected_mode = __get_video_mode()

    # this piece of code is for one bug in openCV that i don't know what is it acutaly:D
    cv2.ocl.setUseOpenCL(False)

    # initiate falling objects state handler
    state = ObjectsStateHandler()
    # capture web cam or video photo video
    if user_selected_mode == 1:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(INPUT_VIDEO_LOC)

    # get video writer in 640*480 size (matches frame size)
    video_writer = __create_video_writer()

    # foreground background separator
    fgbg = cv2.createBackgroundSubtractorKNN(history=1000)
    # in web cam mode it will loop until user get tired :D
    # in offline mode it will loop until video finished
    while True:
        # read current frame
        ret, frame = cap.read()
        if not ret:
            break
        # apply foreground background subtraction
        fg_mask = fgbg.apply(frame)
        # update frame state with falling objects using foreground mask
        state.update(frame=frame, foreground_mask=fg_mask)

        cv2.imshow("snowish :D", frame)  # show image with snowflakes effect on i :D
        video_writer.write(frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
