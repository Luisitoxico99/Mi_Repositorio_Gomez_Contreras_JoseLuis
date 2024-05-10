# Supongamos que tenemos una serie de eventos A1, A2, A3 y A4
# Y queremos calcular la probabilidad conjunta de estos eventos utilizando la regla de la cadena

# Definimos las probabilidades condicionales P(A2|A1), P(A3|A1, A2) y P(A4|A1, A2, A3)
P_A2_dado_A1 = 0.8
P_A3_dado_A1_A2 = 0.6
P_A4_dado_A1_A2_A3 = 0.7

# Definimos las probabilidades marginales P(A1)
P_A1 = 0.5

# Calculamos la probabilidad conjunta utilizando la regla de la cadena
P_conjunta = P_A1 * P_A2_dado_A1 * P_A3_dado_A1_A2 * P_A4_dado_A1_A2_A3

# Imprimimos el resultado
print("La probabilidad conjunta de los eventos A1, A2, A3 y A4 es:", P_conjunta)
