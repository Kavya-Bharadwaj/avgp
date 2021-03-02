from Control.Motors_control import forward,backward,setServoAngle,stop,turnOfCar,changePwm,beInLane
import config
import cv2
def Steer(Distance,Curvature,frame):
    
    if config.Testing:
        if(Distance != -1000 | Curvature != -1000):
            if (config.debugging==False):		
                angle_of_car , current_speed = beInLane(int(frame.shape[1]/4), Distance,Curvature )
                angle_speed_str = "[ Angle ,Speed ] = [ " + str(angle_of_car) + " , " + str(current_speed) + " ] "
                #cv2.putText(frame_disp,str(angle_of_car),(frame.shape[1]-400,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),2)
                cv2.putText(frame,str(angle_speed_str),(100,30),cv2.FONT_HERSHEY_DUPLEX,0.6,(0,0,255),2)

    else:
        if(Distance != -1000 | Curvature != -1000):
            if (config.debugging==False):
                beInLane(int(frame.shape[1]/4), Distance,Curvature )       

def Drive_Car(Current_State):
    [distance, Curvature, frame_disp] = Current_State
    Steer(distance,Curvature,frame_disp)

