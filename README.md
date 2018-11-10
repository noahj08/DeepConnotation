# DeepConnotation
A classifier that recognizes emotions in non-facial images. A collaboration between three Stanford students: Noah Jacobson, Katherine Kowalski, and Hasna Rtabi.

# Important implementation details for project milestone

## What we have
We currently have one model, a fractal CNN that takes an image as an input and directly outputs a classification by emotion. In the ipynb file I uploaded, there is a link to a paper which describes the advantages of a fractal CNN in great detail. Definitely look over that when writing the milestone. I chose to use a fractal net mainly because we don't have a ton of data, and fractal nets allow you to create very deep neural networks without losing the ability to itentity map. There are a lot of other advantages of fractal nets that you can find in the paper (for example, I think they might be smaller than resnets).

We haven't actually ran it and got results so we should probably do that.

## What we plan to make for our other models

### Model 1:

This is our more "vanilla" transfer learning model. We want to take the activation of the final layer in a neural net that's meant to caption images and connect it to a new FC softmax layer which we will train and use to classify the emotions. Using the activation from the other neural net allows for transfer learning, since the other net will have been trained on a much larger dataset of images.

### Model 2:

This model is a bit more complicated, but not by much. Before captioning our images, the repo will output an encoding for the image (the network passes that encoding through another NN to get the captions). We are going to take that image encoding and connect it to 1-2 FC layers in order to get our softmax output for emotion classification. Again, this gives us the same benefits of transfer learning, this time with a bit more end-to-end control.

That should be everything, Kathrene can explain the data side of things, call with questions :)
