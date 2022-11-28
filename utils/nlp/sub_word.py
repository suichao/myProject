import jieba
import re
from subword_nmt import apply_bpe


class SubWordBase(object):
    """

    """
    def __init__(self, bpe_path, vocab_path):
        self._bpe = apply_bpe.BPE(open(bpe_path, "r", encoding="utf-8"))
        self.vocab_path = vocab_path
        self.UNK = "UNK"
        self.t2ids, self.ids2t = self._init_vocab()

    def _cut(self, text):
        raise NotImplementedError

    def _init_vocab(self):
        w2ids, ids2w = {}, {}
        for i, w in enumerate(open(self.vocab_path, "r", encoding="utf-8").readlines()):
            word = w.split()[0]
            w2ids[word] = i
            ids2w[i] = word
        unk = self.UNK
        unk_id = len(w2ids) + 1
        w2ids[unk] = unk_id
        ids2w[unk_id] = unk
        return w2ids, ids2w

    def text2token(self, text):
        new_text = " ".join(self._cut(text))
        token_text = self._bpe.process_line(new_text)
        return token_text.split()

    def token2ids(self, tokens):
        ids = []
        for w in tokens:
            try:
                _id = self.t2ids[w]
            except KeyError:
                _id = self.t2ids[self.UNK]
            ids.append(_id)
        return ids

    def ids2token(self, ids):
        tokens = []
        for _id in ids:
            token = self.ids2t[_id]
            tokens.append(token)
        return tokens

    def text2ids(self, text):
        return self.token2ids(self.text2token(text))

    def ids2text(self, ids):
        return "".join(self.ids2token(ids)).replace("@@", "")


class ZhSubWord(SubWordBase):
    def __init__(self, bpe_path, vocab_path):
        super(ZhSubWord, self).__init__(bpe_path, vocab_path)

    def _cut(self, text):
        return jieba.lcut(text)


class KoSubWord(SubWordBase):
    def __init__(self, bpe_path, vocab_path):
        super(KoSubWord, self).__init__(bpe_path, vocab_path)
        self.ko_tag = re.compile(u"[^\uac00-\ud7ffa-zA-Z0-9]")
        self.spaces_pun = re.compile(r"[ ]+")

    def _cut(self, text):
        text = re.sub(self.ko_tag, lambda x: " " + x.group() + " ", text)
        res = re.sub(self.spaces_pun, " ", text)
        return res

if __name__ == '__main__':
    sw = KoSubWord("../../demo/mySubword/bpe.zh", "../../demo/mySubword/vocab.zh")
    res = sw.text2ids("越是拥抱变化，生活才能越自在。")
    print(res)
    line = sw.ids2text(res)
    print(line)
