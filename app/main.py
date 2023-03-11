from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "นายภัทรพล สมสกุล 116310400294-9"}