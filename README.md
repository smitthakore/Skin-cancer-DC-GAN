# Skin Lesion Synthesis with DCGAN
GAN-based Image Augmentation For  Skin Cancer Classification
## Overview

The Skin Lesion Synthesis with DCGAN project explores the generation of realistic images of skin lesions using a Deep Convolutional Generative Adversarial Network (DCGAN). Leveraging data scraped from diverse online sources, this project aims to showcase the potential of DCGANs in generating synthetic images that closely resemble real skin lesions. Additionally, the project integrates the VGG-19 model for skin cancer classification, providing a comprehensive solution for both image synthesis and classification tasks.

## Key Components

1. **DCGAN for Image Synthesis:**
   - The DCGAN architecture is employed to generate lifelike images of skin lesions.
   - The model is trained on a dataset compiled from Skincancer MNIST: HAM10000 hosted on kaggle.
   - The goal is to demonstrate that even with a small dataset, DCGANs can produce high-quality synthetic images useful for research and training.

2. **Data Collection:**
   - Data scraping techniques were utilized to gather a diverse set of skin lesion images from online sources.
   - The dataset includes various skin lesion types, providing a comprehensive training set for the DCGAN.
   - The primary dataset used for this project is available on Kaggle: [Skin Cancer MNIST (HAM10000)](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000).
   

3. **VGG-19 for Classification:**
   - The VGG-19 model, known for its effectiveness in image classification, is employed to classify skin cancer in the generated and real images.
   - The integration of classification enhances the utility of the project, allowing users to not only generate synthetic images but also assess their potential clinical relevance.
     
4. **Frontend Website:**
   - The project includes a frontend website that runs locally using HTML and CSS.
   - Explore the `frontend` directory to find the HTML and CSS files for the user interface.
   - Launch the website on your local machine to interact with the generated images and classification results.

5. **Backend with Flask:**
   - The backend is powered by Flask, a lightweight web framework for Python.
   - The Flask application handles requests from the frontend and interacts with the DCGAN and VGG-19 models to provide image synthesis and classification results.

