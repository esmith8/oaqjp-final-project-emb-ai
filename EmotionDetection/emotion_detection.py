import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response = json.loads(response.text)
    emotion_list = formatted_response['emotionPredictions']
    emotion_dict = emotion_list[0]
    emotions = emotion_dict['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    max_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
    if anger_score == max_score:
        dominant_emotion = 'anger'
    elif disgust_score == max_score:
        dominant_emotion = 'disgust'
    elif fear_score == max_score:
        dominant_emotion = 'fear'
    elif joy_score == max_score:
        dominant_emotion = 'joy'
    elif sadness_score == max_score:
        dominant_emotion = 'sadness'
    emotions['dominant_emotion'] = dominant_emotion
    return emotions