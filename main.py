from email_util import *
from train import *
from util import *

if __name__ == "__main__":
    ham_fp_list,spam_fp_list = [],[]
    clean_db()#clean the db data
    build_index()#build index
    #register ham
    path = "/home/xiaohan/code/spam-filter/2005-Jul/data/ham"
    f_names = get_files_in_dir(path)
    for i,fname in enumerate(f_names):
        print "the %d th ham message" %i
        fp = join(path,fname)
        try:
            e = Email(fp)
            text = e.get_body()
            register("ham",text,fname)
        except UnicodeDecodeError:
            print "cannot parse it"
        ham_fp_list.append(fname)
            
    #register spam                    
    path = "/home/xiaohan/code/spam-filter/2005-Jul/data/spam"
    f_names = get_files_in_dir(path)
    for i,fname in enumerate(f_names):
        print "the %d th spam message" %i
        fp = join(path,fname)
        try:
            e = Email(fp)
            text = e.get_body()
            register("spam",text,fname)
        except UnicodeDecodeError:
            print "cannot parse it"
        spam_fp_list.append(fname)
    
