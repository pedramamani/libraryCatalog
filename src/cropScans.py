from config import *
import os
import cv2
import numpy as np


def main():
    croppedFiles = os.listdir(croppedPath)

    for fileName in os.listdir(scansPath):
        if fileName in croppedFiles:
            continue

        original = cv2.imread(str(scansPath / fileName), cv2.IMREAD_COLOR)
        img = original.copy()

        for right in range(img.shape[1] - 1, 0, -1):
            if np.mean(img[:, right]) < 252:
                break
        for bottom in range(img.shape[0] - 1, 0, -1):
            if np.mean(img[bottom, :]) < 252:
                break
        
        # draw the bottom and right lines
        cv2.line(img, (0, bottom), (img.shape[1], bottom), (0, 0, 255), 1)
        cv2.line(img, (right, 0), (right, img.shape[0]), (0, 0, 255), 1)
        cv2.imshow('Image', img)

        key = cv2.waitKey()
        if key == ord('q'):
            cv2.destroyAllWindows()
            return
        elif key == ord('y'):
            original = original[0: bottom, 0: right]
            cv2.imwrite(str(croppedPath / fileName), original)
        elif key == ord('n'):
            print(fileName)
            continue


if __name__ == '__main__':
    main()
