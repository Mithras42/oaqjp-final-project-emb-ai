from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

# Initiate the flask app
app = Flask(__name__)


@app.route("/emotionDetector")
def emotionDetector():
    """This code receives the text from the HTML interface and
    runs emotion analysis over it using emotion_detection()
    function. The output returns the emotion scores and the
    dominant emotion
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detection(text_to_analyze)

    # Extracting emotions and dominant emotion from response
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # Formatting the output string
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    """ This functions executes the flask app and deploys it on localhost:5000
    """
    app.run(debug=True)
