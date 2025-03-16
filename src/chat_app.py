"""Gradioを使用したチャットアプリケーション。"""

from typing import List, Tuple

import gradio as gr

from src.response_generator import ResponseGenerator


class ChatApp:
    """Gradioを使用したチャットアプリケーションのメインクラス。

    このクラスは、Gradioインターフェースを初期化し、ユーザー入力を処理して
    ResponseGeneratorを使用して応答を生成します。
    """

    def __init__(self):
        """ChatAppを初期化する。

        ResponseGeneratorを初期化し、Gradioインターフェースを設定します。
        """
        self.response_generator = ResponseGenerator()
        self.interface = None

    def respond(self, message: str, history: List[Tuple[str, str]]) -> str:
        """ユーザーメッセージに対する応答を生成する。

        Args:
            message: ユーザーが入力したメッセージ
            history: これまでのチャット履歴

        Returns:
            生成された応答メッセージ
        """
        return self.response_generator.generate_response(message)

    def launch(self, share: bool = False) -> None:
        """Gradioインターフェースを起動する。

        Args:
            share: Trueの場合、一時的な公開URLを生成する
        """
        self.interface = gr.ChatInterface(
            fn=self.respond,
            title="シンプルチャットアプリ",
            description="メッセージを入力すると、AIが相槌を返します。",
            examples=["こんにちは", "今日の天気はどうですか？", "趣味は何ですか？"],
            theme=gr.themes.Soft(),
        )
        self.interface.launch(share=share)
