# -*- coding: utf-8 -*-


""" 
バーコードリーダから入力された値の数をカウントします。

このアプリの権利は全て影山裕一（兵庫県たつの市）に帰属します。
許可なく改変・再配布することはできません。
お問い合わせはEmail:  kageyama@alicle.jp　へお願いします。 """

# 音を鳴らせるためのライブラリをインポート
from pygame import mixer

# アプリを終了するためのライブラリをインポート
import sys
# アプリの実行時間を測定するためにクロックライブラリをインポート
import time

""" ---------------------------------------------------------
変数定義
--------------------------------------------------------- """
# 読み込まれたバーコードの値を格納するリスト
BarcodeValueArray = []
# 表示バーコードの決められた桁数
BarcodeLength: int = 3


""" ---------------------------------------------------------
バーコード入力を受け付けてリストに格納する処理をする関数
--------------------------------------------------------- """


def BarcodeReading():
    # 動作管理用ステータスを変数として定義
    Status: int = 0
    # 読み込まれたバーコードの数をカウントする変数
    ReadBarcodeQty = 0

    while Status == 0:
        # バーコードを読み込み
        BarcodeValue: str = input('Bar-code >')
        # 読み込まれた値の文字数をカウントする
        ReadValueLength = len(BarcodeValue)

        # 読み込まれた値がBarcodeLengthで規定した桁数と整合すれば実行
        if ReadValueLength == BarcodeLength:
            # 入力された値をリストに追加
            BarcodeValueArray.append(BarcodeValue)
            # print(BarcodeValueArray)

            # 読み込んだバーコードの数を1つアップ
            ReadBarcodeQty = ReadBarcodeQty + 1

            # 読み込んだバーコードの数が20に達したらアラートを出してカウンタを0に戻す
            if ReadBarcodeQty == 20:
                print(ReadBarcodeQty, 'sheets Done!!')
                ReadBarcodeQty = 0
                continue

            # 現在の行を消す
            # sys.stdout.write("\033[2K\033[G")
            # 現在の枚数を表示
            print('Now: ' , ReadBarcodeQty, '\033[1A',end='')

            continue

        # 「q」がタイプされた時はアプリを終了
        elif BarcodeValue == 'q':
            print('Appication has quit.')
            print('Bye!')
            sys.exit()

        # 読み込まれた値がBarcodeLengthで規定した桁数と異なる場合の処理
        elif ReadValueLength != BarcodeLength:
            print('Read error !   Read agein.')
            continue

    return()


""" ---------------------------------------------------------
メイン処理
--------------------------------------------------------- """


def main():
    """ ---------------------------------------------------------
    イニシャル処理
    --------------------------------------------------------- """
    print('Bar-code Counter v0.1.0')
    print('Please read a bar-code.')

    BarcodeReading()


# このファイルがインポートされても勝手に実行されないためのおまじない
if __name__ == "__main__":
    main()
