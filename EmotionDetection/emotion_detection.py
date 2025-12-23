import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detection that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion_detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header) 

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        max_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = max_emotion
    else:
	    emotions =  {'anger':'None'}
    
    return emotions