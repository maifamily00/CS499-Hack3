import numpy as np
from sklearn import linear_model

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='')

input_freeway = [[10,0,1,8], [10,0,2,9], [10,1,1,13],
                 [5,0,1,15], [5,1,5,16], [5,1,6,18]]

output_freeway = [8,7,5,6,9,9]
reg = linear_model.LinearRegression()
reg.fit(input_freeway, output_freeway)

# freeway = input('Enter freeway: ')
# dir = input('Choose direction (N or W =0, S or E = 1): ')
# day = input('Choose day (Monday = 1, Sunday = 7): ')
# time = input('Enter time (Military Time): ')


@app.route("/")
def Traffic():
    return app.send_static_file('hack.html')

@app.route('/', methods=['POST'])
def my_form_post():

    freeway = request.form['freeway']
    dir =  request.form['dir']
    day =  request.form['day']
    time = request.form['time']
    input_freeway.append([freeway, dir, day, time])
    output_freeway.append(reg.predict([[freeway, dir, day, time]]))
    return reg.predict([[freeway, dir, day, time]])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
