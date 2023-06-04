# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:34:08 2023

@author: 苏小洲suxiaozhou
"""

#!/usr/bin/python3

import seaborn as sns
import pandas as pd
import seaborn as sns
sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']}) 
import matplotlib.pyplot as plt
def watch():
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    
    
    sns.set(style="ticks", color_codes=True)
    iris=pd.read_csv('Iris.csv',encoding="gb2312")
    iris.drop('Id',axis=1,inplace=True)
    print(iris.head())
    #sns.pairplot(iris)
    
    sns.pairplot(iris, hue="Species", palette="husl", markers=["o", "s", "D"])
    sns.set_style('whitegrid',{'font.sans-serif':['simhei','Arial']}) 
"""
def check():#单维度检查
    iris.drop(['萼片长','萼片宽','花瓣宽'],axis=1,inplace=True)
    print(iris);
    iris.sort_values(by='花瓣长',axis=0,ascending=True, inplace=True, na_position='last')
    print("sort finish")
    print(iris)
    weights=[]
    for i in range(1,100):
        weights.append({"品种setosa":0,"品种virginica":0,"品种versicolor":0});
    for i in range(0,len(iris)):
        for j in range(-5,5):
            weights[int(iris["花瓣长"][i]*10)+j][iris["Species"][i]]+=int(1/(abs(j-0)+1)*100);
    print(weights)
    test=int(float(input("请输入花瓣长！"))*10)
    max_wei=max(weights[test]["品种setosa"],max(weights[test]["品种virginica"],weights[test]["品种versicolor"]))
    if (max_wei==weights[test]["品种setosa"]):
        print("品种setosa")
    elif (max_wei==weights[test]["品种virginica"]):
        print("品种virginica")
    else:
        print("品种versicolor")
check();
"""
def check(line):#单维度检查,line=检查的列
    iris=pd.read_csv('Iris.csv',encoding="gb2312")
    iris.drop('Id',axis=1,inplace=True)
    del_line_list=['萼片长','萼片宽','花瓣长','花瓣宽'];
    del_line_list.remove(line);
    iris.drop(del_line_list,axis=1,inplace=True)
    print(iris);
    iris.sort_values(by=line,axis=0,ascending=True, inplace=True, na_position='last')
    print("sort finish")
    print(iris)
    weights=[]
    for i in range(1,10*10):
        weights.append({"品种setosa":0,"品种virginica":0,"品种versicolor":0});
    for i in range(0,len(iris)):
        for j in range(-5,5):
            weights[int(iris[line][i]*10)+j][iris["Species"][i]]+=int(1/(abs(j-0)+1)*100);
    return weights;
#watch();
def main1():
    wei1=check('花瓣长')
    wei2=check('花瓣宽')
    wei3=check('萼片长')
    wei4=check('萼片宽')
    print(wei1)
    print(wei2)
    print(wei3)
    print(wei4)
    test1=int(float(input("花瓣长"))*10);
    test2=int(float(input('花瓣宽'))*10);
    test3=int(float(input("萼片长"))*10);
    test4=int(float(input("萼片宽"))*10);
    
    weights={"品种setosa":0,"品种virginica":0,"品种versicolor":0}
    
    weights["品种setosa"]=wei1[test1]["品种setosa"]+wei2[test2]["品种setosa"]+wei3[test3]["品种setosa"]+wei4[test4]["品种setosa"];
    weights["品种virginica"]=wei1[test1]["品种virginica"]+wei2[test2]["品种virginica"]+wei3[test3]["品种virginica"]+wei4[test4]["品种virginica"];
    weights["品种versicolor"]=wei1[test1]["品种versicolor"]+wei2[test2]["品种versicolor"]+wei3[test3]["品种versicolor"]+wei4[test4]["品种versicolor"];
    
    max_wei=max(weights["品种setosa"],max(weights["品种virginica"],weights["品种versicolor"]))
    if (max_wei==weights["品种setosa"]):
        print("品种setosa")
    elif (max_wei==weights["品种virginica"]):
        print("品种virginica")
    else:
        print("品种versicolor")

def main2():
    wei1=check('花瓣长')
    wei2=check('花瓣宽')
    wei3=check('萼片长')
    wei4=check('萼片宽')
    print(wei1)
    print(wei2)
    print(wei3)
    print(wei4)#test1,test2,test3,test4
    weights={"品种setosa":0,"品种virginica":0,"品种versicolor":0}
    iris=pd.read_csv('Iris.csv',encoding="gb2312")
    iris.drop('Id',axis=1,inplace=True)
    con=0;
    r_ans=0;
    for i in range(0,len(iris)):
        con+=1;
        test1=int(iris['花瓣长'][i]*10);
        test2=int(iris['花瓣宽'][i]*10);
        test3=int(iris['萼片长'][i]*10);
        test4=int(iris['萼片宽'][i]*10);
        weights["品种setosa"]=wei1[test1]["品种setosa"]+wei2[test2]["品种setosa"]+wei3[test3]["品种setosa"]+wei4[test4]["品种setosa"];
        weights["品种virginica"]=wei1[test1]["品种virginica"]+wei2[test2]["品种virginica"]+wei3[test3]["品种virginica"]+wei4[test4]["品种virginica"];
        weights["品种versicolor"]=wei1[test1]["品种versicolor"]+wei2[test2]["品种versicolor"]+wei3[test3]["品种versicolor"]+wei4[test4]["品种versicolor"];
        max_wei=max(weights["品种setosa"],max(weights["品种virginica"],weights["品种versicolor"]))
        if (max_wei==weights["品种setosa"]):
            my_ans="品种setosa"
        elif (max_wei==weights["品种virginica"]):
            my_ans="品种virginica"
        else:
            my_ans="品种versicolor"
        if (my_ans==iris['Species'][i]):
            r_ans+=1;
    print(con)
    print(r_ans)
    print(str(round(r_ans/con*100))+"%正确率")

if (1):
    if (0):
        main1();
    else:
        main2();
else:
    watch();