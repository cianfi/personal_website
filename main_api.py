from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello"}

@app.get('/test')
async def test():
    return {"test": "test"}

@app.post('/post')
async def post():
    print("TEST POST")
    return {"post": "post"}