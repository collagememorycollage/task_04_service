from fastapi import FastAPI
import uvicorn
import pandas as pd
from pydantic import BaseModel
import os
from pathlib import Path

base_path = Path(__file__).resolve().parent
data_file = base_path / "data.csv"

df = pd.read_csv(data_file)
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

@app.get("/get-all-data")
def get_all_data():
    df = pd.read_csv(data_file)
    df['timestep'] = pd.to_datetime(df['timestep'], errors='coerce')
    df = df.reset_index(drop=True)
    df['id'] = df.index
    return df.to_dict(orient="records")

@app.post("/create-data")
def create_data(item: DataEntry):
    new_row = pd.DataFrame([item.dict()])
    new_row.to_csv(data_file, mode='a', index=False, header=False)

@app.delete("/delete-data/{id}")
def delete_data(id):
    df = pd.read_csv(data_file)
    
    df = df.drop(index=int(id))

    df.to_csv(data_file, index=False)
    # return df

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, host="localhost")
