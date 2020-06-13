# -*- coding: utf-8 -*-


""" 
バーコードリーダから入力された値の数をカウントします。

このアプリの権利は全て影山裕一（兵庫県たつの市）及びAlice Electronicsに帰属します。
許可なく改変・再配布することはできません。
お問い合わせはEmail:  contact@alicle.jp　へお願いします。 """


# 音を鳴らせるためのライブラリをインポート
from pygame import mixer

# アプリを終了するためのライブラリをインポート
import sys
# ディレクトリ操作をするためのライブラリをインポート
import os


""" ---------------------------------------------------------
変数定義
--------------------------------------------------------- """
# 読み込まれたバーコードの値を格納するリスト
BarcodeValueArray = []
# 表示バーコードの桁数定義する変数（初期値は5）
BarcodeLength: int = 5
# カウント数を定義する変数（初期値は5）
NumberOfCount: int = 5

""" ---------------------------------------------------------
バーコード入力を受け付けてリストに格納する処理をする関数
--------------------------------------------------------- """


def BarcodeReading():
    # 動作管理用ステータスを変数として定義
    Status: int = 0
    # 読み込まれたバーコードの数をカウントする変数
    ReadBarcodeQty = 0

    # バーコードの桁数を設定
    print('\033[2K', 'How many digits in the barcode?')
    BarcodeLength = input('> ')
    # 入力された値を整数に変換
    BarcodeLength = int(BarcodeLength)
    # カウント数を設定
    print('\033[2A', 'How many to count?')

    NumberOfCount = input('> ')
    # 入力された値を整数に変換
    NumberOfCount = int(NumberOfCount)

    # 設定メッセージを削除
    print('\033[2K', '\033[A', '\033[2K', '\033[A', '\033[2K', '\033[A')

    # 設定完了のメッセージ
    print('\033[2K', 'Setting Done. \n Please read a bar-code.')

    # pygameライブラリで効果音を再生するための初期化処理
    mixer.init()

    while Status == 0:

        # コンソールの表示をクリア
        sys.stdout.write('\033[2K')
        # バーコードを読み込み
        BarcodeValue: str = input(' Bar-code >')
        # 読み込まれた値の文字数をカウントする
        ReadValueLength = len(BarcodeValue)

        # 読み込まれた値がBarcodeLengthで規定した桁数と整合すれば実行
        if ReadValueLength == BarcodeLength:
            # 入力された値をリストに追加
            BarcodeValueArray.append(BarcodeValue)
            # print(BarcodeValueArray)

            # 読み込んだバーコードの数を1つアップ
            ReadBarcodeQty = ReadBarcodeQty + 1

            # 読み込んだバーコードの数が設定値に達したらアラートを出してカウンタを0に戻す
            if ReadBarcodeQty == NumberOfCount:
                # カウント完了の効果音を再生
                mixer.Sound('lib/alarm.wav').play()

                print('\033[2K', ReadBarcodeQty, 'sheets Done !', '\033[2A')
                ReadBarcodeQty = 0

                continue

            # 読み込みの効果音を再生
            mixer.music.load('lib/beep.mp3')
            mixer.music.play(1)

            # 現在の行を消す
            # sys.stdout.write("\033[2K\033[G")
            # 現在の枚数を表示し、カーソルを1行戻す
            print('\033[2K', 'Now: ', ReadBarcodeQty, '\033[2A',)

            continue

        # 「q」がタイプされた時はアプリを終了
        elif BarcodeValue == 'q':

            # 読み込んだ値をファイルに出力（追記で出力する）
            d = '\n'.join(BarcodeValueArray)
            with open('Data/data.txt', 'a') as f:
                f.write(d)

            # データファイルの最後に改行を追加
            # データ出力ファイルの初期処理
            with open('Data/data.txt', 'a') as f:
                f.write('\n')

            print('\033[2K', 'Appication has quit.')
            print('\033[2K', 'Bye!')
            sys.exit()

        # 読み込まれた値がBarcodeLengthで規定した桁数と異なる場合の処理
        elif ReadValueLength != BarcodeLength:
            print('\033[2K', 'Read error !   Read agein.', '\033[2A')
            continue

    return()


""" ---------------------------------------------------------
メイン処理
--------------------------------------------------------- """


def main():
    """ ---------------------------------------------------------
    イニシャル処理
    --------------------------------------------------------- """

    # 画面消去
    print('\033[2J', '\033[1;1H')

    # pygameライブラリの初期メッセージを削除
    print('\033[2A')
    print('\033[K', '\033[A', '\033[K')
    print('\033[2A')

    # データ保存用のディレクトリが存在しなければ作成
    if not os.path.isdir('Data'):
        os.makedirs('Data')

    # アプリの初期メッセージを表示
    print('\033[A', '[Bar-code Counter v0.1.0]')

    BarcodeReading()


# このファイルがインポートされても勝手に実行されないためのおまじない
if __name__ == "__main__":
    main()
