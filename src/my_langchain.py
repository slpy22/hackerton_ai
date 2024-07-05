from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate

from langchain_core.prompts.image import ImagePromptTemplate

# API KEY 정보로드
load_dotenv()

# LLM, 응답 인스턴스 설정
model = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()


def extract_information(img):
    prompt_text = ("첨부의 이미지가 나타내는 지역에 대한 부동산 정보 알려 줘"
                   "매매가격(저가, 고가, 평균가), 전세가격(저, 고, 평균), 교통상황(대중, 자가), 건물 외관 상태, 학군정보"
                   "위의 모든 정보에 대하여 0~100 점 사이의 점수도 추가 해 줘."
                   "이 정보들을 json형식으로 생성해 줘. json의 키는 점수는 'point'로 나머지들은 각각"
                   "'price', 'low', 'high', 'middle', 'jonse', 'traffic', 'public', 'private', 'school"
                   "으로 해 줘.")
    prompt_template = HumanMessagePromptTemplate.from_template(
        template=[
            {"type": "text", "text": prompt_text},
            {
                "type": "image_url",
                "image_url": "{img_data}",
            },
        ]
    )
    prompt = ChatPromptTemplate.from_messages([prompt_template])

    # LCEL 체인 생성
    chain = prompt | model | output_parser

    # 체인 호출, 결과 저장, 출력
    result = chain.invoke(input={"img_data": img})
    print(result)
    return result


def recommend_estate(information):
    prompt_text = ("{information}과 유사한 특성의 부동산 매물들을 네이버 부동산 정보를 활용 해서 찾아줘. "
                   "네이버등 인터넷 검색을 해서 찾아 줘."
                   "최대한 많은 후보를 찾아주고 그 매물들의 도로명 주소의 array로 리턴 해 줘."
                   "일체 설명 다 필요 없고 오직 찾아낸 주소들만 array로 리턴 해 줘"
                   "결과를 찾을 수 없으면 그냥 아무 문자도 출력 하지 마.")
    prompt = ChatPromptTemplate.from_template(prompt_text)
    # LCEL 체인 생성
    chain = prompt | model | output_parser

    # 체인 호출, 결과 저장, 출력
    result = chain.invoke({"information": information})
    print(result)
    return result
