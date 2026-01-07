from fastapi import FastAPI

app = FastAPI(title="Hut Model Inf")

async def index():
  """
  Main Router
  """
  return {"message": "Welcome to the Hut Model Inf API"}