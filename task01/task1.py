import cv2
import numpy as np
import matplotlib

cap = cv2.imread("Task01.jpg")


def  My_Edge_Filter(Original_Image, SIGMA):

    kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1],])# guassian kernel

    grey_img = cv2.filter2D(Original_Image,-1,kernel) #smoothning of img

    
    
    sobel_Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    
    # detemination of gradient in X and gradient in Y
    Dx = cv2.filter2D(grey_img,-1,sobel_Kx)
    Dy = cv2.filter2D(grey_img,-1,sobel_Ky)

   

    inte = np.sqrt(np.square(Dx) + np.square(Dy))
 
    inte *= 255.0 / inte.max()

    edge = cv2.addWeighted(Dx,0.5,Dy,0.5,0)

  
    # oreantation determination
    oreantation = np.arctan2(Dy, Dx)

    cv2.imshow("Dx",Dx ) 
    cv2.imshow("Dy",Dy ) 
    cv2.imshow("edge",edge )   
    
   
    
    cv2.waitKey(0)

   
    
    return (edge,inte,oreantation)



edge ,e_int, orr = My_Edge_Filter(cap,3)





