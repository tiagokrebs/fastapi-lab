from fastapi import FastAPI
from time import sleep

app = FastAPI()

def syncWait():
    sleep(5)
    print("sync end")

async def asyncWait():
    sleep(5)
    print("async end")

@app.get("/async")
async def root():
    asyncWait()
    return {"message": "Hello async World"}

@app.get("/sync")
def root():
    syncWait()
    return {"message": "Hello sync World"}