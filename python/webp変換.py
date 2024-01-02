#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""モジュールの説明タイトル

* ソースコードの一番始めに記載すること
* importより前に記載する

Todo:
    TODOリストを記載
    * conf.pyの``sphinx.ext.todo`` を有効にしないと使用できない
    * conf.pyの``todo_include_todos = True``にしないと表示されない

"""

import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from multiprocessing import Pool


def convert_webp_to_png(webp_file):
    """Webp画像を変換処理

    webp→pngで変換を実施
    変換前画像については削除を行う。

    Args:
        webp_file (str): ファイルpath

    Returns:
        return:
    """

    # 出力ファイル名を取得
    png_file = os.path.splitext(webp_file)[0] + ".png"

    # 画像を読み込む
    try:
        webp_image = Image.open(webp_file)
    except Exception as e:
        # 画像の読み込みに失敗した場合はNoneを返す
        return None

    # 画像を保存
    webp_image.save(png_file, "PNG")
    webp_image.close()

    # 画像を削除する
    os.remove(webp_file)

    # 変換した画像を返す
    return png_file


# フォルダ内のWebp画像を処理する関数
def process_folder(folder_selected):
    """フォルダ内の画像を処理

    並列化処理でやろうとしているが、現状はミスが存在。

    Args:
        folder_selected (str): フォルダpath

    Returns:

    """
    # フォルダ内のWebp画像を取得
    webp_files = [
        os.path.join(folder_selected, f)
        for f in os.listdir(folder_selected)
        if f.endswith(".webp")
    ]

    # CPUの最大数でプロセスプールを作成
    pool = Pool(os.cpu_count())

    # プールで並列処理
    results = pool.map(convert_webp_to_png, webp_files)

    # プールを終了
    pool.close()
    pool.join()

    return results


# フォルダを選択
root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

# フォルダ内のWebp画像を処理
results = process_folder(folder_selected)

# 処理が完了したことを表示
if results:
    print("処理が完了しました。")

# メインウィンドウを閉じる
root.destroy()
