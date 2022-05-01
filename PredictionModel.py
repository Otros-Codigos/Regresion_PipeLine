"""
    Santiago Bobadilla
    Juan José Beltrán

    PIPELINE
"""

# Librerias
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline
from joblib import load, dump

# Clase personalizada que permite eliminar columnas por medio de una lista, 
# dado que el PIPELINE hace transform automaticamente cuando corre.
class columnDropperTransformer():

    # Constructor
    def __init__(self,columns):
        self.columns=columns

    # Tranform ~ eliminar las columnas
    def transform(self,X,y=None):
        return X.drop(self.columns,axis=1)

    # Ajustar el modelo (nulo por efecto de simplicidad)
    def fit(self, X, y=None):
        return self

# PIPELINE COMPLETO
class Model:

    # Contructor ~ Inicialmente no existe modelo. 
    # Es decir, se debe o cargar o crear.
    def __init__(self):
        self.model = None
    

    # Crear el modelo.
    def create(self):

        # Creación del PipeLine con base a una lista fija de columnas por borrar, la transformación personalizada y el tipo de modelo que se va correr.
        self.model = Pipeline([
                ("features", FeatureUnion([
                ("columnDropper", columnDropperTransformer(['infant deaths',
                                                    'percentage expenditure',
                                                    'Hepatitis B',
                                                    'under-five deaths',
                                                    'Population',
                                                    'thinness 5-9 years']))
                ])),
                ('classifier', LinearRegression())
            ])

        # Guardar el modelo para futuras ocaciones.
        dump(self.model, 'assets/modelo.joblib')

        # Reportar que el modelo fue creado.
        print("PipeLine Creado")


    # Cargar el modelo.
    def charge(self):

        # Si ya se creo uno en una ocación pasada, este se carga.
        self.model = load("assets/modelo.joblib")

        # Se reporta que el modelo fue cargado y NO creado.
        print("PipeLine Cargado")


    # Ajustar el modelo por medio de información real X y Y
    def fit(self, X, Y):
        self.model.fit(X,Y)

    
    # Predecir Y con base a un solo registro de Y.
    def make_predictions(self, data):
        return self.model.predict(data)