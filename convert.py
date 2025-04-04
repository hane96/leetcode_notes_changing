import os

def convert_txt_to_md(txt_filename, md_filename):
    with open(txt_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    md_content = ''
    code_block_started = False  # 記錄程式碼區塊是否開始

    for line in lines:
        # 處理題目
        if line.startswith("題目:"):
            # 如果程式碼區塊已經開始了，結束它
            if code_block_started:
                md_content += "```\n"  # 結束程式碼區塊
                code_block_started = False
            md_content += f"\n## {line[3:].strip()}\n"  # 顯示題目
        # 處理類型
        elif line.startswith("類型:"):
            md_content += f"**類型:** {line[3:].strip()}\n"
        # 處理筆記
        elif line.startswith("筆記:"):
            md_content += f"### 筆記:\n"
        # 處理程式碼區塊的開始
        elif line.strip() == "程式碼:":
            md_content += "### 程式碼:\n```cpp\n"  # 開始程式碼區塊
            code_block_started = True
        # 略過空行並處理程式碼內容
        elif line.strip() == "" and code_block_started:
            continue  # 略過程式碼區塊中的空行
        # 處理程式碼行
        elif line.startswith("    ") and code_block_started:
            md_content += f"{line.strip()}\n"  # 添加程式碼行
        # 其他情況下結束程式碼區塊
        elif code_block_started:
            md_content += "```\n"  # 結束程式碼區塊
            code_block_started = False
        # 其他內容直接添加
        else:
            md_content += line  # 保證筆記內容不會被跳過

    # 在最後檢查是否有未結束的程式碼區塊
    if code_block_started:
        md_content += "```\n"  # 結束程式碼區塊

    # 儲存為 md 文件
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

    print(f"save as {md_filename}")

# 轉換
txt_file = "origin_note.txt"  # txt 檔案
md_file = "leetcode_notes.md"  # md 檔案
convert_txt_to_md(txt_file, md_file)
