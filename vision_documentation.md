# Vision Sub-team Documentation

The vision system processes stereo camera data from a ZED camera to detect and localise traffic cones for autonomous navigation.

### System Architecture

#### Input Processing

- **ZED Camera Capture**: Acquires stereo image pairs from the ZED camera system
- **Frame Separation**: Splits stereo feed into left and right frames for parallel processing

#### Detection Pipeline

- **Object Detection (YOLOv8)**:
  - Processes left frame using YOLOv8 neural network
  - Identifies and classifies cone objects with bounding boxes
  - Outputs detection confidence scores and object coordinates

#### Depth Estimation

- **Feature Matching**:

  - Matches corresponding features between left and right frames
  - Employs epipolar constraints to ensure geometric consistency
  - Generates disparity map for depth calculation

- **Stereo Triangulation**:
  - Converts 2D detections to 3D world coordinates
  - Calculates distance and position relative to camera frame

#### Localisation System

- **Centroid Recovery**:

  - Processes 3D cone positions from stereo triangulation
  - Filters and validates detected objects

- **Global Position Recovery**:
  - Integrates local cone positions with vehicle telemetry data
  - Transforms coordinates to global reference frame
  - Outputs absolute cone positions for path planning

### Key Features

- Real-time cone detection and tracking
- Robust stereo vision processing with epipolar geometry
- Integration with vehicle telemetry for global positioning
- Scalable architecture supporting additional sensor inputs

### Technical Specifications

- **Camera**: ZED stereo camera system
- **Detection Model**: YOLOv8 object detection network
- **Processing**: Real-time stereo vision pipeline
- **Output**: 3D cone positions in global coordinate system
