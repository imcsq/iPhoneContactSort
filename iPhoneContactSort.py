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
            k = re.findall(r"(\N\:[^\;]*\;[^\;]*\;[^\;]*\;[^\;]*\;)", line) 
            if k:
                if k[0].find(';') - 2 > 3:
                    xing = k[0][2: 5]
                    ming = k[0][5: k[0].find(';')] + k[0][k[0].find(';') + 1 : k[0].find(';', k[0].find(';')+1)]
                else:
                    xing = k[0][2: k[0].find(';') ]
                    ming = k[0][k[0].find(';') + 1 : k[0].find(';', k[0].find(';')+1)]
                contact.append('N:'+xing+';'+ming+';'+";;\n")

                phones = py_engine.hanzi2pinyin(string=xing)
                line = "X-PHONETIC-LAST-NAME:"
                for item in phones:
                    if item != '':
                        line = line + item.capitalize()
                line += "\n"
                contact.append(line)

                phones = py_engine.hanzi2pinyin(string=ming)
                line = "X-PHONETIC-FIRST-NAME:"
                for item in phones:
                    if item != '':
                        line = line + item.capitalize()
                line += "\n"
                contact.append(line)
            else:
                contact.append(line)

        fout = open("ok_"+self.filename, 'w')
        for line in contact:
            fout.write(line)

if __name__ == '__main__':
    filename = 'a.vcf'
    i_engine = iPhoneContactSort(filename)
    i_engine.Convert()
