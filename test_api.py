import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware


# 讀取 pickle 檔案
fileName="/Users/mtk12464/Documents/oneStep/20200118_finlab/finlab_ml_course/trader01/../test_to_fastapi.pickle"
with open(fileName, "rb") as f:
    data = pickle.load(f)

# 建立 FastAPI 實例
app = FastAPI(default_response_class=JSONResponse, default_encoding="utf-8")


# 設置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)


# 定義路由處理函式
@app.get("/data")
def get_data():
    return data

@app.post("/data")
def update_data(new_data):
    # 更新資料
    data = new_data

    # 儲存更新後的資料到 pickle 檔案
    with open(fileName, "wb") as f:
        pickle.dump(data, f)

    return {"message": "Data updated successfully"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8882)
