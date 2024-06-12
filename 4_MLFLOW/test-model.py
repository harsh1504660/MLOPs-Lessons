import mlflow
logged_model = 'runs:/2669849bf9c5430496fa25160f2771e0/RandomForestClassifier'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

import pandas as pd
data = [[
                1.0,
                0.0,
                0.0,
                0.0,
                0.0,
                4.98745,
                360.0,
                1.0,
                2.0,
                8.698
            ]]
print("prediction is : {}".format(loaded_model.predict(pd.DataFrame(data))))
