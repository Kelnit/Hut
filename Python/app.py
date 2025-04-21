from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="Hut Model")

@app.get("/")
async def MainFile():
  """
  Main Router
  """
  return {"result":"Simple Hut Application on FastAPI"}