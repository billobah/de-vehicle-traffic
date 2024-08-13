
import pandas as pd
import numpy as np

def split_csv_to_dataframes(data_file_path, track_file_path, trajectory_file_path):
    """
    Reads a CSV file, splits it into two DataFrames, and writes them to separate CSV files.
    Args:
        data_file_path (str): Path to the CSV file.
        track_file_path (str): Path to save the vehicle data DataFrame (track_info.csv).
        trajectory_file_path (str): Path to save the trajectory data DataFrame (trajectory_info.csv).
    """

    with open(data_file_path, 'r') as file:
        lines = file.readlines()

    cols = lines[0].strip('\n').strip().strip(';').split(';')
    track_cols = cols[:4]
    trajectory_cols = ['track_id'] + cols[4:]

    track_info = []
    trajectory_info = []

    for row in lines[1:]:
        row_values = row.strip('\n').strip().strip(';').split(';')
        track_id = row_values[0]

        # Track data
        track_info.append(row_values[:4])

        # Trajectory data
        remaining_values = row_values[4:]
        trajectory_matrix = [
            [track_id] + remaining_values[i:i + 6]
            for i in range(0, len(remaining_values), 6)
        ]
        trajectory_info.extend(trajectory_matrix)

    df_track = pd.DataFrame(data=track_info, columns=track_cols)
    df_trajectory = pd.DataFrame(data=trajectory_info, columns=trajectory_cols)

    df_track.to_csv(track_file_path, index=False)
    df_trajectory.to_csv(trajectory_file_path, index=False)