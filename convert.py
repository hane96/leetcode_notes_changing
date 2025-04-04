import os

def convert_txt_to_md(txt_filename, md_filename):
    with open(txt_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    md_content = ''
    i = 0
    while i < len(lines):
        line = lines[i]

        # 讀取題目
        if line.startswith("題目:"):
            title = line[3:].strip()
            md_content += f"## 題目: [{title}](https://leetcode.com/problems/{title.lower().replace(' ', '-')}/)\n"
        
        # 讀取類型
        elif line.startswith("類型:"):
            tags = line[3:].strip()
            md_content += f"**類型:** {tags}\n\n"
        
        # 讀取筆記
        elif line.startswith("筆記:"):
            note = ""
            i += 1
            while i < len(lines) and lines[i].strip() != "程式碼:":
                note += lines[i].strip() + "  \n"  # 每行筆記加兩個空格換行
                i += 1
            md_content += f"### 筆記:\n{note}\n\n"
        
        # 讀取程式碼
        elif line.strip() == "程式碼:":
            code = ""
            i += 1
            while i < len(lines) and lines[i].strip() != "":
                code += lines[i]
                i += 1
            md_content += f"### 程式碼:\n```cpp\n{code}\n```\n\n"

        i += 1

    # 保存成 markdown 文件
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

    print(f"save as {md_filename}")

# 使用範例
txt_file = "origin_note.txt"  # txt 檔案
md_file = "leetcode_notes.md"  # md 檔案
convert_txt_to_md(txt_file, md_file)
