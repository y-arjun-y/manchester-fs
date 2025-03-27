import numpy as np
import cv2

cone_positions = [(100 + np.random.randn(), 150 + np.random.randn()) for _ in range(50)]

def kalman_filter_smoothing(cone_positions):
    kf = cv2.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([[1, 0, 0, 0],
                                     [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]], np.float32)
    kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

    smoothed_positions = []
    for position in cone_positions:
        x, y = position
        predicted = kf.predict()
        measurement = np.array([[np.float32(x)], [np.float32(y)]])
        corrected = kf.correct(measurement)
        smoothed_x, smoothed_y = corrected[0], corrected[1]
        smoothed_positions.append((float(smoothed_x), float(smoothed_y)))
    return smoothed_positions

def exponential_moving_average(data, alpha=0.3):
    smoothed_data = []
    if not data:
        return smoothed_data

    smoothed_x, smoothed_y = data[0]
    smoothed_data.append((smoothed_x, smoothed_y))

    for x, y in data[1:]:
        smoothed_x = alpha * x + (1 - alpha) * smoothed_x
        smoothed_y = alpha * y + (1 - alpha) * smoothed_y
        smoothed_data.append((smoothed_x, smoothed_y))

    return smoothed_data

if __name__ == "__main__":
    kalman_result = kalman_filter_smoothing(cone_positions)
    ema_result = exponential_moving_average(cone_positions)

    print("Kalman Filter Result Sample:", kalman_result[:5])
    print("EMA Result Sample:", ema_result[:5])
