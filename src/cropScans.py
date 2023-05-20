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
        temp = cv2.resize(original, (0, 0), fx=0.5, fy=0.5)
        background = np.average(temp[-10:, :], axis=(0, 1))
        temp = np.abs(temp - background).clip(0, 255).astype(np.uint8)

        for right in range(temp.shape[1] - 1, 0, -1):
            if np.std(temp[:, right]) > 50 or np.mean(temp[:, right]) > 30:
                break
        for bottom in range(temp.shape[0] - 1, 0, -1):
            if np.std(temp[bottom, :]) > 50 or np.mean(temp[bottom, :]) > 30:
                break
        
        temp = original[0: int(bottom * 2), 0: int(right * 2)]
        cv2.imwrite(str(croppedPath / fileName), temp)


if __name__ == '__main__':
    main()
