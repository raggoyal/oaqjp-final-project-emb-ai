"""Import needed modules"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

"""emotion detector function URL"""
@app.route("/emotionDetector")
def sent_detector():
    """emotion detector function URL"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    data = emotion_detector(text_to_analyze)

    error = data["anger"]

    if error == "None":
        response = 'Invalid text! Please try again!.'
    else:
        response = data
    return response

@app.route("/")
def render_index_page():
    """Render base homegame"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
