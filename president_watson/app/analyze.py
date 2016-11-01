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
        self.receive_twitter_data()
        self.set_profile_picture()
        self.analyze_tweets()
        self.flatten()
        self.set_personality_data()

    def set_api_keys(self):
        with open("app/static/api_keys/api.txt", encoding="utf-8") as api_file:
            self.twitter_consumer_key = api_file.readline()[:-1]
            self.twitter_consumer_secret = api_file.readline()[:-1]
            self.twitter_access_token = api_file.readline()[:-1]
            self.twitter_access_secret = api_file.readline()[:-1]
            self.pi_username = api_file.readline()[:-1]
            self.pi_password = api_file.readline()[:-1]

    def receive_twitter_data(self):
        twitter_api = twitter.Api(
                                 consumer_key=self.twitter_consumer_key,
                                 consumer_secret=self.twitter_consumer_secret,
                                 access_token_key=self.twitter_access_token,
                                 access_token_secret=self.twitter_access_secret
                                 )
        self.statuses = twitter_api.GetUserTimeline(
                                              screen_name=self.twitter_handle,
                                              count=200,
                                              include_rts=False
                                              )

    def set_profile_picture(self):
        img = self.statuses[0].user.profile_image_url
        self.profile_pic = img.replace("_normal", "")

    def analyze_tweets(self):
        personality_insights = PersonalityInsights(
                                                  username=self.pi_username,
                                                  password=self.pi_password
                                                  )

        twitter_messages = ""
        for status in self.statuses:
            if (status.lang == 'en'):
                twitter_messages += str(status.text.encode('utf-8')) + " "

        self.pi_result = personality_insights.profile(twitter_messages)

    def flatten(self):  # Flatten function sourced from Codeacademy
        data = {}
        for a in self.pi_result['tree']['children']:
            if 'children' in a:
                for b in a['children']:
                    if 'children' in b:
                        for c in b['children']:
                            if 'children' in c:
                                for d in c['children']:
                                    if (d['category'] == 'personality'):
                                        data[d['id']] = d['percentage']
                                        if 'children' not in c:
                                            if c['category'] == 'personality':
                                                data[c['id']] = c['percentage']
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
