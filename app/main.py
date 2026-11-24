from fastapi import FastAPI

app = FastAPI()

# initialize app/register routes
@app.get("/")
async def root():
    return {"message": "Hello World"}