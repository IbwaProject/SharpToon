import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


def main():

    img = cv2.imread("static/images/input/imageTemp1.jpg") # "static/images/b_iu.jpg"
    save_file = "static/images/b_iu_cartoon.jpg"
    # cv2.imshow("img", img)

    img_copy = img
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("img_gray", img_gray)
    img_blur = cv2.medianBlur(img_gray, 5)
    # cv2.imshow("img_blur", img_blur)
    img_edge = cv2.adaptiveThreshold(img_blur,
                                    255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY,
                                    blockSize=7,
                                    C=3)

    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
    # cv2.imshow("img_edge", img_edge)

    for _ in range(2):
        img_copy = cv2.pyrDown(img_copy)
        for _ in range(5):
            img_copy = cv2.bilateralFilter(img_copy, d=9, sigmaColor=9, sigmaSpace=7)
        img_copy = cv2.resize(img_copy, (img.shape[1], img.shape[0]),
                            interpolation=cv2.INTER_CUBIC)

    img_cartoon = cv2.bitwise_and(img_copy, img_edge)
    cv2.imwrite(save_file, img_cartoon)

    # cv2.imshow("img_copy", img_copy)
    # cv2.imshow("img_cartoon", img_cartoon)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_cartoon

if __name__ == "__main__":
    main()