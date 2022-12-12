import tensorflow.compat.v1 as tf
import argparse
import h5py
"""
使用 tf.train.saver() 保存模型时会产生多个文件，会把计算图的结构和图上参数取值分成了不同的文件存储。这种方法是在TensorFlow中是最常用的保存方式。
"""


def convert(arg):
    new_check = tf.train.NewCheckpointReader(arg.ckpt_path)
    f = h5py.File(arg.h5_path, "w")
    for key in sorted(new_check.get_variable_to_shape_map()):
        # 权重名称需根据自己网络名称自行修改
        if key.endswith('w') or key.endswith('biases'):
            keySplits = key.split(r'/')
            keyDict = keySplits[1] + '/' + keySplits[1] + '/' + keySplits[2]
            f[keyDict] = new_check.get_tensor(key)


arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("--ckpt_path", type=str, default="../../model/temp_model/test_model")
arg_parse.add_argument("--h5_path", type=str, default="../../model/temp_model/new_model.h5")
args = arg_parse.parse_args()
convert(args)