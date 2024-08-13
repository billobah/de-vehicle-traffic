from load_traffic_data import split_csv_to_dataframes

# Example usage
data_file_path = "data/data1.csv"
track_file_path = "data/track_info.csv"
trajectory_file_path = "data/trajectory_info.csv"

split_csv_to_dataframes(data_file_path, track_file_path, trajectory_file_path)

print(f"DataFrames written to: \n - {track_file_path} \n - {trajectory_file_path}")