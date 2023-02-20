import cv2
import numpy as np

def merge_code(entity_, message_):

    ret_=np.zeros((entity_.shape[0], entity_.shape[1]), np.uint8)
    index= 0;
    
    for x in range(entity_.shape[0]):
        for y in range(entity_.shape[1]):
            if index>=len(message_):
                ret_[x,y]= entity_[x,y]
            else:
               ret_[x,y]= int(ord(message_[index]))
               index+=1

    return ret_
        


def extract_code(entity_,message_):


    index= 0;
    
    for x in range(entity_.shape[0]):
        for y in range(entity_.shape[1]):
            if index>=len(message_):
                break
            else:
                print(chr(entity_[x,y]));
                index+=1

    

img = cv2.imread('vector1.jpg')
message= "message"

coded_image_component= merge_code(img[:,:,0], message)

reconstructed= cv2.merge((coded_image_component,img[:,:,1],img[:,:,2]))

extract_code(reconstructed[:,:,0],message)

cv2.imshow('', reconstructed)

