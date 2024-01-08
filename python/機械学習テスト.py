#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""機械学習用テスト

動画整理用の機械学習

本コードはメモリ20GB以上使用します。

使用:OpenCV,NumPy,TensorFlow,Keras

Todo:
    * CUDAを使用する用にする。

Bag:
    * 44.2 GiBのメモリ不足状態

"""

import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from sklearn.model_selection import train_test_split

# フレームごとの画像サイズ
img_size = (128, 128)


def get_frames(video_path):
    """動画ファイルからフレームを取得する関数

    Parameters:
    - video_path (str): 動画ファイルのpath

    Returns:
    - frames (list): フレームのリスト
    """
    frames = []  # フレームを格納するリスト
    print(f"処理開始：{os.path.basename(video_path)}")
    cap = cv2.VideoCapture(video_path)  # OpenCVで動画を開く

    while True:
        ret, frame = cap.read()  # フレームを1枚ずつ読み込む
        if not ret:
            break
        frame = cv2.resize(frame, img_size)  # リサイズ
        frames.append(frame)

    cap.release()
    return frames


def create_labeled_data(folder_path, label):
    """ラベル付きデータを作成する関数

    Parameters:
    - folder_path (str): フォルダのpath
    - label (int): ラベル

    Returns:
    - data (list): データのリスト
    - labels (list): ラベルのリスト
    """
    data = []
    labels = []

    # フォルダ内の全ての動画ファイルに対して処理
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            frames = get_frames(video_path)  # 動画からフレームを取得
            video_data = [img_to_array(frame) for frame in frames]  # フレームをNumPy配列に変換
            data.extend(video_data)
            labels.extend([label] * len(video_data))

    print("ラベルデータ読み込み完了")

    return data, labels


def build_model():
    """CNNモデルを構築する関数

    Returns:
    - model (tensorflow.keras.models.Sequential): 構築したモデル
    """
    model = models.Sequential()
    model.add(
        layers.Conv2D(
            16, (3, 3), activation="relu", input_shape=(img_size[0], img_size[1], 3)
        )
    )
    model.add(layers.MaxPooling2D((4, 4)))
    model.add(layers.Conv2D(32, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D((4, 4)))
    model.add(layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D((4, 4)))
    model.add(layers.Flatten())
    model.add(layers.Dense(32, activation="relu"))
    model.add(layers.Dense(1, activation="sigmoid"))

    return model


# 学習元データの読み込み
live_data, live_labels = create_labeled_data("python/training/live", label=0)
anime_data, anime_labels = create_labeled_data("python/training/anime", label=1)
cg_data, cg_labels = create_labeled_data("python/training/cg", label=2)

# 学習データを結合し、シャッフル
all_data = live_data + anime_data + cg_data
all_labels = live_labels + anime_labels + cg_labels
combined_data = list(zip(all_data, all_labels))
np.random.shuffle(combined_data)
all_data, all_labels = zip(*combined_data)

#  データをNumPy配列に変換し、ピクセル値を0から1の範囲にスケーリング
all_data = np.array(all_data) / 255.0
all_labels = np.array(all_labels)

# 訓練データとテストデータに分割
train_data, test_data, train_labels, test_labels = train_test_split(
    all_data, all_labels, test_size=0.2, random_state=42
)

# モデルを構築
model = build_model()

# モデルをコンパイルし、損失関数とオプティマイザを指定
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# モデルの訓練 (モデルをコンパイルし、損失関数とオプティマイザを指定)
model.fit(
    train_data,
    train_labels,
    epochs=10,
    validation_data=(test_data, test_labels),
    batch_size=32,
)

# モデルの保存（Keras形式）
model.save("python/model", save_format="tf")
