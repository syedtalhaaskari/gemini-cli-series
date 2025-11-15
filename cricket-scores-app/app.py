from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    feed = feedparser.parse('https://static.cricinfo.com/rss/livescores.xml')
    return render_template('index.html', entries=feed.entries)

if __name__ == '__main__':
    app.run(debug=True)
