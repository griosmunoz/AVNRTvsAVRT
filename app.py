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
    QRSalt = float(request.args['QRSalt'])

    # aux_print = 'INPUT VARIABLES'
    # print(aux_print)
    # aux_print = '- Edad: ' + str(Edad)
    # print(aux_print)
    # aux_print = '- Edadini: ' + str(Edadini)
    # print(aux_print)
    # aux_print = '- Sexo: ' + str(Sexo)
    # print(aux_print)
    # aux_print = '- Palp_cuello: ' + str(Palp_cuello)
    # print(aux_print)
    # aux_print = '- RV1: ' + str(RV1)
    # print(aux_print)
    # aux_print = '- Pretro: ' + str(Pretro)
    # print(aux_print)
    # aux_print = '- QRSalt: ' + str(QRSalt)
    # print(aux_print)

    # Calculate AVNRT vs AVRT Probabilities
    Prob_AVNRT, Prob_AVRT = calculateAVNRTvsAVRT(Edad=Edad, Edadini=Edadini, Sexo=Sexo, Palp_cuello=Palp_cuello, RV1=RV1, Pretro=Pretro, QRSalt=QRSalt, verbose=False)

    # aux_print = 'RESULTS'
    # print(aux_print)
    # aux_print = '- Prob. AVNRT: ' + str(Prob_AVNRT)
    # print(aux_print)
    # aux_print = '- Prob. AVRT: ' + str(Prob_AVRT)
    # print(aux_print)

    Prob_AVNRT = '{:.2f}'.format(Prob_AVNRT)
    Prob_AVRT = '{:.2f}'.format(Prob_AVRT)

    return render_template('index.html', Prob_AVNRT=Prob_AVNRT, Prob_AVRT=Prob_AVRT,
                           Edad=str(int(Edad)), Edadini=str(int(Edadini)),
                           Sexo=int(Sexo), Palp_cuello=int(Palp_cuello),
                           RV1=int(RV1), Pretro=int(Pretro),
                           QRSalt=int(QRSalt))

# @app.route('/shortenurl')
# def shortenurl():
#
#     print(request.args['shortcode'])
#
#     return render_template('index.html', shortcode=request.args['shortcode'])
#
# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

# about-page
# @app.route("/about")
# def about():
#     return render_template("About.html")


if __name__ == "__main__":
   app.run()
