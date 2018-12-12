# DeepConnotation
A classifier that recognizes emotions in non-facial images. A collaboration between three Stanford students: Noah Jacobson, Katherine Kowalski, and Hasna Rtabi.

# Important implementation details

## Models
There are four models in this repository. The first is a fractal CNN that takes an image as an input and directly outputs a classification by emotion, found in fractal_CNN.ipynb. In the ipynb file I uploaded, there is a link to a paper which describes the advantages of a fractal CNN in great detail. I chose to use a fractal net mainly because we don't have a ton of data, and fractal nets allow you to create very deep neural networks without losing the ability to itentity map. However, the fractal net approach did not work due to slow training and exploding gradients, so I also created resnet.ipynb, which is very similar to the fractal code, except the implementation is for a residual convolutional neural network.

The file "Data.ipynb" contains code to load images from online and resize them to be (32x32x3).

The "labels.json" file contains Y-labels for input data

The "snapshots" folder contains some pre-trained weights.

# Feature Embedding & Multi-Class Classification Model

We adapted a caption generator pre-trained on the MSCOCO dataset[1] for 2MM iterations. We used the pretrained weights to input our 32x32x3 image vectors through a CNN and output a feature embedding of size 1024x1[2]. We then trained 90% of our feature embeddings on a 3 layer neural net (Linear->Relu->Linear->Relu->Linear->Softmax) to classify our images according to human emotional response. We used cross-entropy loss. We hypertuned our parameters of minibatch size, number of epochs, and learning rate. 

We tuned our hyperparameters by repeatedly running our feature embeddings through the 3 layer network, cross validated, graphed results, and detected the optimal value that minimized computational cost, meaning we chose 1000 over 1500 epochs, because they produced similar results, but reducing the number of epochs reduced the run time of our algorithm. 
Learning rate (alpha): 0.0001, number of epochs: 1000, minibatch size:64. 

To run this code:
## Requirements
tensorflow==1.6.0
requests==2.18.4

## Files
Data.ipynb	
labels.json	

caption_generator.py		//scripts for feature embedding
inference.py
model.py
___init__.py
run-dev.ipynb
run-train.ipynb
run-test.ipynb

Classification.ipynb	//classification script

## To run 
Refer to https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f
for instructions to understand the feature embedding, change paths to images within inference.py file and run-dev, run-test, run-train.
Run Classification.ipynb with feature embeddings. 



[1] Lin, T., Maire, M., Belongie, S., Bourdev, L., Girshick, R., Hays, J., Perona, P., Ramanan, D., Zitnick, C. and Dollár, P. (2018). Microsoft COCO: Common Objects in Context. [online] Arxiv.org. Available at: https://arxiv.org/abs/1405.0312 [Accessed 12 Dec. 2018].​
[2] Murray, C. (2018). Building an image caption generator with Deep Learning in Tensorflow. [online] freeCodeCamp.org. Available at: https://medium.freecodecamp.org/building-an-image-caption-generator-with-deep-learning-in-tensorflow-a142722e9b1f [Accessed 12 Dec. 2018].
[3] You, Q., Luo, J., Jin, H. and Yang, J. (2018). Building a Large Scale Dataset for Image Emotion Recognition: The Fine Print and The Benchmark. [online] Arxiv.org. Available at: https://arxiv.org/abs/1605.02677 [Accessed 12 Dec. 2018].
