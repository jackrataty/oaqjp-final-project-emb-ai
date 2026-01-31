''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask(__name__)

# Define the route for emotion detection
@app.route("/emotionDetector", methods=["GET"])
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion, dominant = emotion_detector(text_to_analyze)
    if dominant == None:
        display_statement = "Invalid text! Please try again!"
        
    else:
        display_statement = "For the given statement, the system response is "
        
        for key, value in emotion.items():
            display_statement += f", {key} : {value}"

        display_statement = display_statement + f". The dominant emotion is {dominant}"

    return  display_statement

#Render the index page
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
