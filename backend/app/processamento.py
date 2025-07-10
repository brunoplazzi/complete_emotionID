import cv2
import mediapipe as mp
from deepface import DeepFace
import numpy as np

class Imagem:
    @staticmethod
    def detectar_face(image_rgb: np.ndarray):
        mp_face_detection = mp.solutions.face_detection
        with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
            results = face_detection.process(image_rgb)

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                ih, iw, _ = image_rgb.shape
                x = max(0, int(bbox.xmin * iw))
                y = max(0, int(bbox.ymin * ih))
                w = int(bbox.width * iw)
                h = int(bbox.height * ih)
                # Previne corte inválido
                if w > 0 and h > 0:
                    return image_rgb[y:y+h, x:x+w]
        return None

    @staticmethod
    def identificar_emocao(face_rgb: np.ndarray):
        resultado = DeepFace.analyze(face_rgb, actions=['emotion'], enforce_detection=False)
        return {
            "emocao_principal": resultado[0]['dominant_emotion'],
            "probabilidades": resultado[0]['emotion']
        }
