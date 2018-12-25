import sys

# https://qiita.com/nel215/items/cc3722a1f2d8ce217d42

def exe():
    del sys.modules['package']
    del sys.modules['package.module_a']
    del sys.modules['package.sub_package']
    del sys.modules['package.sub_package.module_b']


# importlib.reload ではダメだった...


#
# 大事
#

# import した時と python でした時で
# トップレベルモジュール, パッケージが変わる
# なんで変えたんだろう....


# __package__ と __name__ の組み合わせでトップレベルモジュール, パッケージを
# 判定している様子。
# トップレベルモジュール, パッケージとは実行時のディレクトリ？
# この辺の概念か...
# https://docs.python.jp/3/reference/import.html#__package__

# スクリプトとして実行するとは何か？

# トップレベルモジュールとは？
