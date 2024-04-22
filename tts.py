from TTS.api import TTS
import torch
from pydub import AudioSegment
import os
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def voice_cloning(chunks):

    output_audio = AudioSegment.empty()
    for chunk in chunks:
        tts.tts_to_file(text=chunk,
                        file_path="output_temp.wav",
                        speaker_wav="1.wav",
                        language='ar')
        chunk_audio = AudioSegment.from_wav("output_temp.wav")
        output_audio += chunk_audio
        os.remove("output_temp.wav")
    return output_audio.export("output_combined.wav", format="wav")


def split_text(input_text):
    
    chunk_size = 160
    chunks = []
    current_chunk = ""

    for word in input_text.split():
        if len(current_chunk) + len(word) <= chunk_size:
            current_chunk += word + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + " "

    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks