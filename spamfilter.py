# coding=utf-8
from operator import mul
from math import log,exp
from types import GeneratorType
from numpy import array , log , exp, sort

from db import *
from chi import *
db = get_db()

def b(w,p):
    w_stat = db["spam_token"].find_one({"word":w,"pos":p})
    num = len(w_stat["text_set"]) if w_stat else 0
    return ( 1 + num ) / ( float(db["spam_text"].find().count()) + 2 )

def g(w,p):
    w_stat = db["ham_token"].find_one({"word":w,"pos":p})
    num = len(w_stat["text_set"]) if w_stat else 0
    return ( 1 + num ) / ( float(db["ham_text"].find().count()) + 2 )

def p(w,p):
    return b(w,p) / ( b(w,p) + g(w,p) )

def n():
    return db["spam_text"].find().count() + db["ham_text"].find().count()

def f(i):
    w,p_ = i
    s = 1
    x = .5
    n_ = n()
    return ( (s * x) + ( n_ * p(w,p_) ) ) / (s + n_)

def cal_spamminess(tokens):
    probs = map(f,tokens)
    #print probs
    return comb_probs(probs)

def cal_hamminess(tokens):
    probs = map(lambda x: 1 - x , map(f,tokens))
    #print probs
    return comb_probs(probs)

def comb_probs(probs):
    #probs = sort(array(probs))[50:0:-1]
    return chi2P( -2 * sum(log(probs)),len(probs) * 2)

def get_I(tokens):
    ham = cal_hamminess(tokens)        
    spam = cal_spamminess(tokens)
    print "hamminess:%f,spamminess:%f" %(ham,spam)
    return (1 +  spam - ham ) / 2.

def cal_probs_nb(tokens):
    probs = array(map(f,tokens))
    h = sum(log(1 - probs) - log(probs))
    return 1 / ( 1 + exp(h))

if __name__ == "__main__":
    print db.spam_token.find_one({"word":"算是","pos":"v"})
