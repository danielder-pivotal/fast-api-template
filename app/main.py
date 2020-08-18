from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "<h1>Hello, World?</h1>"
