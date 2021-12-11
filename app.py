from flask import Flask, render_template, request
from modelFunctions import *

app = Flask(__name__)
# default-page
@app.route("/")
def home():
   return render_template("index.html")

@app.route('/calculateProbability')
def calculateProbability():
    Edad = float(request.args['Edad'])
    Edadini = float(request.args['Edadini'])
    Sexo = float(request.args['Sexo'])
    Palp_cuello = float(request.args['Palp_cuello'])
    RV1 = float(request.args['RV1'])
    Pretro = float(request.args['Pretro'])

    Prob_AVNRT, Prob_AVRT, clinic_model = calculateAVNRTvsAVRT(Edad=Edad, Edadini=Edadini, Sexo=Sexo, Palp_cuello=Palp_cuello,
                                                 RV1=RV1, Pretro=Pretro, verbose=True)

    Prob_AVNRT = '{:.2f}'.format(Prob_AVNRT)
    Prob_AVRT = '{:.2f}'.format(Prob_AVRT)

    return render_template('index.html', Prob_AVNRT=Prob_AVNRT, Prob_AVRT=Prob_AVRT,
                           Edad=str(int(Edad)), Edadini=str(int(Edadini)),
                           Sexo=int(Sexo), Palp_cuello=int(Palp_cuello),
                           RV1=int(RV1), Pretro=int(Pretro))

if __name__ == "__main__":
   app.run()
