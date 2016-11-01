import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


class Politician:
    def __init__(self, handle):
        self.twitter_handle = handle

        # Twitter and Watson API keys
        self.twitter_consumer_key = ''
        self.twitter_consumer_secret = ''
        self.twitter_access_token = ''
        self.twitter_access_secret = ''
        self.pi_username = ''
        self.pi_password = ''

        self.set_api_keys()
        self.set_profile_picture()
        self.analyze_tweets()
        self.flatten()
        self.set_personality_data()

    def set_api_keys(self):
        apiFile = open("app/static/api_keys/api.txt", encoding="utf-8")

        self.twitter_consumer_key = apiFile.readline()[:-1]
        self.twitter_consumer_secret = apiFile.readline()[:-1]
        self.twitter_access_token = apiFile.readline()[:-1]
        self.twitter_access_secret = apiFile.readline()[:-1]
        self.pi_username = apiFile.readline()[:-1]
        self.pi_password = apiFile.readline()[:-1]

    def set_profile_picture(self):
        twitter_api = twitter.Api(
                                 consumer_key=self.twitter_consumer_key,
                                 consumer_secret=self.twitter_consumer_secret,
                                 access_token_key=self.twitter_access_token,
                                 access_token_secret=self.twitter_access_secret
                                 )
        statuses = twitter_api.GetUserTimeline(
                                              screen_name=self.twitter_handle,
                                              count=1,
                                              include_rts=False
                                              )
        img = statuses[0].user.profile_image_url
        self.profile_pic = img.replace("_normal", "")

    def analyze_tweets(self):
        twitter_api = twitter.Api(
                                 consumer_key=self.twitter_consumer_key,
                                 consumer_secret=self.twitter_consumer_secret,
                                 access_token_key=self.twitter_access_token,
                                 access_token_secret=self.twitter_access_secret
                                 )

        personality_insights = PersonalityInsights(
                                                  username=self.pi_username,
                                                  password=self.pi_password
                                                  )

        statuses = twitter_api.GetUserTimeline(
                                              screen_name=self.twitter_handle,
                                              count=200,
                                              include_rts=False
                                              )

        tdgd = ""

        for status in statuses:
            if (status.lang == 'en'):
                tdgd += str(status.text.encode('utf-8')) + " "

        self.pi_result = personality_insights.profile(tdgd)

    def flatten(self):  # Flatten function sourced from Codeacademy
        data = {}
        for c in self.pi_result['tree']['children']:
            if 'children' in c:
                for c2 in c['children']:
                    if 'children' in c2:
                        for c3 in c2['children']:
                            if 'children' in c3:
                                for c4 in c3['children']:
                                    if (c4['category'] == 'personality'):
                                        data[c4['id']] = c4['percentage']
                                        if 'children' not in c3:
                                            if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
        self.data = data

    def set_personality_values(self):
        self.cheerfulness = self.data["Cheerfulness"]
        self.trust = self.data["Trust"]
        self.cautiousness = self.data["Cautiousness"]
        self.orderliness = self.data["Orderliness"]
        self.liberalism = self.data["Liberalism"]
        self.anxiety = self.data["Anxiety"]
        self.achievement = self.data["Achievement striving"]
        self.altruism = self.data["Altruism"]
        self.vulnerability = self.data["Vulnerability"]
        self.discipline = self.data["Self-discipline"]
        self.consciousness = self.data["Self-consciousness"]
        self.assertiveness = self.data["Assertiveness"]
        self.friendliness = self.data["Friendliness"]
        self.immoderation = self.data["Immoderation"]
        self.depression = self.data["Depression"]
        self.emotionality = self.data["Emotionality"]
        self.morality = self.data["Morality"]
        self.cooperation = self.data["Cooperation"]
        self.anger = self.data["Anger"]
        self.duitifulness = self.data["Dutifulness"]
        self.excitement = self.data["Excitement-seeking"]
        self.artistic = self.data["Artistic interests"]
        self.gregariousness = self.data["Gregariousness"]
        self.imagination = self.data["Imagination"]
        self.adventurousness = self.data["Adventurousness"]
        self.sympathy = self.data["Sympathy"]
        self.activity = self.data["Activity level"]
        self.modesty = self.data["Modesty"]
        self.efficacy = self.data["Self-efficacy"]
        self.intellect = self.data["Intellect"]

    def print_keys(self):
        print("Twitter Consumer Key " + self.twitter_consumer_key)
        print("Twitter Consumer Secret " + self.twitter_consumer_secret)
        print("Twitter Access Token " + self.twitter_access_token)
        print("Twitter Access Secret " + self.twitter_access_secret)
        print("Watson PI Username " + self.pi_username)
        print("Watson PI Password " + self.pi_password)
