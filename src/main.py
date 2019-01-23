from src.ObjectsStateHandler import ObjectsStateHandler
import cv2


def main():
    cv2.ocl.setUseOpenCL(False)

    # initiate falling objects state handler
    state = ObjectsStateHandler()
    # capture webcam or video photo video
    cap = cv2.VideoCapture(0)
    # foreground background separator
    fgbg = cv2.createBackgroundSubtractorKNN(history=1000)

    # in web cam mode it will loop until user get tired :D
    # in offline mode it will loop until video finished
    while True:
        # read current frame
        _, frame = cap.read()
        # apply foreground background subtraction
        fg_mask = fgbg.apply(frame)
        # update frame state with falling objects using foreground mask
        state.update(frame=frame, foreground_mask=fg_mask)

        cv2.imshow("snowish :D", frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
