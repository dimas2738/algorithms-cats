Что сделано:
- определение лиц с фото и с видео;
- сопоставление лиц с именами- подпись лиц;
- обучено 2 лица на основе тренировочного датасета.

Как правильно пользоваться файлами.py:

training_yml_Data.py
	recognizer/recognition_by_photo_with OpenCV/trainingImages- тренируем модель на 		отсортированных фото 0 или 1
	recognizer/recognition_by_photo_with OpenCV/trainingData.yml- записываем в 			файл.yml

detect_by_photo.py:
	в папке /detect_by_photo/input - кладем фото с людей
		на выход получаем вырезанные лица из фотографий людей по папкам
	/detect_by_photo.py/output/selected or rejected

detect_by_video.py:
	в папке /detect_video/input - кладем видео мр4
		на выход получаем вырезанные лица людей из видео по папкам
	/detect_video/output/faces/selected or rejected
		и /detect_video/output/frames c кадрами из видео
	

recognition_by_photo.py:
	в папке /recognition_by_photo/faces - кладем фото подписанных лиц 
	/recognition_by_photo/- кладем фото на котором хотим определить лицо
		 из числа тех, что лежит в папке /faces
	на выходе фото с обрамленным и подписанным лицом


recog_by_ph_with OpenCV.py:
	в папке recognizer/recognition_by_photo_with OpenCV/HaarCascade - модель 
		распознавания лиц OpenCV
	recognizer/recognition_by_photo_with OpenCV/TestImages- кладем фото
		 на котором хотим определить лицо из числа тех, что лежит в папке
		 /trainingImages
	recognizer/recognition_by_photo_with OpenCV/trainingImages/0 or 1 фотографии 	
		принадлежащие 0 или 1 человеку
	recognizer/recognition_by_photo_with OpenCV/trainingData.yml- натренированная на 
		trainingImages модель распознавания лиц 0 или 1
	на выходе фото с обрамленным лицом и подписью лица выведенного в консоль

recognition_by_video.py:
	в папке recognizer/recognition_by_photo_with OpenCV/HaarCascade/
		haarcascade_frontalface_default.xml - модель распознавания лиц OpenCV
	recognizer/detect_video/input/test.mp4- кладем видео
		 на котором хотим определить лицо 	
	recognizer/recognition_by_photo_with OpenCV/trainingData.yml- натренированная на 
		trainingImages модель распознавания лиц 0 или 1
	log.txt
		+ кто появляется в кадре, последовательно(по кадрам)( ['anton', 'yrii'])
		+ кто сколько раз появляется в кадре ( Counter({'anton': 1, 'yrii': 1}))
	на выходе видео с обрамленным лицом и подписью лица + файл log.txt

Недостатки: 
	recognition_by_video.py- определяет шумы как лицо, плодит ошибки распознавания
	ecog_by_ph_with OpenCV.py- не подписывает имя на фото- решил выводом в консоль
		 через print

	