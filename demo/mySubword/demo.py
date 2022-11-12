from utils.nlp.sub_word import ZhSubWord
sw = ZhSubWord("bpe.zh", "vocab.zh")
line = "越是拥抱变化，生活才能越自在。"
res = sw.text2token(line)
print(res)
res = sw.text2ids(line)
print(res)
line = sw.ids2text(res)
print(line)