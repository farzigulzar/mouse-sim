import numpy as np
'''Imoport the Image and flip it on columns
here a is the image matrix'''

def flip(a):
    '''
    :param a: it is the image matrix
    :return:  the flip matrix
    '''
    temp=np.zeros(a.shape,np.uint8)
    r,c,ch=a.shape
    i=0
    '''the c are the number of columns in a '''
    while i<c-1:
        i=i+1
        temp[:, i, :] = a[:, c-i, :]
    return temp