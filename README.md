---
license: mit
metrics:
- accuracy
- f1
pipeline_tag: image-classification
---

Recently, someone asked me if you can classify dog images into their respective dog breeds instead just differentiating from cats vs dogs like my last [notebook](https://www.kaggle.com/code/wesleyacheng/cat-vs-dog-image-classification-with-cnns). I say **YES**!

Due to the complexity of the problem, we will be using the most advanced computer vision architecture released in the [2020 Google paper](https://arxiv.org/pdf/2010.11929v2.pdf), the [**Vision Transformer**](https://paperswithcode.com/methods/category/vision-transformer).

The difference between the **Vision Transformer** and the traditional **Convolutional Neural Network (CNN)** is how it treats an image. In **Vision Transformers**, we take the input as a patch of the original image, say 16 x 16, and feed in into the Transformer as a sequence with positional embeddings and self-attention, while in the **Convolutional Neural Network (CNN)**, we use the same patch of original image as an input, but use convolutions and pooling layers as inductive biases. What this means is that **Vision Transformer** can use it's judgement to attend any particular patch of the image in a *global* fashion using it's self-attention mechanism without having us to guide the neural network like a **CNN** with *local* centering/cropping/bounding box our images to help its convolutions. 

This allows the **Vision Transformer** architecture to be more flexible and scalable in nature, allowing us to create [foundation models](https://blogs.nvidia.com/blog/2023/03/13/what-are-foundation-models) in computer vision, similar to the NLP foundational models like [BERT](https://paperswithcode.com/method/bert) and [GPT](https://paperswithcode.com/method/gpt), with pre-training self-supervised/supervised on massive amount of image data that would generalize to different computer vision tasks such as *image classification, recognition, segmentation, etc.* This cross-pollination helps us move closer towards the goal of Artificial General Intelligence.

One thing about **Vision Transformers** are it has weaker inductive biases compared to **Convolutional Neural Networks** that enables it's scalability and flexibility. This feature/bug depending on who you ask will require most well-performing pre-trained models to require more data despite having less parameters compared to it's CNN counterparts.

Luckily, in this model, we will used a **Vision Transformer** from [Google hosted at HuggingFace](https://huggingface.co/google/vit-base-patch16-224-in21k) pre-trained on the [ImageNet-21k dataset](https://paperswithcode.com/paper/imagenet-21k-pretraining-for-the-masses) (14 million images, 21k classes) with 16x16 patches, 224x224 resolution to bypass that data limitation. We will be fine-tuning this model to our "small" dog breeds dataset of around 20 thousand images from the [Stanford Dogs dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/) imported by Jessica Li into [Kaggle](https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset) to classify dog images into 120 types of dog breeds!

