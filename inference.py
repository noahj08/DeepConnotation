from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
import math
import os
import numpy as np
import tensorflow as tf

# from caption_generator import CaptionGenerator
# from model import ShowAndTellModel
# from vocabulary import Vocabulary
from medium_show_and_tell_caption_generator.caption_generator import CaptionGenerator
from medium_show_and_tell_caption_generator.model import ShowAndTellModel
# from medium_show_and_tell_caption_generator.vocabulary import Vocabulary

FLAGS = tf.app.flags.FLAGS 

model_path_ = r"C:\Users\kathe\Documents\CS230\project\caption\medium-show-and-tell-caption-generator\etc\show-and-tell.pb"

# logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger(__name__)


def main(input_files_):
    input_files = input_files_
    model = ShowAndTellModel(model_path_) #tf.app.flags.model_path)) #
#     vocab = Vocabulary(vocab_file_)#tf.app.flags.vocab_file
    filenames = _load_filenames(input_files_)

    generator = CaptionGenerator(model)#, vocab)
    encodings=[];
    first = True
    for filename in filenames:
        with tf.gfile.GFile(filename, "rb") as f:
            image = f.read()
            encoding = generator.beam_search(image);
            if(first):
                encodings = encoding
                first=False
            else:
                encodings = np.concatenate((encodings, encoding),axis=0)
    return encodings

def _load_filenames(input_files):
    filenames = []
    for file_pattern in [input_files]:
        filenames.extend(tf.gfile.Glob(file_pattern))
#     logger.info("Running caption generation on %d files matching %s",
#                 len(filenames), input_files)
    return filenames


if __name__ == "__main__":
    tf.app.run()
