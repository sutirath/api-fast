#import libraly
from fastapi import FastAPI , File
from pydub import AudioSegment
import numpy as np
import librosa
from tensorflow.keras.models import  load_model


names = ['bad','enemy','good','queen']
model = load_model('model.h5')
model.summary()
app = FastAPI()


#do6main where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    A = AudioSegment.from_file(file)
    A = np.array(A.get_array_of_samples(), np.float32)
    A=librosa.feature.mfcc(A)
    sound = A[:,:939]
    classi = names[model.predict(sound[None,:,:,None]).argmax()]
    acc = model.predict(sound[None,:,:,None]).max()*100    
    return {
        "class":classi,
        "acc":acc
    }
