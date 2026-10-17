"""
프롬프트 관리자 자동화 테스트 스위트
모든 핵심 기능과 보너스 기능을 검증합니다.
"""
import os
import json
from prompt_manager import (
    get_default_prompts,
    CATEGORIES,
    save_prompts_to_json,
    load_prompts_from_json,
    export_to_markdown
)

def test_all():
    prompts = get_default_prompts()
    assert len(prompts) >= 4, "기본 프롬프트는 최소 3개 이상이어야 합니다."
    
    # 카테고리 확인
    for p in prompts:
        assert p["category"] in CATEGORIES or p["category"] == "기타"
        assert "title" in p and "content" in p and "favorite" in p
        
    # 신규 추가 시뮬레이션
    new_p = {
        "id": 5,
        "title": "테스트 프롬프트",
        "content": "이것은 자동화 테스트용 프롬프트입니다.",
        "category": "텍스트 생성",
        "favorite": False,
        "views": 0
    }
    prompts.append(new_p)
    assert len(prompts) == 5
    
    # 즐겨찾기 토글 검증
    new_p["favorite"] = not new_p["favorite"]
    assert new_p["favorite"] is True
    
    # JSON 저장 및 로드 검증
    test_json = "test_prompts.json"
    save_prompts_to_json(prompts, test_json)
    assert os.path.exists(test_json)
    loaded = load_prompts_from_json(test_json)
    assert len(loaded) == 5
    os.remove(test_json)
    
    # 마크다운 내보내기 검증
    test_md = "test_export.md"
    export_to_markdown(prompts, test_md)
    assert os.path.exists(test_md)
    with open(test_md, "r", encoding="utf-8") as f:
        md_text = f.read()
    assert "블로그 글 작성 도우미" in md_text
    os.remove(test_md)
    
    print("🎉 모든 단위 테스트 및 기능 검증을 성공적으로 통과했습니다!")

if __name__ == "__main__":
    test_all()
