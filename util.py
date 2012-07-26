from os import listdir
from os.path import isfile,join
from email_util import *
from text_parser import *

def sanitizer(s):
    """decorator may be here"""
    return s
def file_bulk_reader(dir):
    """return the list of content of files"""
    return []
def get_files_in_dir(path):
    return [fname for fname in listdir(path) if isfile(join(path,fname))]

def get_tokens_from_fp(fp):
    e = Email(fp)
    text = e.get_body()
    return tokenize(parse_text(text))
