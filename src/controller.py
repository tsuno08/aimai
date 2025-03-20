from typing import Optional
from .model import CommandModel
from .view import CommandView

class CommandController:
    """モデルとビューを制御するコントローラー"""
    def __init__(self):
        self.model = CommandModel()
        self.view = CommandView()

    def process_command(self, user_input: str) -> Optional[int]:
        """ユーザー入力を処理し、コマンドを実行"""
        try:
            # コマンドの候補を取得
            with self.view.display_loading("コマンドを生成中..."):
                commands = self.model.generate_commands(user_input)

            if not commands:
                self.view.display_error("コマンドの候補を生成できませんでした")
                return None

            # ユーザーにコマンドを選択させる
            selected_index = self.view.display_command_suggestions(commands)
            if selected_index is None:
                return None

            # コマンドを選択
            selected_command = self.model.select_command(selected_index)
            if selected_command is None:
                self.view.display_error("無効なコマンドが選択されました")
                return None

            # 実行の確認と実行
            if self.view.confirm_execution(selected_command):
                return self.model.execute_selected_command()

        except Exception as e:
            self.view.display_error(f"エラーが発生しました: {str(e)}")
            return None

        return None 