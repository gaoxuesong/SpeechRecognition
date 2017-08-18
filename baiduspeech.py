# -*- coding: utf-8 -*-

import json
# 引入Speech SDK
from aip import AipSpeech
from baiduspeech.baiduapisettings import BASE_VOICE_STORAGE, APP_ID, API_KEY, SECRET_KEY

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def recognizer(vFile, vType):
    voice_file = BASE_VOICE_STORAGE + vFile + '.' + vType

    # 识别本地文件
    result_str = aipSpeech.asr(get_file_content(voice_file), 'pcm', 16000, {})    

    return json.dumps(result_str, ensure_ascii=False)