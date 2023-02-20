import cv2
import array as arr
import numpy as np


def mask(entity_, mask_):

    ret0_=np.zeros((entity_.shape[0], entity_.shape[1]), np.uint8)
    
    for x in range(entity_.shape[0]):
        for y in range(entity_.shape[1]):
            ret0_[x,y]= np.bitwise_and(mask_, entity_[x,y].astype(int));
       

    return ret0_

def combine(support_, message_):

    ret_=np.zeros((support_.shape[0], support_.shape[1]), np.uint8)
    
    
    for x in range(support_.shape[0]):
        for y in range(support_.shape[1]):
            ret_[x,y]= np.bitwise_or(support_[x,y].astype(int),
                                      message_[x,y].astype(int))

    return ret_

def extract(support2_, mask__):

    ret2_=np.zeros((support2_.shape[0], support2_.shape[1]), np.uint8)
    

    for x in range(support2_.shape[0]):
        for y in range(support2_.shape[1]):
            ret2_[x,y]= np.left_shift(
                np.bitwise_and(mask__,support2_[x,y].astype(int)),5)
        
            
    
    return ret2_

    
mask1=248
mask2=7
mask__=7
img = cv2.imread('vector1.jpg')
message = cv2.imread('Image.jpg')

image_result= cv2.merge((combine(mask(img[:,:,0],mask1), mask(message[:,:,0],mask2)),
                         combine(mask(img[:,:,1],mask1), mask(message[:,:,1],mask2)),
                         combine(mask(img[:,:,2],mask1), mask(message[:,:,2],mask2))))

extracted= cv2.merge((extract(image_result[:,:,0],mask__),
                              extract(image_result[:,:,1],mask__),
                                      extract(image_result[:,:,2],mask__)))

horizontal_disp= np.concatenate((image_result, extracted), axis=1)
cv2.imshow('Image / Message', horizontal_disp)

cv2.waitKey(0)

cv2.destroyAllWindows()

 

