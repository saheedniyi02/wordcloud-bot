from distutils.log import debug
from flask import Flask, render_template, send_file
from twitterbot import reply_tweets
from apscheduler.schedulers.background import BackgroundScheduler
import time

app = Flask(__name__, template_folder="templates")


@app.route("/<int:tweet_id>")
def wordcloud_page(tweet_id):
    return render_template("image.html", image_name=tweet_id)


@app.route("/download/<int:tweet_id>")
def download(tweet_id):
    return send_file(f"static/{tweet_id}.jpg", as_attachment=True)


def reply():
    reply_tweets()


scheduler = BackgroundScheduler()
scheduler.add_job(func=reply, trigger="interval", seconds=60 * 7)
scheduler.start()


if __name__ == "__main__":
    app.run(debug=False)
