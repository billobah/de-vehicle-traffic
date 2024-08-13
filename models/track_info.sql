-- Create track_info table
CREATE TABLE track_info (
    track_id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(50),
    traveled_distance FLOAT,
    average_speed FLOAT
);