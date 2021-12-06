import numpy as np

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

def calculateAVNRTvsAVRT(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro, QRSalt, verbose=False):

    model_function_result = modelFunction(Edad, Edadini, Sexo, Palp_cuello, RV1, Pretro, QRSalt)

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

    return Prob_AVNRT, Prob_AVRT