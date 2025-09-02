from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

# Download NLTK data (only first run)
nltk.download("vader_lexicon")

# Flask setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sentiments.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Database model
class Sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float, nullable=False)

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        analyzer = SentimentIntensityAnalyzer()
        score = analyzer.polarity_scores(text)["compound"]

        if score >= 0.05:
            sentiment = "Positive"
        elif score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Save to DB
        result = Sentiment(text=text, sentiment=sentiment, score=score)
        db.session.add(result)
        db.session.commit()

        return redirect(url_for("index"))

    # Show all results
    results = Sentiment.query.order_by(Sentiment.id.desc()).all()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create database if not exists
    app.run(debug=True, port=5002)
