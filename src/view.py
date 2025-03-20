from typing import List, Optional
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from prompt_toolkit import prompt
from prompt_toolkit.keys import Keys
from prompt_toolkit.key_binding import KeyBindings

class CommandView:
    """ユーザーインターフェースを担当するビュー"""
    def __init__(self):
        self.console = Console()

    def display_error(self, message: str) -> None:
        """エラーメッセージを表示"""
        self.console.print(f"[red]{message}[/red]")

    def display_loading(self, message: str):
        """ローディング表示を返す"""
        return self.console.status(f"[bold green]{message}[/bold green]")

    def _display_commands(self, commands: List[str], selected_index: int) -> None:
        """コマンドの一覧を表示"""
        self.console.clear()
        table = Table(title="利用可能なコマンド")
        table.add_column("", justify="right", style="cyan")
        table.add_column("コマンド", style="green")
        
        for i, cmd in enumerate(commands):
            cursor = ">" if i == selected_index else " "
            table.add_row(cursor, cmd)
        
        self.console.print(table)
        self.console.print("\n[bold]↑/↓: 選択  Enter: 決定  q: キャンセル[/bold]")

    def display_command_suggestions(self, commands: List[str]) -> Optional[int]:
        """コマンドの候補を表示し、選択されたインデックスを返す"""
        if not commands:
            return None

        selected_index = 0
        self._display_commands(commands, selected_index)

        kb = KeyBindings()
        result = {"index": selected_index, "done": False}

        @kb.add("up")
        def _(event):
            result["index"] = (result["index"] - 1) % len(commands)
            self._display_commands(commands, result["index"])

        @kb.add("down")
        def _(event):
            result["index"] = (result["index"] + 1) % len(commands)
            self._display_commands(commands, result["index"])

        @kb.add("enter")
        def _(event):
            result["done"] = True
            event.app.exit()

        @kb.add("q")
        def _(event):
            result["index"] = None
            result["done"] = True
            event.app.exit()

        prompt("", key_bindings=kb, default="")

        return result["index"] if result["done"] else None

    def confirm_execution(self, command: str) -> bool:
        """コマンド実行の確認を取得"""
        return Prompt.ask(
            f"このコマンドを実行しますか？ [green]{command}[/green]",
            choices=["y", "n"],
            default="n"
        ) == "y" 