from src.ObjectsStateHandler import ObjectsStateHandler
import cv2

if __name__ == '__main__':
    # initiate falling objects state handler
    state = ObjectsStateHandler()
    cv2.ocl.setUseOpenCL(False)

    # capture webcam video
    cap = cv2.VideoCapture(0)

    # foreground background separator
    fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=5)

    # here frame width is 480
    # and frame height is 640
    frame_width = 480
    frame_height = 640

    while True:
        # read current frame
        _, frame = cap.read()
        # apply foreground background subtraction
        fg_mask = fgbg.apply(frame)

        state.update(frame=frame)

        cv2.imshow('frame', frame)
        print(frame.shape)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
