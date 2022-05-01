
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline, FeatureUnion, make_pipeline
from joblib import load, dump

class columnDropperTransformer():
    def __init__(self,columns):
        self.columns=columns

    def transform(self,X,y=None):
        return X.drop(self.columns,axis=1)

    def fit(self, X, y=None):
        return self

class Model:

    def __init__(self):
        self.model = None
        
    def create(self):
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

        dump(self.model, 'assets/modelo.joblib')
        print("PipeLine Creado")

    def charge(self):
        self.model = load("assets/modelo.joblib")
        print("PipeLine Cargado")

    def fit(self, X, Y):
        self.model.fit(X,Y)

    def make_predictions(self, data):
        return self.model.predict(data)