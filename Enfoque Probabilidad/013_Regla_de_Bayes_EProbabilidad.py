# Supongamos que tenemos dos variables aleatorias A y B
# Y queremos calcular la probabilidad de A dado B utilizando la regla de Bayes

# Definimos las probabilidades condicionales P(B|A) y P(A)
P_B_dado_A = 0.8  # Probabilidad de B dado A
P_A = 0.6  # Probabilidad de A

# Calculamos la probabilidad marginal P(B) sumando sobre todas las posibles combinaciones de A y B
# Aquí asumimos que solo hay dos posibles valores para B: verdadero y falso
P_B = P_B_dado_A * P_A + (1 - P_A) * (1 - P_B_dado_A)

# Aplicamos la regla de Bayes para calcular la probabilidad de A dado B
P_A_dado_B = (P_B_dado_A * P_A) / P_B

# Imprimimos el resultado
print("La probabilidad de A dado B es:", P_A_dado_B)
