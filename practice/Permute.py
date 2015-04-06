'''
Created on Mar 31, 2014

@author: swapnesh
'''
#!/usr/bin/python
import sys

def permute(instr):
    
    permuteList=[]
    
    if(instr is None):
        return None
    
    if(len(instr)==0):
        permuteList.append("")
        return permuteList
    
    first=instr[0]
    remainder=instr[1:]
    
    words=permute(remainder)
    if words:
        for word in words:
            for j in range(0,len(word)+1):
                String=insertcharat(word,first,j)
                permuteList.append(String)
    
    return permuteList

def insertcharat(word,first,j):
    return word[0:j]+first+word[j:]

def main():
    
    PList=permute("abc")
    
    print PList

if __name__ == '__main__':
    main()