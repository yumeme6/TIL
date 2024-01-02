#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ダウンロードフォルダ整理用

普段利用していると溜まりがちなダウンロードフォルダを整理。
動画/写真/office系/ゴミ(削除) の4種類にて分類を実施。

移動先のディレクトリはすでに存在しているものとする。

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
        # フォルダ内のファイルに対しループ処理
        for filename in os.listdir(folder_path):
            # ファイルパスを取得
            file_path = os.path.join(folder_path, filename)

            # 指定された拡張子の場合、削除
            if filename.endswith(
                tuple([".zip", ".rar", ".7z", ".exe", ".msi", ".unitypackage"])
            ):
                os.remove(file_path)

            # 指定された拡張子の場合、動画系フォルダに移動
            elif filename.endswith(tuple([".mp4", ".mov", ".mkv"])):
                shutil.move(file_path, os.path.join(folder_path, "動画系"))

            # 指定された拡張子の場合、写真系フォルダに移動
            elif filename.endswith(tuple([".jpg", ".jpeg", ".png", ".gif", ".psd"])):
                shutil.move(file_path, os.path.join(folder_path, "写真系"))

            # 指定された拡張子の場合、office系"フォルダに移動
            elif filename.endswith(
                tuple([".xlsm", ".xlsx", ".xls", ".csv", ".pptx", ".pdf", ".docx"])
            ):
                shutil.move(file_path, os.path.join(folder_path, "office系"))

    # プログラムを終了
    root.destroy()


if __name__ == "__main__":
    main()
