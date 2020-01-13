from flask import Flask, render_template, request

from textblob import TextBlob
global result
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def sentiment_analyzer_front_end ():
    if request.method == 'GET':
        return render_template('sentiment_analyzer_ front_end.html')
            
    
    if request.method =="POST":
        text = request.form["text"]
        processed_text = text.lower()
        sent = TextBlob(processed_text)
        result = sent.sentiment.polarity
        
        if result > 0.0 :
            return render_template('sentiment_analyzer_ front_end.html',result = "positive")
        elif result <0.0:
            return render_template('sentiment_analyzer_ front_end.html',result = "negative")
        elif result == 0.0:
            return render_template('sentiment_analyzer_ front_end.html',result = "neutral")
            
            
@app.route("/offline.html")
def offline():
    return app.send_static_file('offline.html')


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')    


 

if __name__ == '__main__':
   app.run(debug = False)