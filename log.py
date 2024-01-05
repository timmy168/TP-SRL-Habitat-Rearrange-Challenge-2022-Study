import re
import matplotlib.pyplot as plt

def extract_values_from_log(log_file):
    success_values = []
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'rearrangepick_success: (\d+\.\d+)', line)
            # match = re.search(r'place_success: (\d+\.\d+)', line)
            if match:
                success_values.append(float(match.group(1)))
    return success_values

def plot_sampled_values(success_values, sample_interval=5, marker_size=1):
    sampled_values = success_values[::sample_interval]
    # Assuming each update is every 10 entries
    updates = [i * 10 * 4.5 for i in range(1, len(sampled_values) + 1)]  
    plt.plot(updates, sampled_values, marker='o', linestyle='-', color='b', markersize=marker_size)
    plt.xlabel('Checkpoints', fontsize=25)
    plt.ylabel('Pick Success Rate', fontsize=25)
    # plt.ylabel('Place Success Rate', fontsize=25)
    plt.title('Rearrange Pick Success Over Updates', fontsize=25)
    # plt.title('Place Success Over Updates', fontsize=25)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    log_file_path = "pick_train.log"  # Replace with the actual path to your log file
    # log_file_path = "place_train.log"  # Replace with the actual path to your log file
    success_values = extract_values_from_log(log_file_path)
    plot_sampled_values(success_values, sample_interval=10, marker_size=2)
