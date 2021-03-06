import numpy as np
import numpy.linalg as LA
import gensim
from corpus2vocab import read_vocab
import setting as st
import sys

#since the embedding words set equals the context words set in my experiment,
#I just use embedding words to form D_1 and D_2
def vec2pairs(src_mono_vec, trg_mono_vec):
    print("loading source vectors")
    src_vectors = gensim.models.KeyedVectors.load_word2vec_format(src_mono_vec, binary = False)
    print("loading target vectors")
    trg_vectors = gensim.models.KeyedVectors.load_word2vec_format(trg_mono_vec, binary = False)
    src_word = 'magnesium'
    trg_words = ['钒', '氧', '乳化剂', '烃类', '铊', '铷', '甲烷', '还原剂', '钴', '单质', '铋', '树脂', '石蜡', '铂', '钽', '润滑剂', '氯化氢', '硝酸盐', '硅胶', '氮气', 
    '碱性', '挥发性', '碘', '碳酸钙', '过氧化氢', '氰化钾', '硫', '乙烯', '稳定剂', '乙醚', '钙', '氢氧化钠', '钨', '硼酸', '阻燃剂', '氟化物', '甲苯', '氢氧化物', '硒', 
    '矽', '丙烷', '钼', '锑', '溶剂', '氢氟酸', '甲醇', '石墨', '氯化钙', '砷', '丙烯', '氯化钾', '电解质', '氨', '甲醛', '碳酸钠', '氨气', '硫化物', '液态', '氢氧化钾', 
    '钛', '铌', '硫化氢', '锶', '锌', '硫酸盐', '杂质', '钠', '镉', '氯化物', '硅', '氧化剂', '镁', '锂', '碳酸盐', '汞', '氧化物', '氧化铁', '锰', '氯化钠', '混合物', 
    '铝', '二氧化硫', '氯仿', '铅', '铬', '镍', '氢气', '盐酸', '锆', '乙醇', '锗', '丙酮', '一氧化碳', '二氧化硅', '钾', '磷酸盐', '硫酸', '硝酸', '氯气', '碳氢化合物']

    print(src_word)

    sum = 0.0
    a = LA.norm(src_vectors[src_word])
    for word in trg_words:
        b = LA.norm(trg_vectors[word])
        sum += src_vectors[src_word].dot(trg_vectors[word]) / a / b
    print(sum / len(trg_words))

    sum = 0.0
    for word1 in trg_words:
        a = LA.norm(trg_vectors[word1])
        for word2 in trg_words:
            if word1 == word2:
                continue
            b = LA.norm(trg_vectors[word2])
            sum += trg_vectors[word1].dot(trg_vectors[word2]) / a / b
    print(sum / len(trg_words) / (len(trg_words) - 1))
    
if __name__ == "__main__":
    src_vec = sys.argv[1] if len(sys.argv) > 1 else "../../word2vec/mapped.2en"
    trg_vec = sys.argv[2] if len(sys.argv) > 2 else "../../word2vec/mapped.2zh"

    vec2pairs(src_vec, trg_vec)

    
