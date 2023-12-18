from fastapi import FastAPI
from time import sleep
from random import randint

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate_response")
async def send_prompts(body: dict):
    waiting_time = randint(5, 10)
    print(f'wait for {waiting_time}')
    sleep(waiting_time)

    response = f"Hello this is a generate response from you prompt: {body['prompt']}"
    return {"response": response}

