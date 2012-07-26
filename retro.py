import os

from db import *
from spamfilter import *
from email_util import *
from text_parser import *
from util import *
db = get_db()
class TextStat(object):
    def __init__(self,fp,cat):
        tokens = get_tokens_from_fp(fp)
        self.tokens = tokens 
        self.body = Email(fp).get_body()
        f_arr = map(f,tokens)
        self.tok_spam_stat = sorted(zip(tokens, f_arr), key = lambda x:x[1])
        self.tok_ham_stat = sorted(zip(tokens,map(lambda x:1 - x,f_arr )), key = lambda x:x[1])
        
        self.spamicity = cal_spamminess(tokens)
        self.hamicity = cal_hamminess(tokens)
        self.I = get_I(tokens)
        
    def __getattr__(self,attr):
        cat,cnt,order = attr.split("_")
        cnt = int(cnt)
        if cat == "ham":
            data = self.tok_ham_stat
        else:
            data = self.tok_spam_stat
            
        if order == "desc":
            tmp = reversed(data)
            data = [i for i in tmp]
        for i in data[:cnt]:
            print "%s%s: %f" %(i[0][0].ljust(10),i[0][1].ljust(5),i[1])

        return data[:cnt]

if __name__ == "__main__":

    root_dir = "/home/xiaohan/code/spam-filter/2005-Jun/data/ham"
    path = os.path.join(root_dir ,"6504")
    ts = TextStat(path ,"ham")
    print ts.body
    print  ts.spam_10_desc
    print  ts.ham_10_desc
    print ts.I
