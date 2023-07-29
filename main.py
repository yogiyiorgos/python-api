from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'mesage': 'Welcome!'}

@app.get('/posts')
def get_posts():
    return {'data': 'This is the posts'}