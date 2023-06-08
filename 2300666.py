Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
heroes = []
heroes.append("아이언맨")
heroes.append("닥터스트레인지")
print(heroes)
['아이언맨', '닥터스트레인지']

letters=['A','B','C','D','E','F']
print(letters[0])
A
print(letters[2])
C

letters=['A','B','C','D','E','F']
print(letters[0:3])
['A', 'B', 'C']

print(letters[:3])
['A', 'B', 'C']
['A', 'B', 'C']
['A', 'B', 'C']

print(letters[3:])
['D', 'E', 'F']

heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
heroes[1]="닥터 스트레인지"
print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치']

heroes.append("스파이더맨")
print(heroes)
['아이언맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']

heroes.insert(1,"배트맨")
print(heroes)
['아이언맨', '배트맨', '닥터 스트레인지', '헐크', '스칼렛 위치', '스파이더맨']

heroes=["아이언맨","토르","헐크","스칼렛 위치"]
heroes.remove("스칼렛 위치")
print(heroes)
['아이언맨', '토르', '헐크']

heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
del heroes[0]
print(heroes)
['토르', '헐크', '스칼렛 위치']

heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
last_hero = heroes.pop()
print(last_hero)
스칼렛 위치

heroes = ["아이언맨","토르","헐크","스칼렛위치"]
print(heroes.index())
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(heroes.index())
TypeError: index expected at least 1 argument, got 0

heroes = ["아이언맨","토르","헐크","스칼렛위치"]
for hero in heroes:
          print(hero)

          
아이언맨
토르
헐크
스칼렛위치

heroes = ["아이언맨","토르","헐크","스칼렛 위치"]
heroes.sort()
print(heroes)
['스칼렛 위치', '아이언맨', '토르', '헐크']

import random
quotes=[]
quotes.append("꿈을 지녀라.그러면 어려운 현실을 이길 수 있다.")
quotes.append("분노는 바보들의 가슴속에서만 살아간다.")
quotes.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
quotes.append("사람은 사랑할 때 누구나 시인이 된다,")
quotes.append("시작이 반이다.")

dailyQuote=random.choice(quotes)
print("#########################################")
#########################################
print("#오늘의 속담#")
#오늘의 속담#
print(dailyQuote)
시작이 반이다.
print(dailyQuote)
시작이 반이다.
시작이 반이다.
SyntaxError: invalid syntax

phone_book = {}
phone_book["홍길동"] = "010-1234-5678"
print(phone_book)
{'홍길동': '010-1234-5678'}
print(phone_book["홍길동"])
010-1234-5678
>>> 
...  
>>> dict={'Name':'홍길동','Age':7,'Class':'초급'}
>>> print(dict['Name'])
홍길동
>>> print(dict['Age'])
7
>>> 
>>> items = {"콜라":4}
>>> items=input("물건의 이름을 입력하시오.: ");
물건의 이름을 입력하시오.: 콜라
>>> print(items[item])
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(items[item])
NameError: name 'item' is not defined. Did you mean: 'items'?
>>> items={"커피음료":7,"펜":3,"종이컵":2,"콜라":4,"책":5}
>>> item=input("물건의 이름을 입력하시오:");
물건의 이름을 입력하시오:콜라
>>> print(items[item])
4
>>> 
>>> english_dict=dict()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    english_dict=dict()
TypeError: 'dict' object is not callable
>>> english_dict=dict()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    english_dict=dict()
TypeError: 'dict' object is not callable
>>> english_dict = dict()
... english_dict['one'] = '하나'
... english_dict['two'] = '둘'
... english_dict['three'] = '셋'
... word = input("단어를 입력하시오: ");
... print (english_dict[word])
SyntaxError: multiple statements found while compiling a single statement
