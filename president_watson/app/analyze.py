import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


class President:
    def __init__(self):
        self.twitter_consumer_key = ''
        self.twitter_consumer_secret = ''
        self.twitter_access_token = ''
        self.twitter_access_secret = ''
        self.pi_username = ''
        self.pi_password = ''

    def set_API_keys(self):
        apiFile = open("app/static/api_keys/api.txt", encoding="utf-8")

        self.twitter_consumer_key = apiFile.readline()[:-1]
        self.twitter_consumer_secret = apiFile.readline()[:-1]
        self.twitter_access_token = apiFile.readline()[:-1]
        self.twitter_access_secret = apiFile.readline()[:-1]
        self.pi_username = apiFile.readline()[:-1]
        self.pi_password = apiFile.readline()[:-1]

    def getProfilePicture(self, handle):
        twitter_api = twitter.Api(
                                 consumer_key=self.twitter_consumer_key,
                                 consumer_secret=self.twitter_consumer_secret,
                                 access_token_key=self.twitter_access_token,
                                 access_token_secret=self.twitter_access_secret
                                 )
        statuses = twitter_api.GetUserTimeline(
                                              screen_name=handle,
                                              count=1,
                                              include_rts=False
                                              )
        img = statuses[0].user.profile_image_url

        return img.replace("_normal", "")

    def analyze(self, handle):
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
                                              screen_name=handle,
                                              count=200,
                                              include_rts=False
                                              )

        tdgd = ""

        for status in statuses:
            if (status.lang == 'en'):
                tdgd += str(status.text.encode('utf-8')) + " "
        pi_result = personality_insights.profile(tdgd)

        return pi_result

    # flatten function from codeacademy
    def flatten(self, orig):
        data = {}
        for c in orig['tree']['children']:
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
        return data

    def printKeys(self):
        print("Twitter Consumer Key " + self.twitter_consumer_key)
        print("Twitter Consumer Secret " + self.twitter_consumer_secret)
        print("Twitter Access Token " + self.twitter_access_token)
        print("Twitter Access Secret " + self.twitter_access_secret)
        print("Watson PI Username " + self.pi_username)
        print("Watson PI Password " + self.pi_password)


class Tweeter:
    def __init__(self, handle):
        self.handle = handle
        # self.picture = picture

    def setPersonalityValues(self, personalityDict):
        self.cheerfulness = personalityDict["Cheerfulness"]
        self.trust = personalityDict["Trust"]
        self.cautiousness = personalityDict["Cautiousness"]
        self.orderliness = personalityDict["Orderliness"]
        self.liberalism = personalityDict["Liberalism"]
        self.anxiety = personalityDict["Anxiety"]
        self.achievement = personalityDict["Achievement striving"]
        self.altruism = personalityDict["Altruism"]
        self.vulnerability = personalityDict["Vulnerability"]
        self.discipline = personalityDict["Self-discipline"]
        self.consciousness = personalityDict["Self-consciousness"]
        self.assertiveness = personalityDict["Assertiveness"]
        self.friendliness = personalityDict["Friendliness"]
        self.immoderation = personalityDict["Immoderation"]
        self.depression = personalityDict["Depression"]
        self.emotionality = personalityDict["Emotionality"]
        self.morality = personalityDict["Morality"]
        self.cooperation = personalityDict["Cooperation"]
        self.anger = personalityDict["Anger"]
        self.duitifulness = personalityDict["Dutifulness"]
        self.excitement = personalityDict["Excitement-seeking"]
        self.artistic = personalityDict["Artistic interests"]
        self.gregariousness = personalityDict["Gregariousness"]
        self.imagination = personalityDict["Imagination"]
        self.adventurousness = personalityDict["Adventurousness"]
        self.sympathy = personalityDict["Sympathy"]
        self.activity = personalityDict["Activity level"]
        self.modesty = personalityDict["Modesty"]
        self.efficacy = personalityDict["Self-efficacy"]
        self.intellect = personalityDict["Intellect"]

    def setProfilePicture(self, imgURL):
        self.picture = imgURL

    def getTweeter(self):
        return self
