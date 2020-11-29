import cv2 as cv
import numpy as np

img0 = cv.imread('photo/left.JPEG')
img_r = cv.imread('photo/right.JPEG')
img_f = cv.imread('photo/front.JPEG')
img_t = cv.imread('photo/top.JPEG')

def main():
    ima = np.zeros([1536,2048,3],np.uint8) #黑
    #cv.imshow("black",ima)
    ima[:,:,0] = np.ones([1536,2048]) * 255 # 蓝色
    #cv.imshow("deepBlue",ima)

#    img0 = cv.cvtColor(img_l, cv.COLOR_BGR2RGB)
#    img0[:,:,0] = np.ones([1536,2048]) * 255

    img = cv.addWeighted(ima, 1, img0, 1, 1)

#    img1 = cv.cvtColor(img_r, cv.COLOR_BGR2RGB)
#    img1[:,:,1] = np.ones([1536,2048]) * 255

#    img2 = cv.cvtColor(img_t, cv.COLOR_BGR2RGB)
#    img2[:,:,2] = np.ones([1536,2048]) * 255

#    img = cv.addWeighted(img0, 1/3, img1, 1/3, 1)
#    img = cv.addWeighted(img, 1, img2, 1/3, 1)


    cv.imshow('left', img0)
    k = cv.waitKey(0)
#    cv.imshow('right', img1)
#    k = cv.waitKey(0)
#    cv.imshow('top', img2)
#    k = cv.waitKey(0)
    cv.imshow('result', img)
    k = cv.waitKey(0)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
