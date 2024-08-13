-- Create trajectory_info table
CREATE TABLE trajectory_info (
    track_id VARCHAR(255) REFERENCES track_info(track_id),
    lat FLOAT,
    lon FLOAT,
    speed FLOAT,
    lon_acc FLOAT,
    lat_acc FLOAT,
    time FLOAT
);