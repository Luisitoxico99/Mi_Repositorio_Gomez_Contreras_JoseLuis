import numpy as np
import pymc3 as pm

# Datos de ejemplo
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 5, 7, 9])

# Definir el modelo bayesiano
with pm.Model() as modelo:
    # Definir las distribuciones priors para los parámetros
    beta_0 = pm.Normal('beta_0', mu=0, sigma=10)
    beta_1 = pm.Normal('beta_1', mu=0, sigma=10)
    
    # Definir la variable aleatoria dependiente
    mu = beta_0 + beta_1 * x
    
    # Definir la distribución likelihood
    y_obs = pm.Normal('y_obs', mu=mu, sigma=1, observed=y)
    
    # Realizar el muestreo de la distribución posterior
    traza = pm.sample(1000, tune=1000)

# Obtener los resultados
pm.summary(traza)
