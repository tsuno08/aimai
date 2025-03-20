# Aimai CLI

自然言語をシェルコマンドに変換する CLI ツール。Google Generative AI (Gemini 1.5 Flash) を使用して、日本語の指示をシェルコマンドに変換します。

## 特徴

- 日本語の自然な指示をシェルコマンドに変換
- 矢印キーで簡単にコマンドを選択
- 複数のコマンド候補から選択可能
- 実行前の確認機能

## インストール

```bash
git clone https://github.com/yourusername/gemini-command.git
cd gemini-command
pip install -r requirements.txt

# Google API Keyを設定
export GOOGLE_API_KEY="your-api-key"
```

## 使い方

```bash
# コマンドを実行
aimai "ファイル一覧を表示"
aimai "Documentsディレクトリに移動"
aimai "test.txtを作成"
```

操作方法：

- ↑/↓: コマンドの選択
- Enter: 選択したコマンドを確定
- q: キャンセル

## ディレクトリ構造

```
.
├── bin/
│   └── aimai          # 実行スクリプト
├── src/
│   ├── cli.py         # CLIエントリーポイント
│   ├── model.py       # データとビジネスロジック
│   ├── view.py        # 出力フォーマット
│   └── controller.py  # ユーザー入力の処理
├── requirements.txt
└── README.md
```

## 依存関係

- Python 3.8+
- google-generativeai: Gemini API クライアント
- click: CLI インターフェース
- rich: リッチなターミナル出力
- prompt_toolkit: インタラクティブなコマンド選択
- python-dotenv: 環境変数管理
