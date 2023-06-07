# WRP

## 1. 프로젝트 소개
### 프로젝트 추진 배경
최근 코로나 방역 완화로 다시 활발해진 해외여행으로 인해서 외국으로 놀러나가거나 공부를 위해 출국하는 사람들이 잦아졌다. 그런 사람들을 보고 언어를 학습하여 번역기나 통역기가 아닌 직접 대화를 나누는 것에 대한 로망을 실천하고싶어하며, 어학 공부에 뛰어든 사람들의 수가 증가하였다. 최근 기사에서 발견한 효과적인 단어 암기법을 어학 자격증의 단어들을 보다 쉽게 암기할 수 있도록 하고자 오픈소스로 여러 프로젝트를 공유하고 공유 받는 것을 다루는 강의의 목표를 따라가고자 이러한 프로젝트를 추진하게 되었다.

## 2. 개발기간
* 23.04.13 - 23.06.07

## 3. 구현 기능 소개
* 단어장 앱을 실행한다.
![캡처](/image/win_start.png)
* 입력된 단어장들을 확인할 수 있다.
![캡처](/image/win_list.png)
* 입력되어있는 단어장을 확인하여 단어장 안의 단어를 하나씩 확인하며 외울 수 있다.
![캡처](/image/win_word.png)

## 4. 사용자 가이드
### 배경
* GitHub Repository를 컴퓨터에 clone한다.
* cmd 창에 'pip install pyside6'를 입력하여 pyside6를 컴퓨터에 설치한다.

### 사용
단어장 추가
- 다운받은 Repository 로컬 파일에 들어가 wordfile에 원하는 sheet와 단어들을 단어 - 뜻 순서대로 입력한다.
next 버튼을 눌러 다음 단어로 넘어가며 단어를 회독한다.
단어장 삭제
- 삭제하고싶은 단어장을 선택한 뒤 삭제버튼을 누른다. 단, 복구할 수 없으니 조심하자.

