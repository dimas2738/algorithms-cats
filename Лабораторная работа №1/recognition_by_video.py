import cv2
import collections as col

all_list=[]
compressed_list=[]
# Load the cascade
face_cascade = cv2.CascadeClassifier('recognizer/recognition_by_photo_with OpenCV/HaarCascade/haarcascade_frontalface_default.xml')

# To use a video file as input
cap = cv2.VideoCapture('recognizer/detect_video/input/test.mp4')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('recognizer/recognition_by_photo_with OpenCV/trainingData.yml')
name = {0 : "yrii",1 : "anton"}

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
def draw_rect(img,face):
    (x,y,w,h)=face
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=5)


while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle and text(name) around each face

    for face in faces:

        (x, y, w, h) = face
        roi_gray = gray[y:y + w, x:x + h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("confidence:",confidence)
        print("label:",name[label])
        draw_rect(img,face)
        predicted_name=name[label]
        # if confidence < 37:#If confidence less than 37 then don't print predicted face text on screen
        draw_text(img,predicted_name,x,y)
        all_list.append(predicted_name)



    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()


#log and count
for i in range(0, len(all_list) - 1):
    if all_list[i] != all_list[i + 1]:
        compressed_list.append(all_list[i])
    else:
        continue

f = open("log.txt", "w")
f.write("кто появляется в кадре, последовательно(по кадрам) "+str(compressed_list)+ '\n')
counter=col.Counter(compressed_list)
f.write("кто сколько раз появляется в кадре "+str(counter))
f.close()