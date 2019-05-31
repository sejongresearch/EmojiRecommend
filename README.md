# Artificial Intelligence
세종대학교 인공지능 수업 **소웨지존 팀**

<br>

## 진행상황

* 트위터 데이터 크롤링 ... 진행중
* 데이터 전처리... 진행중 
* 데이터 학습 ... 모델 지식 습득중
* 모델 테스트


<br>

## 현재 진행상황 상세

[트위터 데이터 크롤링]
*****************************************
트위터에서 제공하는 api를 이용해 인증키를 받으면 트위터 정보를 읽어 올 수 있다.
[애정, 분노, 슬픔, 피곤, 공포]등의 감정을 대표할 수 있는 이모티콘을 포함한 트윗을 읽어 csv파일로 저장한다
[twitterscraper](https://pypi.org/project/twitterscraper/0.2.7/)를 이용하면 더 오래된 트윗도 읽어올 수 있다.
[크롤링_예시](https://colab.research.google.com/drive/1REz1FcRk2vdIshHQeJAKmraYRZL6KzeE#scrollTo=HHXOOPuyN4GV)

<br>
<br>


[데이터 전처리]
*****************************************
트윗에서 적절하지 않은 단어와 멘션과 같은 토큰을 제거하고, [트위터](https://github.com/twitter/twitter-korean-text), [꼬꼬마](http://kkma.snu.ac.kr/documents/), [코모란](https://www.shineware.co.kr/products/komoran/)과 같은 형태소 분석기로 전처리한다.


<br>
<br>


[데이터 학습]
*****************************************
조사를 제외한 단어단위로 학습을 할지 아니면 조사를 포함하여 학습할 지 정하고
모델에 사용할 네크워크에 대해 공부하고 있음.


<br>
<br>

## 참고할 링크

[한국어 감성 분석기](https://github.com/mrlee23/KoreanSentimentAnalyzer)<br>
[감정기반 이모지추천 시스템](https://github.com/yunsikus/BOAZ_Project)<br>
[KoNLPy를 이용한 한국어 영화 리뷰 감정 분석](https://cyc1am3n.github.io/2018/11/10/classifying_korean_movie_review.html)<br>
[형태소 분석기 성능 비교](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/05/10/postag/)<br>
[이모티콘 추천기 (영어)](https://github.com/DOsinga/deep_learning_cookbook/blob/master/07.1%20Text%20Classification.ipynb)<br>

<br>

## Table of Contents
* Topic
* Execution environment
* Execution screen
* How to execute
* How to contribute
* License
* Contributer's Information

<br>

## 1. Topic: 이모티콘 추천 분류기
이모티콘은 주석으로 달아놓은 상태에서 문장을 미리 설정해 놓은 클래스로 분류하고,  
클래스에 맞는 이모티콘을 추천하는 AI분류기를 만들 예정

<br>

## 2. Execution environment 
파이썬을 기반으로 Google Colab을 통해 개발

<br>

## 3. Execution screen
(준비중)

<br>

## 4. How to execute
(준비중)

<br>

## 5. How to contribute
 (준비중) 
    

<br>

## 6. License
[Open-source under ?? license](https://tldrlegal.com/)  
(준비중)

<br>

## 7. Contributor's Information
| 이름| 학과 | Github | Email |
|:---:|:---:|:---:|:---:|
|김경남|소프트웨어학과|[@kimkyeongnam](https://github.com/kimkyeongnam)|[kkyy0126@naver.com](kkyy0126@naver.com)|
|김민주|소프트웨어학과|[@min942773](https://github.com/min942773)|min942773@gmail.com|
|유지인|디지털콘텐츠학과|[@jiin0217](https://github.com/jiin0217)|yji9602@naver.com|
|이주혁|소프트웨어학과|[@zero5two4](https://github.com/zero5two4)|zero5.two4@gmail.com|
|황유진|지능기전공학부<br>무인이동체공학|[@hyj378](https://github.com/hyj378)|yujine92@gmail.com|
