


---

## Carpetas

1. *requierments*: Contiene un archivo **.txt** donde se puede encontrar los paquetes de Python necesarios (normalmente no instalados por defecto) que son necesarios para el proyecto. Igualmente dicha información se da en un archivo **.bat** con el fin de poder realizar una rapida ejecusión en *Windows*.

2. *data*: Contiene un archivo **.json** con la información utilizada para hacer *fit* al modelo. Dicha información es la misma que se pasa en *Postman*.

3. *postman*: Contiene dos archivos **.json**. Uno con las pruebas de *train* y *predict* en localhost y otro desplegado en Heroku. 

4. *assests*: Si bien puede estar vacio, contiene el modelo PipeLine guardado como **.joblib**.

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

### POSTMAN


