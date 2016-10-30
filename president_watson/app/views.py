from flask import render_template, request
from app import app


POLITICIANS = {"realDonaldTrump": "Donald Trump (@realDonaldTrump)",
               "HiliaryClinton": "Hiliary Clinton (@HiliaryClinton)",
               "BernieSanders": "Bernie Sanders (@BernieSanders)",
               "BarackObama": "Barack Obama (@BarackObama)",
               "tedcruz": "Ted Cruz (@tedcruz)"
               }


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           politicians=POLITICIANS
                           )


@app.route('/results', methods=['GET'])
def results():
    twitter_1 = request.args.get('Politician_1')
    twitter_2 = request.args.get('Politician_2')

    if twitter_1 == twitter_2:
        return render_template('index.html',
                               politicians=POLITICIANS
                               )
    else:
        return render_template('results.html',
                               twitter_1=POLITICIANS[twitter_1],
                               twitter_2=POLITICIANS[twitter_2]
                               )
