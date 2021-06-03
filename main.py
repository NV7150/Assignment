from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_response():
    return {
        "MyName": "dang0",
        "langs": "C/C++, Java, C#, JS",
        "keywords": "IoT, VR, Application"
    }