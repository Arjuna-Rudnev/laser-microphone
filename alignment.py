#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()): 
    summ = 0
    ret, frame = cap.read()
    if ret: 
        height, width = frame.shape[:2]
        cv2.rectangle(frame, (width//2 -32, height//2 + 32), (width//2 +32, height//2 - 32), (0, 255, 255), 10)
        cv2.imshow("webcam",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break  
    else:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




