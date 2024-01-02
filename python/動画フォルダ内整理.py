#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""動画フォルダ整理用

実写映像か2次元アニメ映像かを判断し、分類を実施する。
現状ではファイル名で区別しているため、正確な分類はできていない。

Todo:
    * 機械学習を実施し、ジャンル別に分別が行える用にする。

"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog


def main():
    # フォルダを選択するダイアログボックスを表示
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="フォルダを選択してください")

    # フォルダが指定されている場合、処理を実行
    if folder_path:
        # 移動先のpath
        MMD_folder = os.path.join(folder_path, "MMD")

        # フォルダ内の全ファイルが対象
        for filename in os.listdir(folder_path):
            # .mp4拡張子かつ、ファイル名に"_Source"が含まれている場合
            if filename.endswith(".mp4") and "_source" in filename.lower():
                # 対象ファイルのpathと移動先のpathを取得
                file_path = os.path.join(folder_path, filename)

                # ファイルを移動
                shutil.move(file_path, os.path.join(MMD_folder, filename))

    # プログラムを終了
    root.destroy()


if __name__ == "__main__":
    main()
