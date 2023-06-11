import pandas as pd
import numpy as np
import pygame
import agent
import colors_task as ct

# game = ct.SimpleDecisionTask(num_of_repetitions=30, manual_game=True) # Manual mode
game = ct.SimpleDecisionTask(num_of_repetitions=30, manual_game=False, my_agent=agent.ComparingColorsAgent())  # Agent mode
game.start_exp()
df = game.get_results()
output_path = r"your_path_output.csv" # change here to your own local path
df.to_csv(output_path)
print("The score in this run is %f." % df["Reward"].sum())
print("Number of rounds: %d" % len(df["Reward"]))