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



def select_category() -> str:
    """카테고리 선택 또는 직접 입력 헬퍼"""
    print("\n카테고리 선택:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}) {cat}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")
    
    while True:
        sel = input("선택: ").strip()
        if sel.isdigit():
            val = int(sel)
            if 1 <= val <= len(CATEGORIES):
                return CATEGORIES[val - 1]
            elif val == len(CATEGORIES) + 1:
                custom_cat = input("카테고리명 직접 입력: ").strip()
                if custom_cat:
                    return custom_cat
                print("카테고리명이 비어있습니다. 다시 입력해주세요.")
            else:
                print("올바른 번호를 선택해주세요.")
        else:
            print("숫자를 입력해주세요.")



def add_prompt(prompts: list[dict]):
    """새로운 프롬프트 추가 (입력 유효성 검증 포함)"""
    display_header("프롬프트 추가")
    
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("⚠️ 제목은 비어 있을 수 없습니다. 다시 입력해주세요.")
        
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("⚠️ 내용은 비어 있을 수 없습니다. 다시 입력해주세요.")
        
    category = select_category()
    
    new_id = max([p.get("id", 0) for p in prompts], default=0) + 1
    new_prompt = {
        "id": new_id,
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    }
    prompts.append(new_prompt)
    print("\n✅ 프롬프트가 추가되었습니다!")



def show_list(prompts: list[dict]):
    """저장된 모든 프롬프트를 번호와 함께 출력"""
    display_header("프롬프트 목록")
    if not prompts:
        print("등록된 프롬프트가 없습니다. 먼저 프롬프트를 추가해주세요.")
        return
        
    for idx, p in enumerate(prompts, 1):
        fav_mark = " ⭐" if p.get("favorite") else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_mark}")
        
    print(f"\n총 {len(prompts)}개의 프롬프트")



def show_by_category(prompts: list[dict]):
    """카테고리별 프롬프트 필터링 및 조회"""
    display_header("카테고리별 조회")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}) {cat}")
        
    sel = input("선택: ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(CATEGORIES)):
        print("⚠️ 잘못된 카테고리 번호입니다.")
        return
        
    chosen_cat = CATEGORIES[int(sel) - 1]
    filtered = [p for p in prompts if p.get("category") == chosen_cat]
    
    print(f"\n[{chosen_cat}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return
        
    for idx, p in enumerate(filtered, 1):
        fav_mark = " ⭐" if p.get("favorite") else ""
        print(f"{idx}. {p['title']}{fav_mark}")
        
    print(f"\n총 {len(filtered)}개의 프롬프트")



def search_prompt(prompts: list[dict]):
    """키워드로 제목 또는 내용 검색"""
    display_header("프롬프트 검색")
    query = input("검색어: ").strip()
    if not query:
        print("⚠️ 검색어를 입력해주세요.")
        return
        
    matches = [
        p for p in prompts 
        if query.lower() in p.get("title", "").lower() or query.lower() in p.get("content", "").lower()
    ]
    
    print("\n검색 결과:")
    if not matches:
        print(f"'{query}'에 대한 검색 결과가 없습니다.")
        return
        
    for idx, p in enumerate(matches, 1):
        fav_mark = " ⭐" if p.get("favorite") else ""
        print(f"{idx}. [{p['category']}] {p['title']}{fav_mark}")
        
    print(f"\n{len(matches)}개의 프롬프트를 찾았습니다.")



def show_detail(prompts: list[dict]):
    """프롬프트 번호를 입력받아 상세 내용 전체 출력 및 조회수 증가"""
    display_header("프롬프트 상세 보기")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
        
    num_str = input("번호 입력: ").strip()
    if not num_str.isdigit() or not (1 <= int(num_str) <= len(prompts)):
        print("⚠️ 잘못된 번호입니다. 올바른 프롬프트 번호를 입력해주세요.")
        return
        
    target = prompts[int(num_str) - 1]
    target["views"] = target.get("views", 0) + 1
    fav_mark = "⭐" if target.get("favorite") else "미지정"
    
    print("────────────────────────────")
    print(f"제목: {target['title']}")
    print(f"카테고리: {target['category']}")
    print(f"즐겨찾기: {fav_mark}")
    print(f"조회수: {target['views']}회")
    print("────────────────────────────")
    print("내용:")
    print(target["content"])
    print("────────────────────────────")


def show_menu():
    """메인 메뉴 UI 출력"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def main():
    prompts = get_default_prompts()
    print("✨ 나만의 프롬프트 관리 프로그램에 오신 것을 환영합니다!")
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("\n프로그램을 종료합니다. 즐거운 생성형 AI 여정이 되시길 바랍니다! 👋")
            break
        elif choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            show_by_category(prompts)
        elif choice == "4":
            search_prompt(prompts)
        elif choice == "5":
            show_detail(prompts)
        elif choice == "6":
            print("\n[안내] 즐겨찾기 관리 기능 준비 중입니다.")
        elif choice == "7":
            print("\n[안내] 즐겨찾기 목록 기능 준비 중입니다.")
        else:
            print("\n⚠️ 잘못된 번호입니다. 메뉴에 있는 번호(0~7)를 입력해주세요.")

if __name__ == "__main__":
    main()
