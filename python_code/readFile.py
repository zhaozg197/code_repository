#!/usr/bin/env python
import configparser
import codecs

filepath=r'E:\python学习\exec\corperfmonsymbols.ini'

def printContext(lines):
    for line in lines:
        if -1 != line.find('='):
            str=[]
            str=line.split('=')
            print(str[1])

def readFile():
    iniFile=open(filepath,'r')
    lines=iniFile.readlines()
    return lines

def main():
    lines=[]
    #lines = readFile()
    #printContext(lines)
    cp = configparser.ConfigParser()
    with codecs.open(filepath, 'r', encoding='utf-8') as f:
        ft=f.encode(encoding='utf-8',errors="ignore")
        #print(ft)
        #f.write(ft)
        #cp.readfp(f)
        #lines = cp.get('text', 'GEN0_COLLECTIONS_COUNTER_009_HELP')
        #print(lines)


if __name__ == '__main__':
    main()
