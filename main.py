# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

for i in range(10):
    print(i)
    print_hello()


def print_hello():
    print('hello')

def print_hi(name):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    print_hi('PyCharm')
# test
# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
