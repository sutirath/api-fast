from fastapi import FastAPI, File, UploadFile
from pydub import AudioSegment
import numpy as np
import librosa
import librosa.display
from tensorflow.keras.models import  load_model

names = ['bad','enemy','good','queen']
model = load_model('model.h5')
app = FastAPI()

@app.get("/")
def hello():
    return {"Hello World"}

@app.post("/files/")
async def main(file: bytes = File(...)):
    A = AudioSegment.from_file(file)
    test=A
    test = np.array(test.get_array_of_samples(), np.float32)
    test=librosa.feature.mfcc(test)
    sound = test[:,:939]
    classi = names[model.predict(sound[None,:,:,None]).argmax()]
    acc = model.predict(sound[None,:,:,None]).max()*100
    
    return {
        "class":classi,
        "acc":acc
    }
