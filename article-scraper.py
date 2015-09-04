# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 02:16:27 2015

@author: BHUKANIA.NEERAJ
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup

z =[]
y =[]
r =[]
k = []
count =0
state = []
x2 = pd.DataFrame(columns = ['article_ID','Heading','Date','content','state'])    
for i in xrange(1,5):
    page1 = requests.get('http://thenortheasttoday.com/category/states/arunachal-pradesh/page/{}'.format(i))
    if not page1.ok:
        continue
    soup = BeautifulSoup(page1.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText())
count = len(r)
for t in xrange(1,(count+1)):
    state.append('arunachal-pradesh')
temp = t+1            
#x2['state']='arunachal-pradesh'            
#for assam
count = 0    
for i in xrange(1,5):
    page2 = requests.get('http://thenortheasttoday.com/category/states/assam/page/{}'.format(i))
    if not page2.ok:
        continue
    soup = BeautifulSoup(page2.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText()) 
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('assam')
temp = t+1             
#x2['state']='assam'            
#for manipur
for i in xrange(1,5):
    page3 = requests.get('http://thenortheasttoday.com/category/states/manipur/page/{}'.format(i))
    if not page3.ok:
        continue
    soup = BeautifulSoup(page3.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText())
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('manipur')
temp = t+1                        
#x2['state']='manipur'            
#for meghalaya
for i in xrange(1,5):
    page4 = requests.get('http://thenortheasttoday.com/category/states/meghalaya/page/{}'.format(i))
    if not page4.ok:
        continue
    soup = BeautifulSoup(page4.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText())
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('meghalaya')
temp = t+1               
#x2['state'] = 'meghalaya'            
#for mizoram            
for i in xrange(1,5):
    page5 = requests.get('http://thenortheasttoday.com/category/states/mizoram/page/{}'.format(i))
    if not page5.ok:
        continue
    soup = BeautifulSoup(page5.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText())
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('mizoram')
temp = t+1               
#x2['state']='mizoram'            
#for nagaland
for i in xrange(1,5):
    page6 = requests.get('http://thenortheasttoday.com/category/states/nagaland/page/{}'.format(i))
    if not page6.ok:
        continue
    soup = BeautifulSoup(page6.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText())
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('nagaland')
temp = t+1               
#x2['state']='nagaland'            
#for sikkim
for i in xrange(1,5):
    page7 = requests.get('http://thenortheasttoday.com/category/states/sikkim/page/{}'.format(i))
    if not page7.ok:
        continue
    soup = BeautifulSoup(page7.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText())
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('sikkim')
temp = t+1               
#x2['state']='sikkim'            
#for tripura
for i in xrange(1,5):
    page8 = requests.get('http://thenortheasttoday.com/category/states/tripura/page/{}'.format(i))
    if not page8.ok:
        continue
    soup = BeautifulSoup(page8.text)
    for x in soup.find_all('p'):
            z.append(x.getText())
    for x in soup.find_all('time'):
            y.append(x.getText()) 
    for x in soup.find_all('h2'):
            r.append(x.getText()) 
count = len(r)
for t in xrange(temp,(count+1)):
    state.append('tripura')
temp = t+1               
#x2['state']='tripura' 
del z[0::2]             
for x in xrange(1,(count+1)):
    k.append(x)
x2['article_ID'] = k
x2['Heading']=r
x2['Date'] = y
x2['content']=z
x2['state'] = state
x2.to_excel('thenortheasttoday.xlsx',encoding = 'utf-8')




     