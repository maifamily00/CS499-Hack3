from sklearn import linear_model

from flask import Flask, request, render_template
app = Flask(__name__)

input_freeway = list()
output_freeway = list()


@app.route('/')
def index():
    return render_template('hack.html')

@app.route('/data', methods=['POST'])
def data():

    freeway = int(request.form['freeway'])
    dir =  int(request.form['dir'])
    day =  int(request.form['day'])
    time = int(request.form['time'])
    traffic = int(request.form['traffic'])

    input_freeway.append([freeway, dir, day, time])
    output_freeway.append([traffic])


    return render_template('hack.html')

@app.route('/predict', methods=['POST'])
def predict():

    reg = linear_model.LinearRegression()
    reg.fit(input_freeway, output_freeway)

    freeway = int(request.form['freeway'])
    dir = int(request.form['dir'])
    day = int(request.form['day'])
    time = int(request.form['time'])

    traffic = reg.predict([freeway, dir, day, time])
    return str(traffic)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
