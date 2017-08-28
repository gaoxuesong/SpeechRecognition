import platform

APP_ID = 'YOUR_APP_ID' 
# API Key
API_KEY = 'YOUR_API_KEY'
CLIENT_ID = 'YOUR_CLIENT_ID' 

#Secret Key
SECRET_KEY = 'YOUR_SECRET_KEY' 
CLIENT_SECRET = 'YOUR_CLIENT_SECRET' 

ACCESS_TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'

BAIDUAI_URL = 'http://vop.baidu.com/server_api'

GRANT_TYPE = 'client_credentials'

APP_CUID = 'YOUR_APP_CUID'


# Sotrage
if (platform.system() is 'Windows'):
    BASE_VOICE_STORAGE = 'C:/tmp/DeepSpeech/voice/'
    BASE_SPEECH_STORAGE = 'C:/tmp/DeepSpeech/speech/'
else:
    BASE_VOICE_STORAGE = '/opt/DeepSpeech/voice/'
    BASE_SPEECH_STORAGE = '/opt/DeepSpeech/speech/'
