import os

def convert_txt_to_md(txt_filename, md_filename):
    with open(txt_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    md_content = ''
    code_block_started = False
    for line in lines:
        # 處理題目
        if line.startswith("題目:"):
            md_content += f"## {line[3:].strip()}\n"
        # 處理類型
        elif line.startswith("類型:"):
            md_content += f"**類型:** {line[3:].strip()}\n"
        # 處理筆記
        elif line.startswith("筆記:"):
            md_content += f"### 筆記:\n"
        # 處理程式碼
        elif line.strip() == "程式碼:":
            md_content += "### 程式碼:\n```cpp\n"
            code_block_started = True
        elif line.strip() == "" and code_block_started:
            continue  # 忽略程式碼區塊開始前的空行
        elif line.startswith("    ") and code_block_started:
            md_content += f"{line.strip()}\n"
        elif code_block_started:
            md_content += "```\n"
            code_block_started = False
        else:
            md_content += line  # 這裡保證筆記內容不會被跳過

    # 儲存為 md 文件
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

    print(f"save as {md_filename}")

# 轉換
txt_file = "origin_note.txt"  # txt 檔案
md_file = "leetcode_notes.md"  # md 檔案
convert_txt_to_md(txt_file, md_file)
