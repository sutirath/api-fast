from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/")
def hello():
    return {"Hello World"}

@app.post("/files/")
async def main(file: bytes = File(...)):
    return {"file_size": len(file)}
