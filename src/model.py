import os
from typing import List, Optional
from dataclasses import dataclass
import google.generativeai as genai
from dotenv import load_dotenv

@dataclass
class Command:
    """コマンドデータクラス"""
    command_str: str

class CommandModel:
    """シェルコマンド生成と実行を担当するモデル"""
    def __init__(self):
        self._initialize_gemini()
        self._commands: List[Command] = []
        self._selected_command: Optional[Command] = None

    def _initialize_gemini(self) -> None:
        """Gemini APIの初期化"""
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        genai.configure(api_key=api_key)
        self._model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_commands(self, user_input: str) -> List[str]:
        """自然言語をコマンドの候補に変換"""
        prompt = f"""
        あなたはシェルコマンドの変換を行うアシスタントです。
        以下の自然言語の入力を適切なシェルコマンドに変換してください。
        3つの候補を提案してください。
        各候補は改行で区切り、コマンドのみを返してください。
        説明は不要です。
        コマンドは実行可能な形式で返してください。

        入力: {user_input}
        """
        
        try:
            response = self._model.generate_content(prompt)
            if not response.text:
                return []
            command_strs = [cmd.strip() for cmd in response.text.strip().split("\n") if cmd.strip()]
            self._commands = [Command(cmd_str) for cmd_str in command_strs]
            return command_strs
        except Exception as e:
            print(f"Error generating commands: {str(e)}")
            return []

    def select_command(self, index: int) -> Optional[str]:
        """コマンドを選択"""
        if 0 <= index < len(self._commands):
            self._selected_command = self._commands[index]
            return self._selected_command.command_str
        return None

    def execute_selected_command(self) -> int:
        """選択されたコマンドを実行"""
        if self._selected_command is None:
            raise ValueError("No command selected")
        return os.system(self._selected_command.command_str) 