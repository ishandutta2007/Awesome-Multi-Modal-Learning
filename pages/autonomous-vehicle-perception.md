# Autonomous Vehicle Perception Stacks

## Overview
Self-driving cars fuse data from disparate sensors (Cameras, LiDAR, Radar) to create a comprehensive 3D Bird's-Eye View (BEV) representation of the environment, ensuring robustness under various weather conditions.

## Architecture Diagram
```mermaid
graph TD
    A[LiDAR] --> D[Feature Extraction]
    B[Cameras] --> E[Feature Extraction]
    C[Radar] --> F[Feature Extraction]
    D --> G(BEV Fusion Module)
    E --> G
    F --> G
    G --> H[3D Object Detection]
```
