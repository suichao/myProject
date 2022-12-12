import tensorflow.compat.v1 as tf
import numpy as np
import os
# 在Tensorflow 2.0 中，eager execution 是默认开启的。所以，需要先关闭eager execution
tf.disable_eager_execution()
seq_len = 10
vocab_size = 500
embedding_dim = 128

inputs = tf.keras.Input(seq_len,)
x = tf.keras.layers.Embedding(vocab_size, embedding_dim)(inputs)
x = tf.keras.layers.Dense(100, activation="relu")(x)
x = tf.keras.layers.Dense(100, activation="relu")(x)
x = tf.keras.layers.Flatten()(x),
x = tf.keras.layers.Softmax(2)(x)
model = tf.keras.models.Model(inputs, x)
model.summary()

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=['accuracy']
)
# x_input = tf.convert_to_tensor(
#     np.reshape(np.random.randint(0, 500, 100), (10, 10))
# )
x_input = tf.random_uniform(shape=(10, 10), minval=0, maxval=500, dtype=tf.int32)
# with tf.Session() as sess:
#     x = sess.run(x_input)
#     print(x)

y_output = tf.convert_to_tensor(
    np.random.randint(0, 2, 10)
)

model.fit(x_input, y_output, epochs=2, batch_size=1, steps_per_epoch=4)


path = "../../model/temp_model"
if not os.path.exists(path):
    os.makedirs(path)
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.save(sess, os.path.join(path, "test_model"))