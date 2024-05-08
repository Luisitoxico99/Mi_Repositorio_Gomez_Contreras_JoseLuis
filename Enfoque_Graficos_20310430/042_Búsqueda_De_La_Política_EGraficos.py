import numpy as np

class PolicyIteration:
    def __init__(self, num_states, num_actions, gamma=0.9, theta=1e-5):
        self.num_states = num_states
        self.num_actions = num_actions
        self.gamma = gamma  # Factor de descuento
        self.theta = theta  # Umbral de convergencia
        self.policy = np.ones((num_states, num_actions)) / num_actions  # Política inicial uniforme
        self.values = np.zeros(num_states)  # Función de valor inicializada a cero

    def evaluate_policy(self, env):
        while True:
            delta = 0
            for state in range(self.num_states):
                v = self.values[state]
                new_v = 0
                for action in range(self.num_actions):
                    action_prob = self.policy[state, action]
                    next_state, reward = env.step(state, action)
                    new_v += action_prob * (reward + self.gamma * self.values[next_state])
                self.values[state] = new_v
                delta = max(delta, abs(v - self.values[state]))
            if delta < self.theta:
                break

    def improve_policy(self, env):
        policy_stable = True
        for state in range(self.num_states):
            old_action = np.argmax(self.policy[state])
            action_values = np.zeros(self.num_actions)
            for action in range(self.num_actions):
                next_state, reward = env.step(state, action)
                action_values[action] = reward + self.gamma * self.values[next_state]
            best_action = np.argmax(action_values)
            if old_action != best_action:
                policy_stable = False
            self.policy[state] = np.eye(self.num_actions)[best_action]
        return policy_stable

    def policy_iteration(self, env):
        while True:
            self.evaluate_policy(env)
            policy_stable = self.improve_policy(env)
            if policy_stable:
                break

# Ejemplo de un entorno de aprendizaje
class Environment:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_matrix = np.random.rand(num_states, num_actions, num_states)  # Matriz de transición aleatoria
        self.reward_matrix = np.random.rand(num_states, num_actions)  # Matriz de recompensa aleatoria

    def step(self, state, action):
        # Simulación de una transición de estado y una recompensa basada en la acción elegida
        next_state = np.random.choice(self.num_states, p=self.transition_matrix[state, action])
        reward = self.reward_matrix[state, action]
        return next_state, reward

# Parámetros del entorno y el algoritmo
num_states = 5
num_actions = 3
gamma = 0.9
theta = 1e-5

# Crear el entorno y el algoritmo de iteración de políticas
env = Environment(num_states, num_actions)
policy_iteration = PolicyIteration(num_states, num_actions, gamma, theta)

# Realizar la búsqueda de la política
policy_iteration.policy_iteration(env)

# Imprimir la política óptima encontrada
print("Política óptima encontrada:")
print(policy_iteration.policy)
