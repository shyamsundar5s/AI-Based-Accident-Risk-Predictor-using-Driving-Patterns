import numpy as np

def extract_features(fused_data):
    """
    Extract features such as average speed, max acceleration, etc.
    :param fused_data: List of fused data points
    :return: Feature vector
    """
    speeds = [point["speed"] for point in fused_data]
    accelerations = [np.linalg.norm(point["acceleration"]) for point in fused_data]

    features = {
        "avg_speed": np.mean(speeds),
        "max_speed": np.max(speeds),
        "avg_acceleration": np.mean(accelerations),
        "max_acceleration": np.max(accelerations)
    }
    return features
