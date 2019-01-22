from lib import TEST_CASE_LOC
from ObjectsStateHandler import ObjectsStateHandler

# import cv2
#
# cap = cv2.VideoCapture(0)
# fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=7)
# cv2.ocl.setUseOpenCL(False)
#
# while 1:
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     cv2.imshow('frame', fgmask)
#     print(frame)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()


if __name__ == '__main__':
    state = ObjectsStateHandler()
