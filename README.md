# leetcode_notes_changing

## convert.py

寫給自己用的小工具，把我的leetcode txt筆記轉成markdown，更好在github上面觀看

將特定格式的txt_file轉成md_file

## origin_note.txt

我的原始筆記檔案

## leetcode_notes.md

轉換後的md檔

## 用途

### 原始筆記格式:

題目: question

類型: topic1, topic2

筆記:

testing

123

程式碼:

    cout<<"hi";

### 轉換後:

## question
**類型:** topic1, topic2
### 筆記:
testing
123
### 程式碼:
```cpp
    count<<"hi";

```

##備註

- 程式碼區塊目前固定以1個tab(4個空格)開頭，才會被正確辨識
- 如果程式結尾沒加上\`\`\`markdown格式會亂掉，已經修正過會自動補上結尾
- 未來可能會在增加目錄, 自動分類或其他功能
