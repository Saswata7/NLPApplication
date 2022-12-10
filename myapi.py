import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('EyRjdxdZfH5npG5dixEDi3qkHxeqcQ9MvLkDl0OSKiY')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner_analysis(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion_prediction(self,text):
        response = paralleldots.emotion(text)
        return response

