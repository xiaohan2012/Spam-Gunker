from email.FeedParser import FeedParser
import chardet
import codecs
from os import listdir
from os.path import isfile,join
from time_measure import *


class Email(object):
    def __init__(self,path):
        fp = FeedParser()
        charset = chardet.detect(open(path).read())
        fp.feed(codecs.open(path,encoding = charset["encoding"]).read())
        self.m = fp.close()
        
    #@measure_time        
    def get_body(self,encoding = "utf8"):
        if encoding:
            return self.m.get_payload().encode(encoding)
        else:
            return self.m.get_payload()

if __name__ == "__main__":
    path = "/home/xiaohan/code/spam-filter/2005-Jul/data/ham"
    f_names= [fname for fname in listdir(path) if isfile(join(path,fname))]
    for fname in f_names[:2]:
        fp = join(path,fname)
        try:
            e = Email(fp)
            print e.get_body()
        except UnicodeDecodeError:
            print "cannot parse it"

