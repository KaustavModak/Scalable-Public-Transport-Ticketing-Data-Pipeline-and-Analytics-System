from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FILE_PATH = os.path.join(BASE_DIR, "data/processed/final_data.csv")

# ROOT ENDPOINT
@app.get("/")
def home():
    return {"message": "Public Transport Ticketing API Running"}

# GET ALL TICKETS
@app.get("/tickets")
def get_tickets():
    df = pd.read_csv(FILE_PATH)
    return df.head(1000).to_dict(orient="records")  # limit for performance

# FILTER BY CITY
@app.get("/tickets/city/{city}")
def get_by_city(city: str):
    df = pd.read_csv(FILE_PATH)
    filtered = df[df["city"].str.lower() == city.lower()]
    return filtered.head(1000).to_dict(orient="records")