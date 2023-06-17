# 123456789, 123456789
# 10
import agent
import colors_task as ct
import pandas as pd

ROUNDS = 100
NUM_OF_ITERATIONS = 180

def test_agent(agent_instance):
    """
    This function tests the learning performance of an algorithmic agent playing a decision task.
    Args:
        agent_instance ():
            This instance is the generic instance of an agent class.
    Returns:
        list of [scores in each game, max score, avg score]
    """
    game = ct.SimpleDecisionTask(num_of_repetitions=30, manual_game=False,
                                 my_agent=agent_instance)

    series_all_scores = pd.Series([])

    # running the testing asent software
    for index in range(0, ROUNDS):
        game.start_exp()
        df = game.get_results()

        # for each game the number of iterations
        # will be num_of_repetitions * 6 (combinatorics_options_of_colors) = 180

        series_all_scores[index] = df["Reward"].sum() # summation of the rewards in a specific game is the score.

        game = ct.SimpleDecisionTask(num_of_repetitions=30, manual_game=False,
                                     my_agent=agent_instance)

    max_score = float(series_all_scores.max())
    avg_score = series_all_scores.mean()
    return [series_all_scores, max_score, avg_score]


if __name__ == "__main__":
    agent_n = agent.ComparingColorsAgent()
    print(test_agent(agent_n))


