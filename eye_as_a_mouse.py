import cv2
import mediapipe as mp
import pyautogui as pg

face_mesh_landmarks = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)        
cap = cv2.VideoCapture(0)
screen_width , screen_height = pg.size()


while True:
    ret , image = cap.read()
    image = cv2.flip(image ,1)
    if not ret:
        continue
    window_h , window_w , _ = image.shape
    rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    processed_image = face_mesh_landmarks.process(rgb_image)
    all_face_landmark_points = processed_image.multi_face_landmarks
    
    if all_face_landmark_points:
        one_face_landmark_points = all_face_landmark_points[0].landmark
        
        for id ,landmark_points in enumerate(one_face_landmark_points[474:478]):
            x = int(landmark_points.x * window_w)
            y = int(landmark_points.y * window_h)
            if id == 1:
                mouse_x = int(screen_width / window_w * x)
                mouse_y = int(screen_height / window_h * y)
                
                pg.moveTo(mouse_x , mouse_y)
                cv2.circle(image , (x,y) , 3 , (0,0, 255))
        left_eye =[one_face_landmark_points[145], one_face_landmark_points[159]]
        for landmark_point in left_eye:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
                    
            cv2.circle(image , (x,y) , 3 , (0,255,255))
        if(left_eye[0].y-left_eye[1].y<0.007):
            pg.click()
            pg.sleep(2)
            print("Mouse clicked")
                        
    cv2.imshow("Mouse controller with eyes", image)
    key = cv2.waitKey(10)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()