from fastapi import FastAPI
import uvicorn
import pandas as pd
from pydantic import BaseModel

df = pd.read_csv('data.csv')
df['timestep'] = pd.to_datetime(df['timestep'], errors='coerce')

class DataEntry(BaseModel):
    timestep: str
    consumption_eur: float
    consumption_sib: float
    price_eur: float
    price_sib: float


df = df.reset_index(drop=True)
df['id'] = df.index

app = FastAPI()

@app.get("/get-date")
def get_date(date):
    filtered_df = df[df['timestep'] == date]
    
    return filtered_df.to_dict(orient="records")

@app.post("/create-data")
def create_data(item: DataEntry):
    new_row = pd.DataFrame([item.dict()])
    new_row.to_csv('data.csv', mode='a', index=False, header=False)
    # return data 

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, host="192.168.0.180")
