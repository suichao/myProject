import tensorflow.compat.v1 as tf  # 使用兼容1.x版本代码
"""
tf.gather（）
该接口的作用：就是抽取出params的第axis维度上在indices里面所有的index
 
tf.gather(
    params,
    indices,
    validate_indices=None,
    name=None,
    axis=0
)
"""

sample = tf.reshape(tf.range(49), [7, 7])
print(sample)
"""
tf.Tensor(
[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]
 [35 36 37 38 39 40 41]
 [42 43 44 45 46 47 48]], shape=(7, 7), dtype=int32)
 """

res = tf.gather(sample, [0, 2, 4])  # 取temp一维张量中第0，第2，第4的值形成一个tf张量
"""
tf.Tensor(
[[ 0  1  2  3  4  5  6]
 [14 15 16 17 18 19 20]
 [28 29 30 31 32 33 34]], shape=(3, 7), dtype=int32)
"""
