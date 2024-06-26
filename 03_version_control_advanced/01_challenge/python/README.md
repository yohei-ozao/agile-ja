# チャレンジ 1: バージョン管理 (発展) (Pythonバージョン)

# はじめに

このチャレンジは、Git の高度な機能 (ブランチ作成、マージ、ローカルとリモートのリポジトリ間でのプッシュ/プルなど) についての知識を確認すると同時に、理解を深めることを目的として作られています。チャレンジに含まれている一連のタスクでは、Git と GitHub のさまざまな機能を効果的に活用する必要があります。

このチャレンジでは、摂氏から華氏または華氏から摂氏に温度を変換する簡単な Python プログラムに取り組みます。提供されるプロジェクトテンプレートには摂氏から華氏に変換する関数が含まれており、この関数はユーザーが入力した値を受け取って処理し、変換結果を含むメッセージを出力します。

# タスク

## タスク 1: tconv.py のクローンと更新

このタスクでは、このフォルダにある `tconv.py` に変更を加えます。

ファイルの場所: `03_version_control_advanced\01_challenge\python\tconv.py`

1. このリポジトリを自分のマシンにクローンします。
2. ブランチ `fahrenheit-to-celsius` を作成し、そのブランチに切り替えます。
3. `tconv.py` の中に、華氏から摂氏に温度を変換する関数 `convert_fahrenheit_to_celsius` を書きます。温度の変換には `C = 5/9 * (F - 32)` という数式を使用します。
4. 変更をステージング領域に追加してコミットします。
5. ブランチ `fahrenheit-to-celsius` をリモートリポジトリにプッシュします。
6. ブランチ `fahrenheit-to-celsius` からブランチ `main` にプルリクエスト (PR) を作成し、変更内容を PR の説明に明記します。その際、必ず自分の名前を入力してください。

## タスク 2: プログラムの実行

1. ブランチ `fahrenheit-to-celsius` をローカルの `main` ブランチにマージします。
2. ブランチ `execute-program` を作成し、そのブランチに切り替えます。
3. 関数 `main` に次の処理を実行するコードを追加します。

- 「Enter c if you want to convert from Fahrenheit to Celsius」(華氏から摂氏に変換したい場合は c と入力してください) というメッセージを出力します。
- 「Enter f if you want to convert from Celsius to Fahrenheit」(摂氏から華氏に変換したい場合は f と入力してください) というメッセージを出力します。
- ユーザーの入力をチェックし、次の処理を実行します。
  - ユーザーが `c` と入力した場合は、関数 `convert_fahrenheit_to_celsius` を呼び出します。
  - ユーザーが `f` と入力した場合は、関数 `convert_celsius_to_fahrenheit` を呼び出します。
  - ユーザーが `c` でも `f` でもない値を入力した場合は、「Incorrect input. Please try again later」(無効な入力です。後でもう一度お試しください) というメッセージを出力します。

4. 変更をステージング領域に追加してコミットします。
5. `main` ブランチに戻ります。
6. 次のコードを追加します。

```python
def main():
  convert_fahrenheit_to_celsius()
  convert_celsius_to_fahrenheit()
 

main()
```

7. 変更をステージング領域に追加してコミットします。
8. `execute-program` ブランチを `main` ブランチにマージします。
9. マージコンフリクトが発生した場合は、作成した `main` バージョンを維持するようにコンフリクトを解消します。
10. マージコンフリクトが解消したら、`execute-program` ブランチをリモートリポジトリにプッシュします。
11. ブランチ `execute-program` からブランチ `main` にプルリクエスト (PR) を作成し、変更内容を PR の説明に明記します。その際、必ず自分の名前を入力してください。

## (任意) タスク 3 : プログラムの拡張

1. `enhancements` ブランチを作成し、そのブランチに切り替えます。
2. このプログラムをさらに便利にする拡張機能を考案します。たとえば、次のような拡張機能が考えられます。
   - ケルビンと華氏、ケルビンと摂氏との変換関数を追加する
   - ユーザーが無効な値を入力した場合、有効な値が入力されるまでプログラムを自動的に繰り返し実行する
   - Python モジュール `time` を使って出力メッセージの間に一時停止を追加し、データを処理する実際のプログラムをバックグラウンドでシミュレートしてから応答を送信する
3. `enhancements` ブランチをリモートリポジトリにプッシュします。
4. ブランチ `enhancements` からブランチ `main` にプルリクエスト (PR) を作成し、変更内容を PR の説明に明記します。その際、必ず自分の名前を入力してください。

## 提出するもの

- 最後に作業したタスクのために作成したブランチのURLを提出してください。
