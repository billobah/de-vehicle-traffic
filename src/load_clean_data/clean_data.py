import pandas as pd

def clean_track_info(track_info_df):

    # Check for duplicated rows based on all columns
    duplicated_rows = track_info_df[track_info_df.duplicated()]

    # If there are any duplicated rows, display them
    if not duplicated_rows.empty:
        print("Duplicated Rows:")
        print(duplicated_rows)
    else:
        print("No duplicated rows found.")

    # Remove duplicates
    cleaned_track_info_df = track_info_df.drop_duplicates()

    # Display the cleaned DataFrame without duplicates
    print("DataFrame after removing duplicates:")
    print(cleaned_track_info_df)
    
    # Handle missing values
    cleaned_track_info_df['traveled_d'].fillna(0, inplace=True)
    cleaned_track_info_df['avg_speed'].fillna(0, inplace=True)
    
    return cleaned_track_info_df


def clean_trajectory_info(trajectory_info_df):
    # Handle missing values and filter out irrelevant data
    cleaned_trajectory_info_df = trajectory_info_df.dropna(subset=['lat', 'lon'])
    
    return cleaned_trajectory_info_df