import numpy as np
import pandas as pd

# Load user interactions data
df = pd.read_csv(r"C:\Users\maroua\Desktop\user_interactions.csv")

# Define actions
actions = ["click", "scroll", "hover", "type"]
action_to_index = {a: i for i, a in enumerate(actions)}
Q_table = np.zeros((len(actions), len(actions)))

alpha = 0.1   
gamma = 0.9   
epsilon = 0.2

# Train the model
for i in range(len(df) - 1):
    state = action_to_index[df.loc[i, "action"]]
    next_state = action_to_index[df.loc[i + 1, "action"]]

    # Assign rewards 
    reward = 1 if state == next_state else 0

    # Q-learning update rule
    Q_table[state, next_state] = (1 - alpha) * Q_table[state, next_state] + alpha * (reward + gamma * np.max(Q_table[next_state]))

np.save(r"C:\Users\maroua\Desktop\Q_table.npy", Q_table)
