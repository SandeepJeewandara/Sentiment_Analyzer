from flask import Flask,render_template,request, redirect

app = Flask(__name__)

# logging.info('Flask server started')

data = dict()
reviews = ["I like this place",'Love this location','bad vibe.not suitable']
positive = 5
negative = 2


@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    # logging.info('========== Open home page ============')

    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()