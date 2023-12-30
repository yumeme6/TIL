# static const 関連情報

## 目次

- [static const 関連情報](#static-const-関連情報)
  - [目次](#目次)
  - [はじめに](#はじめに)
  - [static (修飾子)](#static-修飾子)
  - [const (型修飾子)](#const-型修飾子)
  - [static const](#static-const)
  - [余談](#余談)

## はじめに

未経験者に多いですが、static と const は別物である認識を持った上でご確認ください。
基礎的な知識を持っている方向けのため、記載はある程度省略しています。

|  宣言  |  指定子 / 修飾子   |      説明      |
| :----: | :----------------: | :------------: |
| static | 記憶域クラス指定子 |    静的宣言    |
| const  |      型修飾子      | 値の変更が不可 |

## static (修飾子)

静的宣言です。

```c
void ReqValCnt() {
    static uint16_t sw_counter = 0;
    sw_counter++;
}

ReqValCnt(); //sw_counter:1
ReqValCnt(); //sw_counter:2
ReqValCnt(); //sw_counter:3
```

## const (型修飾子)

不変です。

```c
const uint16_t lw_const = 10;

lw_const = 100; // Error
```

## static const

static + const のため、特段何かあるわけではない。

難しく考えた際に罠に陥りがちではあるが、static に似た利用法の認識で概ね間違えではない。  
基本的には配列宣言の際に使用するケースが多いイメージ。

```c
static const uint16_t swr_sample_ad[] = {1U, 2U};
```

## 余談

static は使用できる場合は使用しましょう。
