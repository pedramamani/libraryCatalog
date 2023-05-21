from config import *
import os
import cv2
import numpy as np


state = {}

def updateDisplay():
    image = state.get('image').copy()
    x, y = state.get('corner')
    cv2.line(image, (0, y), (image.shape[1], y), (0, 0, 255), 1)
    cv2.line(image, (x, 0), (x, image.shape[0]), (0, 0, 255), 1)
    cv2.imshow('Image', image)


def mouseListener(event, x, y, *_):
    if event == cv2.EVENT_LBUTTONDOWN:
        state['corner'] = (x, y)
        state['track'] = True
        updateDisplay()
    elif event == cv2.EVENT_MOUSEMOVE and state.get('track', False):
        state['corner'] = (x, y)
        updateDisplay()
    elif event == cv2.EVENT_LBUTTONUP:
        state['track'] = False


def detectCorner():
    image = state.get('image')
    for x in range(image.shape[1] - 1, 0, -1):
        if np.mean(image[:, x]) < 250:
            break
    for y in range(image.shape[0] - 1, 0, -1):
        if np.mean(image[y, :]) < 250:
            break
    state['corner'] = (x, y)


def main():
    names = os.listdir(coverPath)
    genres = os.listdir(scanPath)

    for genre in genres:
        genrePath = scanPath / genre
        for fileName in os.listdir(genrePath):
            if fileName in names:
                continue

            original = cv2.imread(str(genrePath / fileName))
            state['image'] = original.copy()
            detectCorner()
            updateDisplay()
            cv2.setMouseCallback('Image', mouseListener)

            key = cv2.waitKey()
            if key == ord('q'):
                return
            elif key == ord('y'):
                x, y = state.get('corner')
                original = original[0: y, 0: x]
                cv2.imwrite(str(coverPath / fileName), original)
            elif key == ord('n'):
                continue


if __name__ == '__main__':
    main()
