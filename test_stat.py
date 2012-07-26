# coding=utf-8
from db import *
from numpy import linspace
from collections import defaultdict
from matplotlib import pylab as p
db = get_db()
#chi_collect_name = "chi_test_result"
#nb_collect_name = "nb_test_result"
chi_collect_name = "improved_chi_test_result"
nb_collect_name = "improved_nb_test_result"
def np_chi_comp():
    fig = p.figure()
    ax = fig.add_subplot(1,2,1)
    ax.set_ylim( 0 , 2500 )

    chi_stat = []
    for r in db[chi_collect_name].find():
        chi_stat.append((r["real_cat"],r["I"]))
    ax.hist([i for c,i in chi_stat])
    ax.set_xlabel("spamicity")
    ax.set_ylabel("quantity")
    ax.set_title("spamicity histogram using chi-square method")

    ax = fig.add_subplot(1,2,2)

    nb_stat = []
    for r in db[nb_collect_name].find():
        nb_stat.append( (r["real_cat"],r["I"]) )
    
    ax.hist([i for c,i in nb_stat])
    ax.set_ylim( 0 , 2500 )
    ax.set_xlabel("spamicity")
    ax.set_ylabel("quantity")
    ax.set_title("spamicity histogram using naive-bayes method")

    p.show()

def chi_ham_spam():
    f = p.figure()
    ax1 = f.add_subplot(1,2,1)
    ax1.set_ylim( 0 , 2000 )
    ham_stat = []
    for r in db[chi_collect_name].find({"real_cat":"ham"}):
        ham_stat.append((r["real_cat"],r["I"]))
    ax1.hist([i for c,i in ham_stat])

    ax1.set_xlabel(u"spamicity")
    ax1.set_ylabel(u"quantity")
    ax1.set_title(u"normal messages spamicity histogram")

    ax2 = f.add_subplot(1,2,2)
    ax2.set_ylim( 0 , 2000 )
    spam_stat = []
    for r in db[chi_collect_name].find({"real_cat":"spam"}):
        spam_stat.append((r["real_cat"],r["I"]))
    ax2.hist([i for c,i in spam_stat])

    ax2.set_xlabel(u"spamicity")
    ax2.set_ylabel(u"quantity")
    ax2.set_title(u"spam messages spamicity histogram")

    p.show()

def chi_acc_err_data(spam_thre = 0.8 , ham_thre = 0.2):
    tn = db[chi_collect_name].find({"real_cat":"ham","I":{"$lte":ham_thre}}).count()
    tp = db[chi_collect_name].find({"real_cat":"spam","I":{"$gte":spam_thre}}).count()
    fn = db[chi_collect_name].find({"real_cat":"spam","I":{"$lte":ham_thre}}).count()
    fp = db[chi_collect_name].find({"real_cat":"ham","I":{"$gte":spam_thre}}).count()
    s_u = db[chi_collect_name].find({"real_cat":"spam","I":{"$gte":ham_thre,"$lte":spam_thre}}).count()
    h_u = db[chi_collect_name].find({"real_cat":"ham","I":{"$gte":ham_thre,"$lte":spam_thre}}).count()
    
    print "tn:%d,tp:%d,fn:%d,fp:%d,s_u:%d,h_u:%d" %(tn,tp,fn,fp,s_u,h_u)
    recall = float(tp) / ( tp + fp + s_u)
    precision = float(tp) / ( tp + fn )
    fallout = float(fp) / ( fp + tn )
    print "recall:%f\tprecision:%f\tfallout:%f" %(recall,precision,fallout)
    
def nb_acc_err_data(spam_thre = 0.5 ):
    tn = db[nb_collect_name].find({"real_cat":"ham","I":{"$lte":spam_thre}}).count()
    tp = db[nb_collect_name].find({"real_cat":"spam","I":{"$gte":spam_thre}}).count()
    fn = db[nb_collect_name].find({"real_cat":"spam","I":{"$lte":spam_thre}}).count()
    fp = db[nb_collect_name].find({"real_cat":"ham","I":{"$gte":spam_thre}}).count()

    print "tn:%d,tp:%d,fn:%d,fp:%d" %(tn,tp,fn,fp)
    recall = float(tp) / ( tp + fp )
    precision = float(tp) / ( tp + fn )
    fallout = float(fp) / ( fp + tn )
    print "recall:%f\tprecision:%f\tfallout:%f" %(recall,precision,fallout)

if __name__ == "__main__":
    #chi_ham_spam()
    #np_chi_comp()
    chi_acc_err_data()
    nb_acc_err_data()
