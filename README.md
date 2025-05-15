# CISC 5800 Machine Learning Final Project

## Overview

This project aims to replicate many existing software that recognize handwritten digits, Latin letters, Greek letters, and mathematical symbols that can be used to evaluate mathematical problems accurately. Part 1 of the project was to load the data and use one of the simpler ML models to classify the symbols in the combined dataset. The ML model used for this is Random Forest. Part 2 of the project was to develop a PDF extractor that would extract individual symbols and then developing a CNN model that would identify the symbols correctly/incorrectly and then rebuild the equations to then evaluate them.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Model Details](#model-details)
- [Results](#results)
- [Acknowledgments](#acknowledgments)

## Project Structure

```plaintext
├── data
│   ├── EMNIST
│   ├── GREEK
│   ├── MATH
│   ├── MNIST
│   └── PDFS
├── output
│   ├── pages
│   ├── symbols
│   └── ...png
├── inverter.py
├── label_mapping.pkl
├── labels_2.csv
├── labels.csv
├── part_1.ipynb
├── part_2.ipynb
├── pdf_reader.ipynb
└── trained_symbol_cnn.pth
```


- `data/`: Contains CSV files with labels for training and evaluation.
- `output/`: Directory for storing output files generated during processing.
- `inverter.py`: Script for inverting images, useful for preprocessing.
- `label_mapping.pkl`: Pickle file mapping labels to class indices.
- `part_1.ipynb`: Notebook for data preprocessing and initial exploration.
- `part_2.ipynb`: Notebook for model training and evaluation.
- `pdf_reader.ipynb`: Notebook for extracting symbols from PDF files.
- `trained_symbol_cnn.pth`: Saved PyTorch model weights.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jbierowiec/CISC_5800.git
   cd CISC_5800
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage 

1. Data Preprocessing
- Use part_1.ipynb to preprocess the data. This includes loading the CSV files, cleaning the data, and preparing it for model training.
2. Model Training and Evaluation
- Execute part_2.ipynb to train the CNN model on the preprocessed data. This notebook includes model architecture, training loops, and evaluation metrics.
3. PDF Symbol Extraction
- Utilize pdf_reader.ipynb to extract symbols from PDF documents. This notebook demonstrates how to process PDFs and prepare the extracted symbols for classification.
4. Image Inversion
- Run inverter.py to invert images as part of the preprocessing pipeline.

   ```bash
   python inverter.py --input_dir path/to/images --output_dir path/to/output
   ```

- Replace path/to/images and path/to/output with your actual directories.

## Model Details

- Architecture: Convolutional Neural Network (CNN)
- Framework: PyTorch
- Input: Preprocessed images of symbols
- Output: Predicted class labels for each symbol

The trained model is saved as trained_symbol_cnn.pth and can be loaded for inference.

## Results

Unfortunately the model has very poor accuracy with it being 2%. This may be based on the fact that the model has 500 samples, but only 10 epochs were used to train the model which is not enough to build an accurate model. Other issues can involve the current cnn architecture. The model did manage to reconstruct the correct number of symbols when trying to evaluate them, however a mix of Latin lowercase and uppercase letters were outputted without Greek letters, digits or mathematical symols being used, which should have been in the output. 

## Acknowledgments

This project although does not work fully, has the potential of being refactored and worked on to reach a point where the uploaded PDF files, and symbol extraction is correctly or near correctly identified. This is a future improvement and next step to continue the project. 
