import configparser
from flask import render_template, request
from app import app
from .analyze import Politician


@app.route('/')
@app.route('/index')
def index():
    politicians = configparser.ConfigParser()
    politicians.read('app/static/config/twitter_handles.ini')

    return render_template('index.html',
                           politicians=politicians['Twitter Handles']
                           )


def personality_compare(trait, value_1, value_2, name_1, name_2):
    percentage = 100 * abs(value_1 - value_2)
    if percentage < 0.1:
        return "{} and {} have an equal amount of {}.".format(name_1,
                                                              name_2,
                                                              trait
                                                              )
    elif value_1 > value_2:
        return "{} has {:.1f}% more {} than {}.".format(name_1,
                                                        percentage,
                                                        trait,
                                                        name_2
                                                        )
    elif value_1 < value_2:
        return "{} has {:.1f}% more {} than {}.".format(name_1,
                                                        percentage,
                                                        trait,
                                                        name_2
                                                        )


@app.route('/results', methods=['GET'])
def results():
    twitter_1 = request.args.get('Politician_1')
    twitter_2 = request.args.get('Politician_2')

    if twitter_1 == twitter_2:
        index()
    else:
        politician_1 = Politician(twitter_1)
        politician_2 = Politician(twitter_2)

        modesty = personality_compare("modesty",
                                      politician_1.modesty,
                                      politician_2.modesty,
                                      politician_1.name,
                                      politician_2.name
                                      )
        liberalism = personality_compare("liberalism",
                                         politician_1.liberalism,
                                         politician_2.liberalism,
                                         politician_1.name,
                                         politician_2.name
                                         )
        anger = personality_compare("anger",
                                    politician_1.anger,
                                    politician_2.anger,
                                    politician_1.name,
                                    politician_2.name
                                    )
        intellect = personality_compare("intellect",
                                        politician_1.intellect,
                                        politician_2.intellect,
                                        politician_1.name,
                                        politician_2.name
                                        )
        morality = personality_compare("morality",
                                       politician_1.morality,
                                       politician_2.morality,
                                       politician_1.name,
                                       politician_2.name
                                       )

        return render_template('results.html',
                               politician_1=politician_1.name,
                               politician_2=politician_2.name,
                               twitter_1=twitter_1,
                               twitter_2=twitter_2,
                               image_1=politician_1.profile_pic,
                               image_2=politician_2.profile_pic,
                               modesty=modesty,
                               liberalism=liberalism,
                               anger=anger,
                               intellect=intellect,
                               morality=morality
                               )
