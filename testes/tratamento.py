#import cv2
##Read Image
#img = cv2.imread('imagem/10 mg cubiu - 5h.jpg')
##Display Image
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
##Applying Grayscale filter to image
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
##Saving filtered image to new file
#cv2.imwrite('imagem/10 mg cubiu - 5h.jpg',gray)



# import numpy as np
# import cv2
# 
# img = cv2.imread('imagem/10 mg cubiu - 5h.jpg',0)
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:
#     # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'):
# # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()



import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()