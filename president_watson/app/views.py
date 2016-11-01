from flask import render_template, request
from app import app
from .analyze import Politician, Tweeter


POLITICIANS = {"realDonaldTrump": "Donald Trump",
               "HillaryClinton": "Hillary Clinton",
               "BernieSanders": "Bernie Sanders",
               "BarackObama": "Barack Obama",
               "tedcruz": "Ted Cruz",
               "JoeBiden": "Joe Biden",
               "GovPenceIN": "Mike Pence",
               "SylvesterTurner": "Sylvester Turner",
               "GregAbbott_TX": "Greg Abbott",
               "SarahPalinUSA": "Sarah Palin",
               "GovGaryJohnson": "Gary Johnson",
               "DrJillStein": "Jill Stein"
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
        politician = Politician()
        politician.set_API_keys()

        name_1 = POLITICIANS[twitter_1]
        name_2 = POLITICIANS[twitter_2]

        politician_1 = Tweeter('@' + twitter_1)
        politician_1.set_personality_values(politician.flatten(politician.analyze(politician_1.handle)))
        image_1_url = politician.get_(politician_1.handle)

        modesty_1 = politician_1.modesty
        liberalism_1 = politician_1.liberalism
        anger_1 = politician_1.anger
        intellect_1 = politician_1.intellect
        morality_1 = politician_1.morality

        politician_2 = Tweeter('@' + twitter_2)
        politician_2.setPersonalityValues(politician.flatten(politician.analyze(politician_2.handle)))
        image_2_url = politician.get_profile_picture(politician_2.handle)

        modesty_2 = politician_2.modesty
        liberalism_2 = politician_2.liberalism
        anger_2 = politician_2.anger
        intellect_2 = politician_2.intellect
        morality_2 = politician_2.morality

        modesty_value = 100 * abs(modesty_1 - modesty_2)
        if modesty_value < 0.1:
            modesty_str = "{} and {} have an equal amount of modesty.".format(name_1, name_2)
        elif modesty_1 > modesty_2:
            modesty_str = "{} is {:.1f}% more modest than {}.".format(name_1, modesty_value, name_2)
        elif modesty_1 < modesty_2:
            modesty_str = "{} is {:.1f}% more modest than {}.".format(name_2, modesty_value, name_1)
        else:
            modesty_str = "{} and {} have an equal amount of modesty.".format(name_1, name_2)

        liberalism_value = 100 * abs(liberalism_1 - liberalism_2)
        if liberalism_value < 0.1:
            liberalism_str = "{} and {} have an equal amount of liberalism.".format(name_1, name_2)
        elif liberalism_1 > liberalism_2:
            liberalism_str = "{} is {:.1f}% more liberal than {}.".format(name_1, liberalism_value, name_2)
        elif liberalism_1 < liberalism_2:
            liberalism_str = "{} is {:.1f}% more liberal than {}.".format(name_2, liberalism_value, name_1)
        else:
            liberalism_str = "{} and {} have an equal amount of liberalism.".format(name_1, name_2)

        anger_value = 100 * abs(anger_1 - anger_2)
        if anger_value < 0.1:
            anger_str = "{} and {} have an equal amount of anger.".format(name_1, name_2)
        elif anger_1 > anger_2:
            anger_str = "{} is {:.1f}% more angry than {}.".format(name_1, anger_value, name_2)
        elif anger_1 < anger_2:
            anger_str = "{} is {:.1f}% more angry than {}.".format(name_2, anger_value, name_1)
        else:
            anger_str = "{} and {} have an equal amount of anger.".format(name_1, name_2)

        intellect_value = 100 * abs(intellect_1 - intellect_2)
        if intellect_value < 0.1:
            intellect_str = "{} and {} are both equally intellectual.".format(name_1, name_2)
        elif intellect_1 > intellect_2:
            intellect_str = "{} is {:.1f}% more intellectual than {}.".format(name_1, intellect_value, name_2)
        elif intellect_1 < intellect_2:
            intellect_str = "{} is {:.1f}% more intellectual than {}.".format(name_2, intellect_value, name_1)
        else:
            intellect_str = "{} and {} are both equally intellectual.".format(name_1, name_2)

        morality_value = 100 * abs(morality_1 - morality_2)
        if morality_value < 0.1:
            morality_str = "{} and {} are both equally moral.".format(name_1, name_2)
        elif morality_1 > morality_2:
            morality_str = "{} is {:.1f}% more moral than {}.".format(name_1, morality_value, name_2)
        elif morality_1 < morality_2:
            morality_str = "{} is {:.1f}% more moral than {}.".format(name_2, morality_value, name_1)
        else:
            morality_str = "{} and {} are both equally moral.".format(name_1, name_2)

        return render_template('results.html',
                               name_1_=name_1,
                               name_2_=name_2,
                               twitter_1_=twitter_1,
                               twitter_2_=twitter_2,
                               image_1=image_1_url,
                               image_2=image_2_url,
                               modesty_str_=modesty_str,
                               liberalism_str_=liberalism_str,
                               anger_str_=anger_str,
                               intellect_str_=intellect_str,
                               morality_str_=morality_str
                               )
