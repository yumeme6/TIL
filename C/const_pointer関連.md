# const/pointer 関連情報

__NOTE__: Information taken from
- [変数の const 付け方一覧](https://qiita.com/go_astrayer/items/63e8a059ae20a5d5e000)
- [ポインタ型に付ける const は型名の後ろに付くと考えると憶えやすい](https://qiita.com/yuki12/items/06c85af2735ddefd5666)

## 目次
- [const/pointer 関連情報](#constpointer-関連情報)
  - [目次](#目次)
  - [結論](#結論)
  - [非ポインタ型変数の const](#非ポインタ型変数の-const)
  - [ポインタ型変数の const](#ポインタ型変数の-const)
  - [ダブルポインタ型変数の const](#ダブルポインタ型変数の-const)
  - [余談](#余談)



## 結論

| const | 修飾先   | 動作 |
| :---: | :------: | :--: |
| (*)の前 | ポインタ先を修飾 | ポインタ先(値)の変更不可 |
| (*)の後 | ポインタ型そのものを修飾 | アドレスの変更不可 |

| <div style="text-align: center;">ポインタ宣言</div> | ポインタ<br>(アドレス) | 実体<br>(値)  | <div style="text-align: center;">備考</div> |
| ---------: | :------: | :------: | :------: |
| T* D | ⭕ | ⭕ |
| `const` T* D | ⭕ | ❌ |
| T `const`* D | ⭕ | ❌ | 同上 |
| `const` T `const`* D | 🚫 | 🚫 | Error
| T* `const` D | ❌ | ⭕ |
| `const` T* `const` D | ❌ | ❌ |
| T `const`* `const` D | ❌ | ❌ | 同上 |
| `const` T `const`* `const` D | 🚫 | 🚫 | Error

| <div style="text-align: center;">ダブルポインタ宣言</div> | ポインタのポインタ<br>(アドレス)   | ポインタ<br>(アドレス) | 実体<br>(値)  |
| ---------: | :------: | :------: | :------: |
| T** D | ⭕ | ⭕ | ⭕ |  |
| `const` T** D | ⭕ | ⭕ | ❌ | 
| T* `const`* D | ⭕ | ❌ | ⭕ | 
| T** `const` D | ❌ | ⭕ | ⭕ | 
| `const` T* `const`* D | ❌ | ❌ | ⭕ |
| `const` T** `const` D| ❌ | ⭕ | ❌ |
| T* `const`* `const` D| ⭕ | ❌ | ❌ |
| `const` T* `const`* `const` D| ❌ | ❌ | ❌ |

## 非ポインタ型変数の const

値の書き換え禁止❌

```c
uint16_t lw_value       = 10;

/* constの位置はどちらでも可 */
const uint16_t lw_const = 10;
uint16_t const lw_const = 10;  

lw_value = 100; // OK
lw_const = 100; // Error
```

## ポインタ型変数の const

代表3ケースを紹介する。
- `const` uint16_t*
- uint16_t* `const`
- `const` uint16_t* `const`


### `const` uint16_t* 変数名

ポインタ変数(アドレス)は変更可能 ⭕  
ポインタ先の実体(値)は変更不可 ❌

```c
uint16_t fw_value = 10;

void main(void) {
    
    const uint16_t *lwp_const = &fw_value;

    lwp_const  = &fw_value; // OK
    *lwp_const = fw_value;  // Error
}
```

### uint16_t* `const` 変数名

ポインタ変数(アドレス)は変更不可 ❌  
ポインタ先の実体(値)は変更可能 ⭕

```c
uint16_t fw_value = 10;

void main(void) {
    uint16_t *const lwp_const = &fw_value;

    lwp_const  = &fw_value; // Error
    *lwp_const = fw_value;  // OK
}
```

### `const` uint16_t* `const` 変数名

ポインタ変数(アドレス)は変更不可 ❌  
ポインタ先の実体(値)は変更不可 ❌

```c
uint16_t fw_value = 10;

void main(void) {
    const uint16_t *const lwp_const = &fw_value;

    lwp_const  = &fw_value; // Error
    *lwp_const = 100;       // Error
}
```

## ダブルポインタ型変数の const

代表3ケースを紹介する。 残りのパターンは下記の組み合わせであるため省略する。
- `const` uint16_t**
- uint16_t* `const`*
- uint16_t** `const`

### `const` uint16_t** 変数名

ポインタ先の実体(値)は変更不可 ❌

```c
uint16_t lw_val   = (uint16_t)1;
uint16_t *lwp_Ptr = &lw_val;
const uint16_t **lwpp_doublePtr;

lwpp_doublePtr   = &lwp_Ptr; // OK
*lwpp_doublePtr  = lwp_Ptr;  // OK
**lwpp_doublePtr = 10;       // Error
```

### uint16_t* `const`* 変数名

ポインタ変数(アドレス)は変更不可 ❌
```c
uint16_t lw_val   = (uint16_t)1;
uint16_t *lwp_Ptr = &lw_val;
uint16_t *const *lwpp_doublePtr;

lwpp_doublePtr   = &lwp_Ptr; // OK
*lwpp_doublePtr  = lwp_Ptr;  // Error
**lwpp_doublePtr = 10;       // OK
```

### uint16_t** `const` 変数名

ダブルポインタ変数(アドレス)は変更不可 ❌
```c
uint16_t lw_val   = (uint16_t)1;
uint16_t *lwp_Ptr = &lw_val;
uint16_t **const lwpp_doublePtr;

lwpp_doublePtr   = &lwp_Ptr; // Error
*lwpp_doublePtr  = lwp_Ptr;  // OK
**lwpp_doublePtr = 10;       // OK
```

## 余談
本資料はあくまでポインタに対しアクセスする際のconstの影響をまとめた資料である。  
定義時点でコンパイルエラーが発生するパターンもあるのでご注意ください。

また、constとは関係ないが、下記表現には気を付けてください。
```c
int* p, q; // p:pointer, q:int
```