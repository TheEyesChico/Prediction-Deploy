from flask import Flask
from flask import render_template
import pickle, numpy as np
from flask import request

# creates a Flask application, named app
app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
# a route where we will display a welcome message via an HTML template
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


# run the application
if __name__ == "__main__":
    app.run(debug=True)