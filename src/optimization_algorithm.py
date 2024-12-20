from scipy.optimize import minimize
import numpy as np

def efficiency_function(params, temperature, vibration, speed):
    # otimiza a eficiencia
    temp_weight, vib_weight, speed_weight = params
    efficiency = -1 * (temp_weight * np.mean(temperature) + 
                       vib_weight * np.mean(vibration) + 
                       speed_weight * np.mean(speed))
    return efficiency
def optimize_production(data):
    #otimizaçao de linha de produção
    temperature = data['temperature']
    vibration = data['vibration']
    speed = data['speed']
    initial_guess = [0.5, 0.3, 0.2]
    bounds = [(0, 1), (0, 1), (0, 1)]
    result = minimize(
        efficiency_function, 
        initial_guess, 
        args=(temperature, vibration, speed), 
        bounds=bounds
    )
    print("Melhores Parâmetros de Produção:", result.x)
    return result.x
