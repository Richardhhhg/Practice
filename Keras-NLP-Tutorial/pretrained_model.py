import os
import keras_nlp
import keras
os.environ['KERAS_BACKEND'] = 'jax'


keras.mixed_precision.set_global_policy('mixed_float16')

BATCH_SIZE = 16
imdb_train = keras.utils.text_dataset_from_directory(
    "aclImdb/train",
    batch_size=BATCH_SIZE
)

imdb_test = keras.utils.text_dataset_from_directory(
    "aclImdb/test",
    batch_size=BATCH_SIZE
)