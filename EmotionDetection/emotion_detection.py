

import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # Mock API endpoint
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
                             
    if response.status_code == 200:
        data = response.json() 
        emotions = data["emotionPredictions"][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
                
    if response.status_code == 400:
        dominant_emotion = None
        emotions = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
            }
        
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions, dominant_emotion
     