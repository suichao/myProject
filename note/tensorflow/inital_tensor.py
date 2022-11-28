# encoding=utf-8
import tensorflow.compat.v1 as tf

sess = tf.Session()  # 初始化Session

#  常数
'''
tf.constant(value, dtype=None, shape=None, name="Const"):
Args:
    value: 值，用列表或常数表示
    dtype: 类型
    shape: 形状
    name: 名字
'''
c1 = tf.constant([1., 2., 3.], dtype=tf.float32)  # 形状为3
c2 = tf.constant([1, 2, 3, 4], shape=[2, 2])  # 形状为2×2
print(sess.run(tf.shape(c2)))
'''
[2 2]
'''
print(sess.run(c2))
'''
[[1 2]
 [3 4]]
 '''

#  变量
'''
class tf.Variable()
Args:
    initial_value=None, 初始化的值，使用常数、序列或者随机数作为初始化的值
    trainable=True,
    collections=None,
    validate_shape=True,
    caching_device=None,
    name=None,
    variable_def=None,
    dtype=None,
    expected_shape=None,
    import_scope=None,
    constraint=None,
    use_resource=None,
    synchronization=VariableSynchronization.AUTO,
    aggregation=VariableAggregation.NONE):
'''
v = tf.Variable(c2)  # 使用常数初始化
v2 = tf.Variable(tf.range(10))  # 使用序列初始化
v3 = tf.Variable(tf.random_uniform([2, 3]))  # 使用随机数初始化
sess.run(tf.global_variables_initializer())  # 全局变量初始化器，sess.run变量之前必须要先初始化，否则会抛出变量未初始化的异常
print(sess.run(v3))
'''
[[0.31143284 0.53024447 0.0968231 ]
 [0.1862328  0.68729246 0.89440215]]
'''

# tf.get_variable()
'''
tf.get_variable(
        name,
        shape=None,
        dtype=None,
        initializer=None,
        regularizer=None,
        trainable=None,
        collections=None,
        caching_device=None,
        partitioner=None,
        validate_shape=True,
        use_resource=None,
        custom_getter=None,
        constraint=None,
        synchronization=VariableSynchronization.AUTO,
        aggregation=VariableAggregation.NONE)
Args:
    name: 变量名，必须
    shape: 形状
    dtype: 类型
    initializer: 初始化器
'''
emb_v2 = tf.get_variable(shape=[20000, 20, 8],
                         initializer=tf.random_normal_initializer(), name='emb_v2')

#  占位符
'''
tf.placeholder(dtype, shape=None, name=None):
Args:
    dtype: 类型
    shape: 形状，None表示这一维可以接受任意输入
    name: 名称
'''
x = tf.placeholder(tf.float32, [None, 500])  # 一般第一维设置为none，表示batch

#  序列
'''
tf.range(start, limit=None, delta=1, dtype=None, name="range")
'''
tf.range(10)  # [0 1 2 3 4 5 6 7 8 9]
r2 = tf.range(10, 0, -2)
print(sess.run(r2))
'''
[10  8  6  4  2]
'''

# tf.ones()
'''
tf.ones(shape, dtype=dtypes.float32, name=None)
'''
tf.ones([3, 5])

# tf.onrs_like()
'''
tf.ones_like(tensor, dtype=None, name=None, optimize=True)
'''
tf.ones_like(r2)  # 生成和r2形状一样的全是1的张量

# 随机数
'''
tf.random_normal(shape,
                mean=0.0,
                stddev=1.0,
                dtype=dtypes.float32,
                seed=None,
                name=None)
Args:
    shape: 形状
    mean=0.0: 均值，默认为0
    stddev=1.0: 标准差，默认为1
    dtype: 类型，默认tf.float32
    seed=None: 随机种子
    name=None: 名称
'''
r = tf.random_normal([3, 5], stddev=0.1)  # 生成的随机数服从均值0，标准差0.1的正态分布
print(sess.run(r))
'''
[[-0.10203493 -0.08492908 -0.12519914  0.1285079  -0.09017794]
 [-0.11248418  0.00505971  0.10674645 -0.09033418  0.02617419]
 [ 0.01536902 -0.08910552  0.10969975  0.10016834 -0.03961685]]
'''

r = tf.truncated_normal([3, 5], stddev=0.1)  # 与均值相差超过2个标准差的会被丢弃重新生成
print(sess.run(r))
'''
[[ 0.10411328 -0.19037913  0.05412641  0.01675856 -0.03939838]
 [ 0.0683771  -0.00904175  0.00975604  0.13849497  0.11131003]
 [ 0.09745935  0.09535291 -0.0058706   0.01729187  0.04007868]]
'''

# tf.random_uniform()
'''
tf.random_uniform(shape,
                  minval=0,
                  maxval=None,  # 最大值是取不到的
                  dtype=dtypes.float32,
                  seed=None,
                  name=None)
'''
r = tf.random_uniform([2, 3], 1, 7, tf.int32)  # 相当于掷6次骰子
print(sess.run(r))
'''
[[6 1 3]
 [5 1 2]]
'''