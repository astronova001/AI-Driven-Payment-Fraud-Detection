from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('model/random_forest_model.pkl')
scaler = joblib.load('model/scaler.pkl')  # Load the saved scaler

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict_get():
    return render_template('predict.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predict', methods=['POST'])
def predict_post():
    try:
        # Get form data
        data = {
            'step': [float(request.form['step'])],
            'type': [float(request.form['type'])],
            'amount': [float(request.form['amount'])],
            'oldbalanceOrg': [float(request.form['oldBalanceOrigin'])],
            'oldbalanceDest': [float(request.form['oldBalanceDestination'])]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame(data)

        # Scale the input data using the loaded scaler
        input_scaled = scaler.transform(input_df)

        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]

        # Print prediction in the terminal (for debugging)
        print(f'Prediction: {prediction}')
        print(f'Prediction Probability: {prediction_proba}')
        print(f'Input Data: {input_df}')

        # Render the result page with prediction data
        return render_template(
            'result.html',
            prediction=prediction,
            probability=prediction_proba
        )
    
    except Exception as e:
        print(f"Error: {e}")
        return render_template('result.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
