import functions_for_faceRecognition as fr

faces,faceID=fr.labels_for_training_data('recognizer/recognition_by_photo_with OpenCV/trainingImages')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.write('recognizer/recognition_by_photo_with OpenCV/trainingData.yml')