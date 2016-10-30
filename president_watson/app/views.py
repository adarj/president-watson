from flask import render_template, request
from app import app
from .analyze import President, Tweeter


POLITICIANS = {"realDonaldTrump": "Donald Trump",
               "HiliaryClinton": "Hiliary Clinton",
               "BernieSanders": "Bernie Sanders",
               "BarackObama": "Barack Obama",
               "tedcruz": "Ted Cruz",
               "JoeBiden": "Joe Biden",
               "GovPenceIN": "Mike Pence",
               "SylvesterTurner": "Sylvester Turner",
               "GregAbbott_TX": "Greg Abbott"
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
        president = President()
        president.set_API_keys()

        politician_1 = Tweeter('@' + twitter_1)
        flattened_values_1 = president.flatten(president.analyze('@'+twitter_1))
        politician_1.setPersonalityValues(flattened_values_1)

        return render_template('results.html',
                               name_1=POLITICIANS[twitter_1],
                               name_2=POLITICIANS[twitter_2],
                               twitter_1=twitter_1,
                               twitter_2=twitter_2,
                               liberalism=politician_1.liberalism
                               )
