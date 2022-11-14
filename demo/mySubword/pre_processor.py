# import jieba
# in_path = "news.2021.zh.txt"
# out_path = "news.zh.txt"
# fp_out = open(out_path, "w", encoding="utf-8")
# for line in open(in_path, "r", encoding="utf-8").readlines():
#     new_line = " ".join(jieba.lcut(line))
#     fp_out.write(new_line)

import re
tag = re.compile(u"[^\uac00-\ud7ffa-zA-Z0-9]")
spaces_pun = re.compile(r"[ ]+")


def pre_ko(text):
    res = re.sub(tag, lambda x: " " + x.group() + " ", text)
    res = re.sub(spaces_pun, " ", res)
    return res

in_path = "news.2021.ko"
out_path = "news.ko.txt"
fp_out = open(out_path, "w", encoding="utf-8")
for line in open(in_path, "r", encoding="utf-8").readlines():
    new_line = pre_ko(line)
    new_line = new_line.replace("\n ", "\n")
    fp_out.write(new_line)
    fp_out.flush()