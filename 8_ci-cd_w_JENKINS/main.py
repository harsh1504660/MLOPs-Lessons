from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from prediction_model.predict import generate_predictions

app = FastAPI(
    title = "Loan prediction ci cd using jenkins",
    description = "ci cd demo"
)
origin = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class LoanPrediction(BaseModel):
    Gender :str
    Married :str
    Dependents:str
    Education:str
    Self_Employed:str
    ApplicantIncome :float
    CoapplicantIncome:float
    LoanAmount:float
    Loan_Amount_Term:float
    Credit_History:float
    Property_Area:str

@app.get("/")
def index():
    return {"message":"welcome to loan prediction app"}

@app.post("/prediction_api")
def predict(load_details:LoanPrediction):
    data = load_details.model_dump()
    prediction = generate_predictions([data])['prediction'][0]
    if prediction =='Y':
        pred = 'Aproved'
    else :
        pred = 'Rejected'
    return {"status":pred}

@app.post("/prediction_ui")
def predict_gui(Gender :str,
    Married :str,
    Dependents:str,
    Education:str,
    Self_Employed:str,
    ApplicantIncome :float,
    CoapplicantIncome:float,
    LoanAmount:float,
    Loan_Amount_Term:float,
    Credit_History:float,
    Property_Area:str):

    input_data = [Gender,Married,Dependents,
    Education,Self_Employed,ApplicantIncome,
    CoapplicantIncome,LoanAmount,Loan_Amount_Term,
    Credit_History,Property_Area]

    colo ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    data_dict = dict(zip(cols,input_data))
    prediction = generate_predictions([data_dict])['prediction'][0]
    if prediction =='Y':
        pred = 'Aproved'
    else :
        pred = 'Rejected'
    return {"status":pred}

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)