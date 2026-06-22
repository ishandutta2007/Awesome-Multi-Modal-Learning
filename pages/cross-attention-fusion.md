# Cross-Attention Fusion

## Overview
In cross-attention fusion, the self-attention mechanism of Transformers is extended across modalities. One modality acts as the Query, while the other provides the Keys and Values, allowing one stream of information to conditionally process the other.

## Architecture Diagram
```mermaid
graph LR
    A[Text Tokens: Query] --> C[Cross-Attention Layer]
    B[Image Patches: Key/Value] --> C
    C --> D[Contextualized Output Tokens]
```
