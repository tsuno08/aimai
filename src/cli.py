import click
from typing import List
from .controller import CommandController

def main(args: List[str]) -> None:
    """自然言語をシェルコマンドに変換するCLIツール"""
    if not args:
        click.echo("コマンドを入力してください")
        return

    controller = CommandController()
    user_input = " ".join(args)
    controller.process_command(user_input) 