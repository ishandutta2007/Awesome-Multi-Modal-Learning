# Late Fusion (Decision-Level)

## Overview
Late fusion keeps modalities completely separate until the very end. Independent models make predictions based on their respective modalities, and the final decision is made by aggregating these predictions (e.g., voting, averaging).

## Architecture Diagram
```mermaid
graph TD
    A[Modality 1] --> B[Model 1] --> C[Prediction 1]
    D[Modality 2] --> E[Model 2] --> F[Prediction 2]
    C --> G(Aggregator)
    F --> G
    G --> H[Final Decision]
```
