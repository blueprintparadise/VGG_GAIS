import DeepFace

IMAGE_PATH = r"C:\Users\rhira\Documents\Face_Recognition_GAIS\Face_Recog\images"

DeepFace.stream(source=0, db_path= IMAGE_PATH,model_name="VGG-Face", detector_backend="mediapipe",enable_face_analysis=False)
