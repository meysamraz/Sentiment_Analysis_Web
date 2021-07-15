from flask import Flask , render_template  ,request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def main():
    if request.method == "POST":
        inp = request.form.get('inp')
        sid = SentimentIntensityAnalyzer()
        socre = sid.polarity_scores(inp)
        if socre['neg'] != 0:
            return render_template('home.html',message="Negative🙁🙁")
        else:
            return render_template('home.html',message="Positive🙂🙂")   
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)