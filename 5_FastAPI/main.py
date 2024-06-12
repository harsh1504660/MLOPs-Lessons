from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"hello world"}

@app.get('/demo')
def root():
    return {"message":"hello world from demo"}

@app.post('/postdemo')
def root():
    return {"message":"hello world from post demo"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=30000)