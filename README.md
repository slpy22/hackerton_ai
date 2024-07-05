부동산 매물 추천 AI 서비스
===
---
# 목차
1. [버전정보](#버전정보)
2. [설정가이드](#설정가이드)
3. [실행](#실행)

---

## 버전정보

- python 3.11
---
## 빌드 설정
- 프로젝트 루트 폴더로 이동
- 다음의 명령들을 차례로 실행
- python -m venv venv
- OS의 종류 확인
  - macOS의 경우 source venv/bin/activate 실행
  - windows의 경우 venv\Scripts\activate 실행
- pip install -r r.txt

## OpenAI key 설정
- 프로젝트의 루트 폴더에 .env라는 빈 파일을 만든다.
- 이 파일을 열어서 다음과 같이 OpenAI의 API키를 추가 한다.
- OPENAI_API_KEY=sk-????-???????
---

## 실행
- python -m src.main

## API 호출 테스트
- url : http://localhost:8010/estate/predict
- method : POST
- body : form-data 
  - img_file : 여기에 이미지 파일 첨부
