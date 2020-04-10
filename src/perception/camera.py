import cv2

def retrieve_camera(mirror):
    cam = cv2.VideoCapture(0)
    while True:                         
        ret_val, img = cam.read()
        if mirror:                     
            img = cv2.flip(img, 1)     
        else:                         
            pass                        
        cv2.imshow('Drone', img)
        if cv2.waitKey(1) == 27:         
            break                        
        else:                            
            pass                        
    
    cv2.destroyAllWindows()              

def camera(mirror_status):             
    retrieve_webcam(mirror = mirror_status)
    
# exports camera
