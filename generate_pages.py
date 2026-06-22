import os

pages_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Multi-Modal-Learning\pages"
os.makedirs(pages_dir, exist_ok=True)

pages = {
    "feature-fusion-era.md": """# The Feature Fusion Era (Late 2000s–2010s)

## Overview
During this era, multi-modal learning was heavily reliant on completely separate network backbones for different modalities. For instance, CNNs were exclusively used for extracting image features, while LSTMs were deployed for sequential text data. The extracted features were then fused either very early or very late in the model.

## Architecture Diagram
```mermaid
graph LR
    A[Image Input] --> B[CNN Backbone]
    C[Text Input] --> D[LSTM Backbone]
    B --> E[Late Fusion / Concatenation]
    D --> E
    E --> F[Final Prediction]
```
""",
    "contrastive-alignment-era.md": """# The Contrastive Alignment Era (CLIP Era)

## Overview
Starting around 2021, popularized by OpenAI's CLIP, the paradigm shifted toward aligning independently processed modalities into a shared representation space. Instead of merging modalities to generate a joint output, models were trained to maximize the cosine similarity between matching text and image pairs.

## Architecture Diagram
```mermaid
graph TD
    A[Image Input] --> B[Image Encoder]
    C[Text Input] --> D[Text Encoder]
    B --> E[Image Embedding]
    D --> F[Text Embedding]
    E --> G((Contrastive Loss))
    F --> G
```
""",
    "native-unified-token-era.md": """# The Native Unified Token Era (2024+)

## Overview
Modern multi-modal frontier models natively tokenize all modalities (text, audio, image patches) into a single, shared embedding space. A massive Transformer backbone then processes these tokens simultaneously, learning deep cross-modal interactions from the first layer.

## Architecture Diagram
```mermaid
graph LR
    A[Text] --> D[Shared Tokenizer / Patchifier]
    B[Audio] --> D
    C[Image] --> D
    D --> E[Massive Unified Transformer]
    E --> F[Cross-Modal Output]
```
""",
    "cross-modal-alignment.md": """# Cross-Modal Alignment

## Overview
Cross-modal alignment focuses on establishing a direct correspondence between elements of different modalities. A classic example is grounding text phrases to specific bounding boxes in an image or linking spoken words to temporal video frames.

## Architecture Diagram
```mermaid
graph TD
    A[Audio Stream: 'Dog barking'] --> C[Alignment Function]
    B[Video Stream: Dog on screen] --> C
    C --> D[Mapped Temporal Correspondences]
```
""",
    "cross-attention-fusion.md": """# Cross-Attention Fusion

## Overview
In cross-attention fusion, the self-attention mechanism of Transformers is extended across modalities. One modality acts as the Query, while the other provides the Keys and Values, allowing one stream of information to conditionally process the other.

## Architecture Diagram
```mermaid
graph LR
    A[Text Tokens: Query] --> C[Cross-Attention Layer]
    B[Image Patches: Key/Value] --> C
    C --> D[Contextualized Output Tokens]
```
""",
    "cross-modal-generation.md": """# Cross-Modal Generation (Translation)

## Overview
Cross-modal generation is the process of translating information from one modality to entirely generate data in another modality. Prominent examples include Text-to-Image synthesis using Diffusion models and Image-to-Text generation for captioning.

## Architecture Diagram
```mermaid
graph LR
    A[Text Prompt] --> B[Text Encoder]
    B --> C[Diffusion Model / Generator]
    C --> D[Generated Image]
```
""",
    "early-fusion.md": """# Early Fusion (Input-Level)

## Overview
Early fusion integrates multi-modal data at the input level by concatenating raw features or initial embeddings before they are processed by the main deep learning model.

## Architecture Diagram
```mermaid
graph TD
    A[Modality 1 Features] --> C(Concatenation)
    B[Modality 2 Features] --> C
    C --> D[Joint Neural Network]
    D --> E[Predictions]
```
""",
    "late-fusion.md": """# Late Fusion (Decision-Level)

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
""",
    "intermediate-fusion.md": """# Intermediate / Hybrid Fusion

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
""",
    "omni-channel-assistants.md": """# Omni-Channel Conversational Assistants

## Overview
Modern conversational agents can simultaneously process real-time audio, text, and visual inputs, producing synthesized audio and text responses fluidly without explicit pipelining steps like ASR or TTS.

## Architecture Diagram
```mermaid
graph LR
    A[Camera Feed] --> D[Unified Multimodal Agent]
    B[Microphone] --> D
    C[Text Chat] --> D
    D --> E[Voice Synthesis]
    D --> F[Text Output]
```
""",
    "autonomous-vehicle-perception.md": """# Autonomous Vehicle Perception Stacks

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
""",
    "multimodal-medical-diagnostics.md": """# Multimodal Medical Diagnostics

## Overview
In healthcare, patient records are highly multimodal. By combining structured EHR tables, raw clinical notes, genomic data, and medical imaging (like MRIs or X-Rays), diagnostic systems can achieve far greater accuracy.

## Architecture Diagram
```mermaid
graph LR
    A[MRI Scan] --> D[Multimodal Diagnostics Model]
    B[Clinical Notes] --> D
    C[Genomic Sequences] --> D
    D --> E[Diagnosis & Prognosis]
```
"""
}

for name, content in pages.items():
    with open(os.path.join(pages_dir, name), "w", encoding="utf-8") as f:
        f.write(content)
print("Generated 12 pages.")
