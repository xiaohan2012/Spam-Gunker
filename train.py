# coding=utf-8
import time

from db import *
from text_parser import *
from time_measure import *
db = get_db("sb_all")
def build_index():
    col_opts = {
                 "ham_token":[("t_id",pymongo.ASCENDING)],
                 "spam_token":[("t_id",pymongo.ASCENDING)],
                 "spam_token":[("word",pymongo.ASCENDING),("pos",pymongo.ASCENDING)],
                 "ham_token":[("word",pymongo.ASCENDING),("pos",pymongo.ASCENDING)],
                 "trained_spam_text":[("t_id",pymongo.ASCENDING)],
                 "trained_ham_text":[("t_id",pymongo.ASCENDING)],
                 "trained_ham_set":[("t_id",pymongo.ASCENDING)],
                 "trained_spam_set":[("t_id",pymongo.ASCENDING)],
                }
    for col,opts in col_opts.items():
        db[col].ensure_index(opts,unique = True)

def clean_db():
    col_names = ["spam_text","spam_token","ham_text","ham_token","trained_spam_text","trained_ham_text"]
    for coln in col_names:
        db[coln].remove({})

@measure_time
def register(category , text, t_id):
    parsed_text = parse_text(text)#parse text and get the raw parsed string
    t_ = {"text":text,"tokens":[],"t_id":int(t_id)}
    
    #tokenize the raw parsed string
    for word,pos in tokenize(parsed_text):
        t_["tokens"].append({"w":word,"p":pos})
            
    #save text
    db[category + "_text"].save(t_)
    #print "newly saved text id:",t_id

    #save tokens
    col_name = category + "_token"
    for word,pos in tokenize(parsed_text):
        tok = db[col_name].find_one({"word":word,"pos":pos})
        if tok:
            #print "token find:",tok
            db[col_name].update({"word":word,"pos":pos},{"$addToSet":{"text_set":t_id}})
        else:
            #print "token not found, create it"
            tok = {"word":word,"pos":pos,"text_set":[t_id]}
            db[col_name].save(tok)
    #updating trained set respectively
    db["trained_%s_set" %category].save({"t_id":int(t_id),"when":time()})
if __name__ == "__main__":
    clean_db()

    register("spam","seemsspam")
    register("spam","spam")
    register("ham","ham")
    register("ham","seemsspam")
