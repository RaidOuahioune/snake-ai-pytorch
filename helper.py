import matplotlib.pyplot as plt
from IPython import display
import threading

plt.ion()



def plot(scores, mean_scores):
    try:
        display.clear_output(wait=True)
        display.display(plt.gcf())
    #     plt.clf()
    #     plt.title('Training...')
    #     plt.xlabel('Number of Games')
    #     plt.ylabel('Score')
        
    #     if not scores or not mean_scores:
    #         print("Scores or mean_scores are empty")
    #         return
        
    #     plt.plot(scores, label='Scores')
    #     plt.plot(mean_scores, label='Mean Scores')
    #     plt.ylim(bottom=0)  # Updated to use 'bottom' instead of 'ymin'
    #     plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    #     plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    #     plt.legend()
    #     plt.show(block=False)
    #     plt.pause(.1)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# plot([1, 2, 3, 4], [1, 1.5, 2, 2.5])
