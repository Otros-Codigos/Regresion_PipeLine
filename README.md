# Regresion_PipeLine

* Santiago Bobadilla - 201820728
* Juan José Beltrán Ruiz - 201819446

---

## Carpetas

1. *requierments*: Contiene un archivo **.txt** donde se puede encontrar los paquetes de Python necesarios (normalmente no instalados por defecto) que son necesarios para el proyecto. Igualmente dicha información se da en un archivo **.bat** con el fin de poder realizar una rapida ejecusión en *Windows*.

2. *data*: Contiene un archivo **.json** con la información utilizada para hacer *fit* al modelo. Dicha información es la misma que se pasa en *Postman*.

3. *postman*: Contiene dos archivos **.json**. Uno con las pruebas de *train* y *predict* en localhost y otro desplegado en Heroku. 

4. *assests*: Si bien puede estar vacio, contiene el modelo PipeLine guardado como **.joblib**.

5. *results*: Contiene el **.ppt** y el **.pdf** de los resultados de los escenarios.

## Archivos

Todos los archivos explican su funcionamiento internamente por medio de su respectiva documentación:

*   *DataModel.py*: Incluye los modelos usados para el *train* y *predict*.
*   *PredictionModel.py*: Incluye la implementación del **PipeLine** y sus debidos metodos.
*   *main.py*: Incliye la ejecusión del **API** que permite realizar las pruebas necesarias por medio de la aplicación de **POSTMAN**: https://www.postman.com/ 

## Ejecutar

1. Descargar el repositorio e instalar lo necesario con base en la carpeta: **requierments**.

2. Correr el Main por medio del siguiente comando en **terminal**:

```
uvicorn main:app --reload
```

3. Revisar que en consola tenga dos posibles respuestas en texto plano:

```
PipeLine Creado        or        PipeLine Cargado
```

4. Correr las pruebas en **POSTMAN**.

## POSTMAN

Para correr las pruebas de manera local se debe usar cualquiera de los siguientes links dependiendo de la necesidad:

*   *Train*:http://127.0.0.1:8000/train
*   *Predict*: http://127.0.0.1:8000/predict

Cada uno de dichos links requiere un archivo **json** pasado como **raw** en **body** por medio de Postamn bajo la siguiente estructura: 

***TRAIN***

Es de suma importancia notar que el JSON de la carpeta data es un listado de registros. Para que el API funcione, dicha lista debe estar guardada en la variable del JSON 'data'. Aparte es necesaria la información de la variable Y, como sus explicativas X.

```
{
  "data": [
    {
      "life_expentancy": 0,
      "adult_mortality": 0,
      "infant_deaths": 0,
      "alcohol": 0,
      "percentage_expenditure": 0,
      "hepatitis_B": 0,
      "measles": 0,
      "bmi": 0,
      "under_five_deaths": 0,
      "polio": 0,
      "total_expenditure": 0,
      "diphtheria": 0,
      "hiv_aids": 0,
      "gdp": 0,
      "population": 0,
      "thinness_10_19_years": 0,
      "thinness_5_9_years": 0,
      "income_composition_of_resources": 0,
      "schooling": 0
    },
    {
      "life_expentancy": 0,
      "adult_mortality": 0,
      "infant_deaths": 0,
      "alcohol": 0,
      "percentage_expenditure": 0,
      "hepatitis_B": 0,
      "measles": 0,
      "bmi": 0,
      "under_five_deaths": 0,
      "polio": 0,
      "total_expenditure": 0,
      "diphtheria": 0,
      "hiv_aids": 0,
      "gdp": 0,
      "population": 0,
      "thinness_10_19_years": 0,
      "thinness_5_9_years": 0,
      "income_composition_of_resources": 0,
      "schooling": 0
    }
  ]
}
```

***PREDICT***

Para predecir se pasan las variables explicativas X y nada más. Se debe aclarar que si el modelo acaba de ser creado con el fin de lograr predecir debe realizar primero un ajusto, por tanto, si bien el **API** verifica dicha afirmación, se sugiere correr primero las pruebas de *train* y luego las de *predict* como aparecen en las colecciones de Postman suministardas. 

```
{
  "adult_mortality": 0,
  "infant_deaths": 0,
  "alcohol": 0,
  "percentage_expenditure": 0,
  "hepatitis_B": 0,
  "measles": 0,
  "bmi": 0,
  "under_five_deaths": 0,
  "polio": 0,
  "total_expenditure": 0,
  "diphtheria": 0,
  "hiv_aids": 0,
  "gdp": 0,
  "population": 0,
  "thinness_10_19_years": 0,
  "thinness_5_9_years": 0,
  "income_composition_of_resources": 0,
  "schooling": 0
}
```

## Escenarios 

Los resultados de los escenarios se encuentran en el **.pdf** en la carpeta **results**, así como se suministran las colecciones ejecutables donde se puede revisar lo dicho. En total se tienen 5 pruebas de predict, y 1 de train.

0. *Train*: Carga una tabla de datos y devuelve la métrica de R^2.
1. *Predict*: Prueba y valor lógico correctos.
2. *Predict*: Prueba y valor lógico correctos.
3. *Predict*: Prueba correcta y valor lógico incorrecto.
4. *Predict*: Prueba correcta y valor lógico incorrecto.
5. *Predict*: Prueba incorrecta.

Como conclusiones de porque un resultado es incorrecto se tiene un explicación visible de los datos. Cuando una variable esta fuera de su rango normal (definase normal, como dentro de los limites estipulados por el negocio y la naturaleza para dicho componente) la predicción es errorea. Un segundo resultado no evidente por lo obtenido en el análisis del laboratio 3 puede ser entrenar el modelo con datos que tengan problemas dentro de los supuestos. 

Como conclusión cuando la aplicación falla se debe unicamente a la violación de los parametros del **json** pasados en postamn, es decir, falta algun parametro. 

Como medida de solución, se propone: *Realizar una validación por medio del API de los datos, buscando comprobar si todas las variables estan dentro del rango normal, o en su defecto, usar un SimpleImputer de la libreria Sklearn. Así se logra validar que la información presentada sea correcta. Segundo, programar filtros personalizados que permitan remover columnas o transformar los datos cuando un supuesto se viole con el fin de saber que los resultados del modelo son fiables. Tercero, y ya respecto al API, permiter que no se pasen ciertos campos sin marcar error, pero que dichos campos sean luego imputados por medio de alguna tecnica.*
