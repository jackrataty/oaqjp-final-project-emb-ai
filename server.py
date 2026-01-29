''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : 
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    return f"For the given statement, th esystem response is  as {result['dominant_emotion']} with a score of {result['score']}" 
    
    

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
