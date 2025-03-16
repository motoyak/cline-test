"""ChatAppのテスト。"""

from unittest.mock import MagicMock, patch

import pytest

from src.chat_app import ChatApp


@pytest.fixture
def chat_app():
    """ChatAppのフィクスチャ。"""
    return ChatApp()


def test_chat_app_initialization(chat_app):
    """ChatAppの初期化をテストする。"""
    assert chat_app.response_generator is not None, (
        "ResponseGeneratorが初期化されていません"
    )
    assert chat_app.interface is None, "インターフェースが初期化前に設定されています"


def test_respond(chat_app):
    """respondメソッドをテストする。"""
    # ResponseGeneratorのgenerate_responseメソッドをモック化
    chat_app.response_generator.generate_response = MagicMock(return_value="テスト応答")

    response = chat_app.respond("こんにちは", [])

    # モック化したメソッドが呼び出されたことを確認
    chat_app.response_generator.generate_response.assert_called_once_with("こんにちは")
    assert response == "テスト応答", "応答が正しく返されていません"


@patch("gradio.ChatInterface")
def test_launch(mock_chat_interface, chat_app):
    """launchメソッドをテストする。"""
    # モックインスタンスを設定
    mock_interface = MagicMock()
    mock_chat_interface.return_value = mock_interface

    chat_app.launch()

    # ChatInterfaceが正しく初期化されたことを確認
    assert mock_chat_interface.call_count == 1, "ChatInterfaceが初期化されていません"

    # launchメソッドが呼び出されたことを確認
    assert mock_interface.launch.call_count == 1, "launchメソッドが呼び出されていません"
