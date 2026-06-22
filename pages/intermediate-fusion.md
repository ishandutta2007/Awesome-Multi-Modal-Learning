# Intermediate / Hybrid Fusion

## Overview
Intermediate fusion strategies combine features at various depths within a neural network. This allows the model to learn interactions between high-level semantic abstractions as well as low-level physical traits.

## Architecture Diagram
```mermaid
graph TD
    A[Modality 1] --> C[Layer 1] --> E[Layer 2]
    B[Modality 2] --> D[Layer 1] --> F[Layer 2]
    C --> F
    D --> E
```
