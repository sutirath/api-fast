from fastapi import FastAPI, File, UploadFile
from pydub import AudioSegment
import numpy as np
#import librosa
#import librosa.display
#from tensorflow.keras.models import  load_model

names = ['bad','enemy','good','queen']
#model = load_model('model.h5')
app = FastAPI()

@app.get("/")
def hello():
    return {"Hello World"}


