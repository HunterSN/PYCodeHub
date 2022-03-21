import difflib
import csv
import os

def standardingprotein(pathway):
    inputsorcefile = csv.reader(open('sourceprotein.csv', encoding='utf-8-sig'))
    c = 0
    ccc = 1
    for sourcerow in inputsorcefile:
        i = 0
        #print('第一个' + str(i))
        zhong = '0'
        targetprotein = 'None'
        sopn = str(sourcerow).replace('[','').replace(']','').replace("'","").replace('"','')
        #print('开始' + sopn)
        inputstandaedfile = csv.reader(open('standardprotein.csv', encoding='utf-8-sig'))
        for standardrow in inputstandaedfile:
            sdpn = str(standardrow).replace('[','').replace(']','').replace("'","").replace('"','')
            #print(sopn)
            #print(sdpn)
            num = difflib.SequenceMatcher(None,sopn,sdpn).quick_ratio()
            #print(sdpn + '  ' + str(num))
            if num > i:
                i = num
                targetprotein = sdpn
                pass
            else:
                i = i
                pass
            #print(i)
            #print(targetprotein)
            zhong = str(i)
            c = c + 1 
            pass
        outputprotein = open('standardedprotein.txt','a+')
        outputprotein.write(sopn + '$' + targetprotein + '$' + zhong + '\n')
        outputprotein.close()
        #print(str(sourcerow))
        print(ccc)
        ccc = ccc + 1
    pass


def qufangkuohao(pathway):
    inputsorcefile = csv.reader(open('sourceuniprot.csv'))
    for sourcerow in inputsorcefile:
        sourceu = str(sourcerow)
        sopn = str(sourcerow).replace('[','').replace(']','').replace("'","").replace('"','')
        outputprotein = open('matchtcmsp.txt','a+')
        outputprotein.write(sopn + '$' + sourceu + '\n')
        outputprotein.close()
    pass


standardingprotein('skjfdk')
#qufangkuohao('fsffss')