import numpy as np

def modelFunctionGlobal(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro):

    # function(Edad=56, Palp_cuello="No", Sexo="Female", Edadini=40,
    #          Pretro="No", RV1="No")
    # {
    #     -0.92167009
    #     + 0.003310067 * Edad
    #     + 1.5677935e-06 * pmax(Edad - 27, 0) ^ 3
    #     - 3.6344303e-06 * pmax(Edad - 56, 0) ^ 3
    #     + 2.0666368e-06 * pmax(Edad - 78, 0) ^ 3
    #     + 1.3953093 * (Palp_cuello == "Yes")
    #     + 0.45189063 * (Sexo == "Female")
    #     + 0.038070991 * Edadini
    #     - 2.5235519e-06 * pmax(Edadini - 14, 0) ^ 3
    #     + 4.6461657e-06 * pmax(Edadini - 41, 0) ^ 3
    #     - 2.1226138e-06 * pmax(Edadini - 73.1, 0) ^ 3
    #     - 1.3506311 * (Pretro == "Yes")
    #     + 2.4980727 * (RV1 == "Yes")
    # }

    model_function_result = -0.92167009\
                            + 0.003310067 * Edad\
                            + (1.5677935e-06 * np.power(np.max(Edad - 27, 0), 3))\
                            - (3.6344303e-06 * np.power(np.max(Edad - 56, 0), 3))\
                            + (2.0666368e-06 * np.power(np.max(Edad - 78, 0), 3))\
                            + (1.3953093 * Palp_cuello)\
                            + (0.45189063 * Sexo)\
                            + (0.038070991 * Edadini)\
                            - (2.5235519e-06 * np.power(np.max(Edadini - 14, 0), 3))\
                            + (4.6461657e-06 * np.power(np.max(Edadini - 41, 0), 3))\
                            - (2.1226138e-06 * np.power(np.max(Edadini - 73.1, 0), 3))\
                            - (1.3506311 * Pretro)\
                            + (2.4980727 * RV1)

    return model_function_result

def modelFunctionClinic(Edad, Edadini, Sexo, Palp_cuello):

    # function(Edad=56, Palp_cuello="No", Sexo="Female", Edadini=40)
    # {
    #     -1.4271779
    #     + 0.0046822421 * Edad
    #     - 1.2980809e-06 * pmax(Edad - 27, 0) ^ 3
    #     + 3.0091875e-06 * pmax(Edad - 56, 0) ^ 3
    #     - 1.7111066e-06 * pmax(Edad - 78, 0) ^ 3
    #     + 1.5176917 * (Palp_cuello == "Yes")
    #     + 0.58600511 * (Sexo == "Female")
    #     + 0.043353257 * Edadini
    #     - 1.8409627e-06 * pmax(Edadini - 14, 0) ^ 3
    #     + 3.389436e-06 * pmax(Edadini - 41, 0) ^ 3
    #     - 1.5484733e-06 * pmax(Edadini - 73.1, 0) ^ 3
    # }

    model_function_result = -1.4271779\
                            + (0.0046822421 * Edad)\
                            - (1.2980809e-06 * np.power(np.max(Edad - 27, 0), 3))\
                            + (3.0091875e-06 * np.power(np.max(Edad - 56, 0), 3))\
                            - (1.7111066e-06 * np.power(np.max(Edad - 78, 0), 3))\
                            + (1.5176917 * Palp_cuello)\
                            + (0.58600511 * Sexo)\
                            + (0.043353257 * Edadini)\
                            - (1.8409627e-06 * np.power(np.max(Edadini - 14, 0), 3))\
                            + (3.389436e-06 * np.power(np.max(Edadini - 41, 0), 3))\
                            - (1.5484733e-06 * np.power(np.max(Edadini - 73.1, 0), 3))

    return model_function_result

def modelFunction(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro, QRSalt):

    # ORIGINAL MODEL IN R
    # -1.3652367 - 0.017194461 * Edad\
    # + 5.9542216e-05 * pmax(Edad - 22.95, 0) ^ 3\
    # - 0.00039731049 * pmax(Edad - 42, 0) ^ 3\
    # + 0.0010345862 * pmax(Edad - 56, 0) ^ 3\
    # - 0.0011521644 * pmax(Edad - 69, 0) ^ 3\
    # + 0.00045534642 * pmax(Edad - 81, 0) ^ 3\
    # + 1.5607585 * (Palp_cuello == "Yes")\
    # + 0.63123388 * (Sexo == "Female")\
    # + 0.087535778 * Edadini\
    # - 8.6297031e-05 * pmax(Edadini - 10, 0) ^ 3\
    # + 0.00023554448 * pmax(Edadini - 24, 0) ^ 3\
    # - 0.00026624779 * pmax(Edadini - 40, 0) ^ 3\
    # + 0.00016574799 * pmax(Edadini - 58, 0) ^ 3\
    # - 4.8747652e-05 * pmax(Edadini - 77, 0) ^ 3\
    # - 1.2827899 * (Pretro == "Yes")\
    # + 2.6300718 * (RV1 == "Yes")\
    # - 0.60656125 * (QRSalt == "Yes")

    model_function_result = -1.3652367 - 0.017194461 * Edad\
                            + (5.9542216e-05 * np.power(np.max(Edad - 22.95, 0), 3)) \
                            - (0.00039731049 * np.power(np.max(Edad - 42, 0), 3))\
                            + (0.0010345862 * np.power(np.max(Edad - 56, 0), 3))\
                            - (0.0011521644 * np.power(np.max(Edad - 69, 0), 3))\
                            + (0.00045534642 * np.power(np.max(Edad - 81, 0), 3))\
                            + (1.5607585 * Palp_cuello)\
                            + (0.63123388 * Sexo)\
                            + (0.087535778 * Edadini)\
                            - (8.6297031e-05 * np.power(np.max(Edadini - 10, 0), 3))\
                            + (0.00023554448 * np.power(np.max(Edadini - 24, 0), 3))\
                            - (0.00026624779 * np.power(np.max(Edadini - 40, 0), 3))\
                            + (0.00016574799 * np.power(np.max(Edadini - 58, 0), 3))\
                            - (4.8747652e-05 * np.power(np.max(Edadini - 77, 0), 3))\
                            - (1.2827899 * Pretro)\
                            + (2.6300718 * RV1)\
                            - (0.60656125 * QRSalt)

    return model_function_result

def calculateAVNRTvsAVRT(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro, verbose=False):

    # Old model
    # model_function_result = modelFunction(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro, QRSalt)

    clinic_model = 0

    if RV1 == -1 or Pretro == -1:
        # Clinic Model (No ECG)
        model_function_result = modelFunctionClinic(Edad, Edadini, Sexo, Palp_cuello)
        clinic_model = 1

        if verbose:
            aux_print = ' - CLINIC MODEL'
            print(aux_print)
    else:
        # Global Model
        model_function_result = modelFunctionGlobal(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro)

        if verbose:
            aux_print = ' - GLOBAL MODEL'
            print(aux_print)

    if verbose:
        aux_print = ' - model_function_result: ' + str(model_function_result)
        print(aux_print)

    # plogis(q, location=0, scale=1, lower.tail = TRUE, log.p = FALSE)
    # Inverse of the logit function
    aux_prob = 1/(1+np.exp(-model_function_result))

    if verbose:
        aux_print = ' - aux_prob: ' + str(aux_prob)
        print(aux_print)

    # RESULTS
    Prob_AVNRT = aux_prob
    Prob_AVRT = 1 - Prob_AVNRT

    return Prob_AVNRT, Prob_AVRT, clinic_model