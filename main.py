"""
    Santiago Bobadilla
    Juan José Beltrán

    MAIN
"""

# Librerias
import pandas as pd
from sklearn.metrics import r2_score
from fastapi import FastAPI

# Dependiecias entre archivos
from PredictionModel import Model
from DataModel import DataModel, DataList, columnsAll

# Incializar el API
app = FastAPI()

# incializar el PipeLine
model = Model()

# Por defecto siempre intentar cargar si ya hay un modelo
try:
   model.charge()

# En dado caso de que no exista, se crea un nuevo modelo (pipeline)
except Exception:
   model.create()

# ----------------------------------------------------------------------------

# Ruta inicial
@app.get("/")
def read_root():

   #Muestra los autores del API
   return {"Juan José Beltrán": "Santiago Bobadilla"}

# Ruta de entrenamiento
@app.post("/train")
def make_training(data: DataList):

   # Crea un DataFrame vacio con los nombres de la columnas en el orden en el que le van a llegar Y y X.
   df = pd.DataFrame(columns=data.data[0].dict().keys())

   # Del Body que llega por HTTP se cargan todos los registros en la tabla.
   for d in data.data:
      new_row = pd.DataFrame(d.dict(), columns=d.dict().keys(), index=[0])
      df = pd.concat([new_row, df]).reset_index(drop = True)

   # Se ajustan los nombres de las columnas.
   df.columns = columnsAll()

   # Se separan las variables de respuesta Y y las explicativas X
   Y = df['Life expectancy']
   X = df.drop(['Life expectancy'], axis=1)

   # Se ajusta el modelo.
   model.fit(X,Y)

   # Se calcula las metricas.
   y = model.make_predictions(X)
   r = r2_score(Y, y)

   # Se da respuesta.
   return {'R²': r}

# Ruta de predecir
@app.post("/predict")
def make_predictions(dataModel: DataModel):

   # Castea el JSON que llega a un registro de solo variables explicativas X
   df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
   df.columns = dataModel.columns()

   # Realiza la predicción si el modelo ya esta ajustado
   try:
      result = model.make_predictions(df)
   
   # Realizar el fit con los datos de la carpeta data y luego predecir.
   except Exception:

      # Se carga el Json Predeterminado
      data = pd.read_json("data/data.json")

      # Se ajustan los nombres de las columnas.
      data.columns = columnsAll()

      # Se separan las variables de respuesta Y y las explicativas X
      Y = data['Life expectancy']
      X = data.drop(['Life expectancy'], axis=1)

      # Se ajusta el modelo.
      model.fit(X,Y)

      # Se realiza la predicción
      result = model.make_predictions(df)

   # Se da respuesta.
   return {"Prediction": result[0]}