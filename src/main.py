"""チャットアプリケーションのエントリーポイント。"""

from src.chat_app import ChatApp


def main():
    """アプリケーションのメインエントリーポイント。"""
    app = ChatApp()
    app.launch()


if __name__ == "__main__":
    main()
