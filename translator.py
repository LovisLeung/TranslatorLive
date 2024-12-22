import subprocess
from subprocess import DEVNULL

from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# External program startup
process_run_server = subprocess.Popen(
    ['python', 'WhisperLive-0.5.1/run_server.py',
     '--backend', 'faster_whisper',
     '--omp_num_threads', '6'], # thread: 6(max12)
    stdout=DEVNULL,
    stderr=DEVNULL
)

process_client = subprocess.Popen(
    ['python', 'WhisperLive-0.5.1/whisper_live/client.py'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)

try:
    with process_client.stdout as pipe:
        for line in pipe:
            whisper_live_text = str(line.strip())
            translator = GoogleTranslator(source="en", target="zh-CN")
            result = translator.translate(text=whisper_live_text)
            print(result)
except Exception as e:
    print(f"Error_exist: {e}")
return_code = process_client.wait()
print(f"Ending_Code: {return_code}")