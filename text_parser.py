# coding=utf-8
import subprocess
import unittest

def rm_new_line(fun):
    def wrapper(text):
        return fun(text.replace("\n",""))
    return wrapper

@rm_new_line    
def parse_text(inp):
    process=subprocess.Popen('./chn_parser',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,_ = process.communicate(input=inp)
    return unicode(stdout).decode("utf8")

def tokenize(p_str):
    tokens = p_str.split()
    a_ = []
    for tok in tokens:
        ind = tok.rfind("/")
        a_.append( (tok[:ind],tok[ind + 1:]) )
    return a_
    #return list(set(a_))

class TextParserTest(unittest.TestCase):
    def test_rm_new_line(self):
        output = parse_text("啊啊啊啊\noo ooo oooo")
        self.assertTrue("\n" not in output)

if __name__ == "__main__":
    unittest.main()

