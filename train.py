import numpy as np
import pickle
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def predict():
    if request.method =='GET':
        return render_template('webapp.html')
    else:
        features = [float(i) for i in request.form.values()]
        array_features = [np.array(features)]
        model = pickle.load(open('saved_model.pkl', 'rb'))
        prediction = model.predict(array_features)
        output = prediction

        # Check the output values and retrive the result with html tag based on the value
        if output == 1:
            result='Kemungkinan besar Anda terkena penyakit jantung!'
            result2='Disarankan untuk melakukan pemeriksaan pada dokter dan jangan lupa tetap jaga kesehatan ya!'
        else:
            result='Anda diprediksi tidak memiliki penyakit jantung!'
            result2='Jangan lupa jaga kesehatan ya!'
    return render_template('webapp.html', result=result,result2 = result2)

@app.route('/info')
def info():
    return render_template('information.html')


if __name__ == '__main__':
    app.run()