import argparse
import tensorflow.compat.v1 as tf
from tensorflow.python.framework import graph_util
tf.disable_eager_execution()
"""
通过传入 CKPT 模型的路径得到模型的图和变量数据
通过 import_meta_graph 导入模型中的图
通过 saver.restore 从模型中恢复图中各个变量的数据
通过 graph_util.convert_variables_to_constants 将模型持久化
"""
def freeze_graph(arg):
    """

    """
    input_checkpoint, output_graph = arg.ckpt_path, arg.h5_path
    output_node_names = "embedding/embeddings"   # 输出的节点名称
    # 导入模型中的图
    saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=True)
    # 获取当前默认计算图。
    graph = tf.get_default_graph()
    input_graph_def = graph.as_graph_def()

    with tf.Session() as sess:
        #===================================
        file = open('./nodes.txt', 'a+')
        tensor_name_list = [tensor.name for tensor in graph.as_graph_def().node]
        for n in tensor_name_list:
           file.write(n + '\n')
        file.close()
        #===================================
        saver.restore(sess, input_checkpoint)
        output_graph_def = graph_util.convert_variables_to_constants(
            sess=sess,
            input_graph_def=input_graph_def,
            output_node_names=output_node_names.split(","))

        with tf.gfile.GFile(output_graph, "wb") as f:
            f.write(output_graph_def.SerializeToString())
        print("%d ops in the final graph." % len(output_graph_def.node))



arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("--ckpt_path", type=str, default="../../model/temp_model/test_model")
arg_parse.add_argument("--h5_path", type=str, default="../../model/temp_model/my_model.h5")
args = arg_parse.parse_args()
freeze_graph(args)