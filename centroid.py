import cv2


def bimg(img):
    '''
    need the binary video for contour length calculation here the image is already gray which is mask
    :param img: image is masked  hsv image in this case(which is already gray)
    :return: the binary of it
    '''
    _, maskbin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return maskbin

def xlen(a):
    '''
    :param a: it is the masked image for the specific color (in this case mask)
    :return: the weighted x length of all the contours
    '''

    _, contours, _ = cv2.findContours(bimg(a), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    cx = 0
    totalarea=0
    while (i<len(contours)-1):
        area=cv2.contourArea(contours[i])       #selecting the ith contour
        M=cv2.moments(contours[i])
        totalarea=totalarea+area

        if(area!=0):
            ''' here x is the respective weighted X cordinate of the contour '''
            x=area*(int(M['m10']/M['m00']))
            cx=cx+x
            i=i+1
        else:
            i=i+1

    if(totalarea!=0):
        return cx/totalarea
    else:
        return 0

def ylen(a):
    '''

    :param a:  it is the masked image for the specific color (in this case mask)
    :return: the weighted x length of all the contours
    '''
    
    #thinking of checking number of returns done by findContours method().
    contours, _ = cv2.findContours(bimg(a), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    cy = 0
    totalarea=0
    while (i < len(contours) - 1):
        area = cv2.contourArea(contours[i])  # selecting the ith contour
        M = cv2.moments(contours[i])
        totalarea=totalarea+area
        if(area!=0):
            ''' here x is the respective weighted Y cordinate of the contour '''
            y = area * (int(M['m01'] / M['m00']))
            cy = cy + y
            i = i + 1
        else:
            i=i+1

    if(totalarea!=0):
        return cy/totalarea
    else:
        return 0
