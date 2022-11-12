import jieba
in_path = "news.2021.zh.txt"
out_path = "news.zh.txt"
fp_out = open(out_path, "w", encoding="utf-8")
for line in open("news.2021.zh.txt", "r", encoding="utf-8").readlines():
    new_line = " ".join(jieba.lcut(line))
    fp_out.write(new_line)