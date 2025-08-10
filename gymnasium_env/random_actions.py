import numpy as np
import gymnasium
import gymnasium_env
from gymnasium.wrappers import TimeAwareObservation, TimeLimit

env = gymnasium.make('gymnasium_env/GridWorld-v0', render_mode="human")
print(f"Action space: {env.action_space}")  # Discrete(2) - left or right
print(f"Sample action: {env.action_space.sample()}")

# Box observation space (continuous values)
print(f"Observation space: {env.observation_space}")  # Box with 4 values
# Box([-4.8, -inf, -0.418, -inf], [4.8, inf, 0.418, inf])
print(f"Sample observation: {env.observation_space.sample()}")  # Random valid observation
env = TimeLimit(env, max_episode_steps=500)  # Set max steps explicitly
wrapped_env = TimeAwareObservation(env)
# Reset environment to start a new episode
observation, info = env.reset()
# observation: what the agent can "see" - cart position, velocity, pole angle, etc.
# info: extra debugging information (usually not needed for basic learning)

print(f"Starting observation: {observation}")
# Starting observation: {'agent': array([4, 4]), 'target': array([3, 1])}

episode_over = False
total_reward = 0

while not episode_over:
    # Choose an action
    action = env.action_space.sample()  # Random action for now - real agents will be smarter!

    # Take the action and see what happens
    observation, reward, terminated, truncated, info = env.step(action)

    total_reward += reward
    episode_over = terminated or truncated

print(f"Episode finished! Total reward: {total_reward}")
env.close()
