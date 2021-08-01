from flask import Flask, render_template, request
import pickle

from sklearn.ensemble import RandomForestRegressor



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        cement = request.form['cement']
        slag = request.form['slag']
        fly_ash = request.form['fly_ash']
        water = request.form['water']
        superplasticizer = request.form['superplasticizer']
        coarseaggregate = request.form['coarseaggregate']
        fineaggregate = request.form['fineaggregate']
        age = request.form['age']
        

        data = [[float(cement),float(slag),float(fly_ash),float(water),float(superplasticizer),float(coarseaggregate)
        ,float(fineaggregate),float(age)]]

        rnd = pickle.load(open('loaded_model.pkl','rb'))
        prediction = rnd.predict(data)[0]
    return render_template('index.html',output="concrete compressive strength prediction is :{}".format(prediction) )














if __name__ == '__main__':
    app.run()