# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:06:56 2019

@author: Shawn Hu
"""


from collections import Counter
import re
import os
nw = os.path.abspath('.').replace("\\","/")

def openfile(tip):
    while True:
        try:
            path =tip
            file = open(path.replace("\\","/"),"r")
            return file.read()
        except:
            tip=input("檔案路徑錯誤!!!請重新輸入:")
            
            continue


def Compare():
   
    first = input("輸入檔案1路徑:")
    first = openfile(first)
    second = input("輸入檔案2路徑:")
    second= openfile(second)
    sp = input("資料轉成清單(若資料以空白、換行作為分割依據，則直接按回車鍵，若無，請輸入分割依據)：")

        
    if sp == "":        
        first = first.split()    
        second = second.split()
    else:
        first = first.split(sp)
        second = second.split(sp)        
    
    first = set(first)
    second = set(second)
    
    result = list(first.difference(second))
    
    print(result)



def delr():
   
    first = input("輸入檔案路徑:")
    first = openfile(first)
    sp = input("資料轉成清單(若資料以空白、換行作為分割依據，則直接按回車鍵，若無，請輸入分割依據)：")
    
    
    if sp == "":        
        first = first.split()    
    else:
        first = first.split(sp)
    
    result = Counter(first)
    key = result.keys()
    for k in key:
        if (result[k]) > 1:
            print(k+"重複幾次?"+ str(result[k]-1))
            
def regex():
    data = input("輸入檔案路徑:")
   
    data = openfile(data)
    pat = input("輸入正則表達式:")
    it = re.finditer(pat,data) 
    li=[]
    for match in it: 
        print (match.group())
        li.append(match.group())
    

    YN=input('要存檔此次結果嗎')    
    if ((YN == 'Y')|(YN=='y')):
        while True:
            try:
                SV=input('存檔位置:')
        
                path =nw+"/"+SV
                file = open(path.replace("\\","/"),"w+")
                
                for i in li: 
                    file.writelines(i+"\n")
                        
                file.close()
            except:
                print("檔案路徑錯誤!!!請重新輸入")
                continue
    else:
        print("結束")
            
            





print("比對檔案&正規化小幫手 v 0.1 beta")


print("請選擇功能項目：\n")
print("1.比對兩份檔案")
print("2.刪除重複項目")
print("3.檔案分割正規化")

ch = input(":")


if ch == "1":
    Compare()
elif ch == "2":
    delr()
elif ch == "3":
    regex()
else:
    print('輸入錯誤!!!')


  