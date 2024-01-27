# Semantic Entity Recognition of Handwritten Images using LayoutLMv3

This project focuses on extracting information from images and saving it in a JSON key-value pair format.

## Prerequisites

Ensure you have the following dependencies installed:

- PyTorch
- torchvision

## Dataset Creation and Labelling

This project requires a handwritten dataset. You can use the dataset example in [`handwritten-layoutlmv3/dataset/`](./dataset/). Follow these steps if you want create and label your dataset:

1. Collect handwritten samples for your dataset.
2. Install and set up Label Studio.
3. Import your collected samples into Label Studio.
4. Label the samples according to your project requirements.

Ensure the dataset is properly labeled and saved in a format compatible with the OCR models used in this project.

## Installation

1. Clone this repository.
2. Download the model and place it in the appropriate folder ([Dowload Model](https://drive.google.com/file/d/1b-Jyf6PVzE-zcfHFfEsG8wP6XsRf5SQ9/view?usp=sharing)).
3. Run the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```
Note: Make sure to install PyTorch and torchvision before running pip install.

## Usage

Run `python convert_anno.py` first to convert the previous annotation format to the appropriate format.
Run `python src/main.py` for training. Make sure the number of classes matches the annotation and the model architecture.
Run `python src/inference.py` to perform inference. Adjust the image path and classes before running and comment out the loss function on the trainer to prevent errors during forward propagation.

## Limitations

While this project has demonstrated promising results, there are a few limitations to note:

- The bounding box predictions from the trained model may not always be accurate. This could lead to errors in text detection and subsequently in the recognition and extraction of information.
- The extraction of information into a JSON key-value pair format currently relies on manual logic. This may not be robust to variations in the data and could limit the scalability of the project.

These limitations present opportunities for future improvements and refinements to the project.
