from db import *
from spamfilter import get_I , cal_probs_nb
from util import *
from os.path import join

db = get_db()

if __name__ == "__main__":
    test_size = 5000
    chi_collect_name = "improved_chi_test_result"
    nb_collect_name = "improved_nb_test_result"
    db[chi_collect_name].remove()
    db[nb_collect_name].remove()
    path = "/home/xiaohan/code/spam-filter/2005-Jun/data/ham"
    counter = 0
    db[chi_collect_name].ensure_index([("t_id",pymongo.ASCENDING)])
    db[nb_collect_name].ensure_index([("t_id",pymongo.ASCENDING)])
    for fn in get_files_in_dir(path):
        if counter == test_size:
            break
        #not trained
        fp = join(path,fn)
        print fp
        try:
            tokens = get_tokens_from_fp(fp)
            I = get_I(tokens)
            db[chi_collect_name].save({"real_cat":"ham","I":I,"t_id":int(fn)})
            print "HAM's spamminess using chi: %f\n" %I
            
            I = cal_probs_nb(tokens)
            db[nb_collect_name].save({"real_cat":"ham","I":I,"t_id":int(fn)})
            print "HAM's spamminess using naive bayes: %f\n" %I

            counter += 1
        except UnicodeDecodeError:
            print "decode error"

    path = "/home/xiaohan/code/spam-filter/2005-Jun/data/spam"
    counter = 0
    for fn in get_files_in_dir(path):
        if counter == test_size:
            break
        #not trained
        fp = join(path,fn)
        print fp
        try:
            tokens = get_tokens_from_fp(fp)
            I = get_I(tokens)
            db[chi_collect_name].save({"real_cat":"spam","I":I,"t_id":int(fn)})
            print "SPAM's spamminess using chi: %f\n" %I
            
            I = cal_probs_nb(tokens)
            db[nb_collect_name].save({"real_cat":"spam","I":I,"t_id":int(fn)})
            print "SPAM's spamminess using naive bayes: %f\n" %I

            counter += 1
        except UnicodeDecodeError:
            print "decode error"
