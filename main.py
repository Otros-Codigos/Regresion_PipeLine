import pandas as pd
from sklearn.metrics import r2_score
from fastapi import FastAPI

from PredictionModel import Model
from DataModel import DataModel, DataList, columnsAll

app = FastAPI()

# Instance the PipeLine
model = Model()
try:
   model.charge()
except Exception:
   model.create()

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/train")
def make_training(data: DataList):

   df = pd.DataFrame(columns=data.data[0].dict().keys())

   for d in data.data:
      new_row = pd.DataFrame(d.dict(), columns=d.dict().keys(), index=[0])
      df = pd.concat([new_row, df]).reset_index(drop = True)

   df.columns = columnsAll()
   Y = df['Life expectancy']
   X = df.drop(['Life expectancy'], axis=1)
   model.fit(X,Y)

   y = model.make_predictions(X)
   r = r2_score(Y, y)

   return {'R²': r}


@app.post("/predict")
def make_predictions(dataModel: DataModel):

   df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
   df.columns = dataModel.columns()

   result = model.make_predictions(df)
   return {"Prediction": result[0]}