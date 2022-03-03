from distutils.log import debug
from flask import Flask, render_template
from twitterbot import reply_tweets
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__, template_folder="templates")


@app.route("/<string:name>")
def wordcloud_page(name):
    return render_template("display_image.html", image_name=name)


def reply():
    print("hi")
    reply_tweets()


scheduler = BackgroundScheduler()
scheduler.add_job(func=reply, trigger="interval", seconds=300)
scheduler.start()


if __name__ == "__main__":
    app.run(debug=False)
