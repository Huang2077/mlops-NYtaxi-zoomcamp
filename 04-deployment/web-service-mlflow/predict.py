import pickle
import mlflow
from mlflow.tracking import MlflowClient

import os
from flask import Flask, request, jsonify


RUN_ID = 'm-6068cbce8f9c480a81d34754ff5687ca'

logged_model = f's3://mlflow-models-alexey/1/{RUN_ID}/artifacts/model'
# logged_model = f'runs:/{RUN_ID}/model'
model = mlflow.pyfunc.load_model(logged_model)


with open(path, 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    return preds[0]


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration' : pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)