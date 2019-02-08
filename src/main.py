import requests

auth_request = requests.post("https://eastus.api.cognitive.microsoft.com/sts/v1.0/issuetoken",
                             headers={"Ocp-Apim-Subscription-Key": "{{ Your Subscription Key }}"})
bearer_token = 'Bearer ' + auth_request.text

ssml = """<speak version='1.0' xmlns=\"http://www.w3.org/2001/10/synthesis\" xml:lang='en-US'>
                <voice  name='Microsoft Server Speech Text to Speech Voice (en-US, Jessa24kRUS)'>
                    Welcome to Microsoft Cognitive Services <break time=\"100ms\" /> Text-to-Speech API.
                </voice> </speak>"""

audio_request = requests.post("https://eastus.tts.speech.microsoft.com/cognitiveservices/v1",
                              headers={"Content-Type": "application/ssml+xml",
                                       "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
                                       "User-Agent": "PluralsightDemo",
                                       "Authorization": bearer_token },
                              data=ssml)

with open("speech.mpga","wb") as file:
    file.write(audio_request.content)
