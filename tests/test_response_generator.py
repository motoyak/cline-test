"""ResponseGeneratorのテスト。"""

from src.response_generator import ResponseGenerator


def test_response_generator_initialization():
    """ResponseGeneratorの初期化をテストする。"""
    generator = ResponseGenerator()
    assert len(generator.responses) > 0, "応答パターンが初期化されていません"


def test_generate_response():
    """generate_responseメソッドをテストする。"""
    generator = ResponseGenerator()
    response = generator.generate_response("こんにちは")
    assert response in generator.responses, (
        "生成された応答が応答パターンに含まれていません"
    )
