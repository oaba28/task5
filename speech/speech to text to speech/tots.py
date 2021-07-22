from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/4a88b56e-8551-4d18-ac8e-9fbc6fe14bbb'
apikey = 'dVRJtX0R7cKkQhwrLo6TF5pfveaIETsWOQY5vckiR2rF'


authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open("text1.txt", "r") as f:
    text1 = f.readlines()

text1 = [line.replace('\n', '')for line in text1]
text1 = ''.join(str(line) for line in text1)

print(text1)

with open('./text1.mp3', 'wb') as audio_file:
    res = tts.synthesize(text1, accept='audio/mp3',
                         voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
