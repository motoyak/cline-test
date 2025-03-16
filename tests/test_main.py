"""mainモジュールのテスト。"""

from unittest.mock import patch

from src.main import main


@patch("src.chat_app.ChatApp")
def test_main(mock_chat_app):
    """mainメソッドをテストする。"""
    # モックインスタンスを設定
    mock_app = mock_chat_app.return_value

    main()

    # ChatAppが正しく初期化されたことを確認
    assert mock_chat_app.call_count == 1, "ChatAppが初期化されていません"

    # launchメソッドが呼び出されたことを確認
    assert mock_app.launch.call_count == 1, "launchメソッドが呼び出されていません"
