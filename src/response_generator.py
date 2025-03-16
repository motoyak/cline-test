"""相槌を生成するモジュール。"""

import random
from typing import List


class ResponseGenerator:
    """ユーザー入力に対する相槌を生成するクラス。

    このクラスは、ユーザーの入力に対して適切な相槌をランダムに選択して返します。
    """

    def __init__(self):
        """ResponseGeneratorを初期化する。

        相槌のパターンを初期化します。
        """
        self.responses: List[str] = [
            "なるほど、それは興味深いですね。",
            "確かに、その通りですね。",
            "へぇ、そうなんですか？",
            "それで、それからどうなりましたか？",
            "もう少し詳しく教えていただけますか？",
            "それは素晴らしいですね！",
            "そうですね、理解できます。",
            "本当ですか？それは驚きました。",
            "なるほど、参考になります。",
            "それは考えさせられますね。",
        ]

    def generate_response(self, user_input: str) -> str:
        """ユーザー入力に対する相槌を生成する。

        Args:
            user_input: ユーザーが入力したメッセージ

        Returns:
            ランダムに選択された相槌
        """
        # 現在はユーザー入力の内容に関わらずランダムに相槌を選択
        return random.choice(self.responses)
