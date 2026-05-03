import speech_recognition as sr
import pyaudio
import wave
import json, requests
from django.http import JsonResponse


def microphone():
    # the file name output you want to record into
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 10
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()
 
def extract(audio_path):
    # wf = wave.open(audio_path, "wb")
    return audio_path.encode('utf-8').strip()
    # audio_path = "genevieve.wav"
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        r.adjust_for_ambient_noise(source)
 
        print("Converting Audio To Text ..... ")

        audio = r.listen(source)
        loaded_text=dict(audio)
        # loaded_text= {
        #     "audio" : audio,
        # }
        return JsonResponse(loaded_text,safe=False)
        # r = json.dumps(audio, indent=10)
        # loaded_r = json.loads(r)
        # return loaded_r

        # print("Converted Audio Is : \n" + r.recognize_google(audio))
    # try:
    #     print("Converted Audio Is : \n" + r.recognize_google(audio))
    # except Exception as e:
#     #     print("Error {} : ".format(e) )



# def process(file_content, file_extension):
#     """
#     Wrapper function to detect the file extension and call text
#     extraction function accordingly

#     :param file_path: path of file of which text is to be extracted
#     :param extension: extension of file `file_name`
#     """
#     jd_lines = ""
#     if file_extension == ".docx":
#         jd_lines = extract_text_from_docx(file_content)
#         return jd_lines
#     elif file_extension == ".DOCX":
#         jd_lines = extract_text_from_docx(file_content)
#         return jd_lines
    
#     else:
#         error_status_code = {
#             "status": "failure",
#             "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
#             "message": "file_content and file_extension Mismatch/Missing",
#         }
#         return error_status_code