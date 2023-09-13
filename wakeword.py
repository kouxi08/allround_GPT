import struct
from datetime import datetime

import pvporcupine
import pyaudio

porcupine = None
pa = None
audio_stream = None
# 検知したいワード
keywords = ["こんにちは"]
# picovoiceのアクセスキー
ACCESS_KEY = ""
# 検知したいワードの音声ファイル
KEYWORD_FILE_PATH = "こんにちは_ja_windows_v2_1_0.ppn"
# 日本語用のファイル
MODEL_PATH = "porcupine_params_ja.pv"
try:
    # porcupine = pvporcupine.create(keywords=keywords, access_key=access_key)
    porcupine = pvporcupine.create(access_key=ACCESS_KEY,
                                   keyword_paths=[KEYWORD_FILE_PATH],
                                   model_path=MODEL_PATH,
                                   )
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
    print("start")
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)
        if result >= 0:
            print('[%s] Detected %s' % (str(datetime.now()), keywords[result]))

finally:
    if porcupine:
        porcupine.delete()

    if audio_stream:
        audio_stream.close()

    if pa:
        pa.terminate()