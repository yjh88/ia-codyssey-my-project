"""
나만의 프롬프트 관리자 (Prompt Manager)
- 작성자: AI 활용 학습자
- 개발 환경: Python 3.10+ / Git
"""
import os
import json

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]

def get_default_prompts() -> list[dict]:
    """초기 실행 시 제공되는 기본 프롬프트 4개 반환"""
    return [
        {
            "id": 1,
            "title": "블로그 글 작성 도우미",
            "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
            "category": "텍스트 생성",
            "favorite": True,
            "views": 5
        },
        {
            "id": 2,
            "title": "제품 썸네일 생성",
            "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요: 배경은 현대적인 미니멀리즘 스튜디오, 자연스러운 소프트 조명, 제품이 정중앙에 위치하며 고해상도 8k 렌더링 스타일.",
            "category": "이미지 생성",
            "favorite": False,
            "views": 2
        },
        {
            "id": 3,
            "title": "IT 컨설턴트 페르소나",
            "content": "당신은 포춘 500대 기업 대상 15년 경력의 수석 클라우드 솔루션 아키텍트입니다. 비즈니스 리더가 이해하기 쉬운 비유와 실무적인 아키텍처 다이어그램 설계 방안을 곁들여 설명해주세요.",
            "category": "페르소나",
            "favorite": True,
            "views": 8
        },
        {
            "id": 4,
            "title": "뉴스 요약 자동화 프롬프트",
            "content": "제공된 긴 뉴스 기사를 핵심 요약 3줄, 주요 인물 및 수치 팩트체크, 향후 시장 영향 분석으로 정돈하여 마크다운 표와 불릿 포인트로 작성하세요.",
            "category": "자동화",
            "favorite": False,
            "views": 1
        }
    ]

def display_header(title: str):
    """표준 섹션 헤더 출력"""
    print(f"\n{'=' * 10} {title} {'=' * 10}")
