import numpy as np

def fuse_sensors(gps_data, accelerometer_data):
    """
    Fuse GPS and accelerometer data to create a coherent dataset.
    :param gps_data: List of GPS coordinates (lat, long, speed)
    :param accelerometer_data: List of acceleration values (x, y, z)
    :return: Fused dataset combining GPS and accelerometer data
    """
    # Resample data to match timestamps
    min_length = min(len(gps_data), len(accelerometer_data))
    gps_data = gps_data[:min_length]
    accelerometer_data = accelerometer_data[:min_length]

    # Combine data
    fused_data = []
    for i in range(min_length):
        fused_data.append({
            "latitude": gps_data[i]["latitude"],
            "longitude": gps_data[i]["longitude"],
            "speed": gps_data[i]["speed"],
            "acceleration": accelerometer_data[i]
        })
    return fused_data
