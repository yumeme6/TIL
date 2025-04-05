#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ダウンロードフォルダ整理用

普段利用していると溜まりがちなダウンロードフォルダを整理。
動画/写真/office系/ゴミ(削除) の4種類にて分類を実施。

移動先のディレクトリはすでに存在しているものとする。

"""

import os
import shutil
import re


# ======== 拡張子の定義 ========
DELETE_EXTS = (".zip", ".rar", ".7z", ".exe", ".msi", ".unitypackage", ".htm")
VIDEO_EXTS = (".mp4", ".mov", ".mkv")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".gif", ".psd")
OFFICE_EXTS = (".xlsm", ".xlsx", ".xls", ".csv", ".pptx", ".pdf", ".docx")


# ======== フォルダの定義 ========
DOWNLOAD_FOLDER = r"Downloads"
VIDEO_FOLDER = r"Videos\動画系"


def main():
    for filename in os.listdir(DOWNLOAD_FOLDER):
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)

        if not os.path.isfile(file_path):
            continue

        # ❌ 削除対象
        if filename.endswith(DELETE_EXTS):
            os.remove(file_path)

        # 🎥 動画:ファイル名に日付パターン
        elif filename.endswith(VIDEO_EXTS) and re.search(
            r"\d{2}-\d{2}-\d{2}", filename
        ):
            target = os.path.join(VIDEO_FOLDER, "FC")
            os.makedirs(target, exist_ok=True)
            shutil.move(file_path, target)

        # 🎞️ 動画:通常
        elif filename.endswith(VIDEO_EXTS):
            target = os.path.join(VIDEO_FOLDER, "動画系")
            os.makedirs(target, exist_ok=True)
            shutil.move(file_path, target)

        # 🖼️ 写真系
        elif filename.endswith(IMAGE_EXTS):
            target = os.path.join(DOWNLOAD_FOLDER, "写真系")
            os.makedirs(target, exist_ok=True)
            shutil.move(file_path, target)

        # 📄 Office系
        elif filename.endswith(OFFICE_EXTS):
            target = os.path.join(DOWNLOAD_FOLDER, "office系")
            os.makedirs(target, exist_ok=True)
            shutil.move(file_path, target)


if __name__ == "__main__":
    main()
