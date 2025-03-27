In visual perception systems using the ZED SDK, cone detection data may be noisy due to frame rate variations, lighting conditions, or minor detection inaccuracies. Applying **temporal filtering** techniques such as the **Kalman Filter** or **Exponential Moving Average (EMA)** can help smooth this data over time, resulting in more stable and accurate tracking.

The **Kalman Filter** is a recursive estimator used to predict and correct the position of an object based on noisy observations. It works in two steps:
- **Prediction**: Estimates the next state from the current state.
- **Update**: Refines the prediction using the latest measurement.


In our case, cone positions detected per frame (e.g., from the ZED SDK) can be input to a Kalman Filter to smooth their (x, y) coordinates across time (see `kalman_filtering_boilerplate.py` for potential first-step). In addition, the **EMA** is a simpler filtering technique that gives exponentially decreasing weights to past observations where **more recent positions** are weighted more heavily. This is a bit **smoother and computationally cheaper** than a Kalman Filter.