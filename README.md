# KorEDA 

소스코드는 [catSirup](https://github.com/catSirup/KorEDA/tree/master)님이 올린 코드를 사용해 inference 코드를 구현했습니다.

이 프로젝트는 [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://github.com/jasonwei20/eda_nlp) 를 한국어로 쓸 수 있도록 wordnet 부분만 교체한 프로젝트 입니다.

wordnet은 KAIST에서 만든 [Korean WordNet(KWN)](http://wordnet.kaist.ac.kr/) 을 사용했습니다.

EDA에 대한 자세한 내용은 [논문](https://arxiv.org/pdf/1901.11196.pdf)을 참조하시거나 [한글로 번역한 블로그](https://catsirup.github.io/ai/2020/04/21/nlp_data_argumentation.html)를 확인하시면 됩니다.

## argmentation

- sr 특정 단어를 유의어로 교체

- ri 임의의 단어를 삽입

- rs 문장 내 임의의 두 단어의 위츠를 바꿈

- rd 임의의 단어를 삭제

- 다음과 같이 4개의 agmentation이 나오게 됩니다.

## How to use

1. inference.py의 data_path(데이터를 늘린 csv파일 경로), save_file_path(늘린 데이터를 저장할 경로)를 설정해주시고 실행하시면 됩니다.

2. make_dataset.py

sum_sheet 함수는 나누어져 있는 sheet를 합쳐주고 label을 붙여주는 함수입니다.(pandas사용)

sum_csv 함수는 나누어져 있는 파일을 합쳐주는 함수입니다.

### data_path 데이터 구조

|script|label|
|---|---|
|나는 정말 행복해|1|
|나는 정말 불행하고 슬퍼|0|

## 결과

inference한 결과

|script|label|
|---|---|
|나는 정말 행복|1|
|나는 행복해|1|
|나는 정말 불행하고|2|
|나는 불행하고 정말 슬퍼|2|

이렇게 결과를 얻을 수 있습니다.

## EDA만 한 결과

원문 데이터
```plain
제가 우울감을 느낀지는 오래됐는데 점점 개선되고 있다고 느껴요
```
data augmentation한 데이터
```plain
우울감을 느낀지는 오래됐는데 점점 개선되고 있다고	
제가 우울감을 느낀지는 오래됐는데 느껴요 개선되고 있다고 점점	
오래됐는데 우울감을 느낀지는 제가 점점 개선되고 있다고 느껴요	
느껴요 우울감을 느낀지는 오래됐는데 점점 개선되고 있다고 제가
```

## 한계
문장이 짧거나 바뀔 문장이 없다면 원래의 문장이 그대로 나오게 됩니다.

WordNet만을 단순히 바꿔서 결괏값을 내기 때문에 의미가 변형되어버리는 경우가 생깁니다. 특히 SR과 RI를 사용할 때 많이 발생하는데 **제가 잘못한 건 아닌 것 같아요** 를 **제가 잘못한 총 아닌 것 같아요** (건 -> 총) 으로 바뀌기도 한다. 본 논문에서는 이렇게 바꿔도 꽤나 원문 데이터의 성질을 따라간다고 하지만.. 한국어의 특성상 완전히 따라가기에는 쉽지 않은 것 같다.

안전하게 데이터 증강을 하고 싶다면 RD, RS만을 사용하고, 데이터가 많이 필요하다싶으면 SR과 RI까지 사용하고 인간지능으로 데이터를 걸러내는 작업이 필요할 것이다.
