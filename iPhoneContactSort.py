"""
    Author:zheng.li
    E-mail:ronnie.alonso@gmail.com
"""
import re
from pinyin import PinYin

class iPhoneContactSort(object):
    def __init__(self, filename='contacts.vcf'):
        self.filename = filename

    def Convert(self):
        py_engine = PinYin()
        py_engine.load_word()

        contact = list()
        f = open(self.filename,'r')
        for line in open(self.filename):  
            line = f.readline()
            contact.append(line)
            k = re.findall(r"(\N\:[^\;]*\;)", line) 
            if k:
                phones = py_engine.hanzi2pinyin(string=k[0])
                line = "X-PHONETIC-LAST-NAME:"
                for item in phones:
                    if item != '':
                        line = line + item.capitalize()
                line += "\n"
                contact.append(line)

        fout = open(filename, 'w')
        for line in contact:
            fout.write(line)

if __name__ == '__main__':
    filename = 'Brown David and 397 others.vcf'
    i_engine = iPhoneContactSort(filename)
    i_engine.Convert()
