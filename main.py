from fastapi import FastAPI
import uvicorn
from recommand import *


app = FastAPI()
Recommand_module = Recommand()

@app.get('/')
def home():
    return "main"

@app.get('/recommand')
def recommand():
    global Recommand_module
    return Recommand_module.get_query_sim_top_k("밤에 가서 건물의 불빛과 함께 예쁜 풍경을 보기")


if __name__ == "__main__":
    uvicorn.run("main:app" , host="127.0.0.1", port=8000)