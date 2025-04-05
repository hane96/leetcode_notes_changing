import os

def convert_txt_to_md(txt_filename, md_filename):
    with open(txt_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    md_content = ''
    code_block_started = False  #code block finish

    for line in lines:
        #question
        if line.startswith("題目:"):
            if code_block_started: #end code block
                md_content += "```\n"
                code_block_started = False
            md_content += f"\n## {line[3:].strip()}\n"  #add question
        #topic
        elif line.startswith("類型:"):
            md_content += f"**類型:** {line[3:].strip()}\n" #add topic
        #note
        elif line.startswith("筆記:"):
            md_content += f"### 筆記:\n" #add note
        #code block
        elif line.strip() == "程式碼:":
            md_content += "### 程式碼:\n```cpp\n"  #add code block 
            code_block_started = True #code block start
        #skipping blank
        elif line.strip() == "" and code_block_started:
            continue
        #code block
        elif line.startswith("    ") and code_block_started:
            md_content += f"{line.strip()}\n"  

        elif code_block_started:
            md_content += "```\n"
            code_block_started = False
    
        else:
            md_content += line 

    #checking code block ends
    if code_block_started:
        md_content += "```\n"  #finish code block

    #writing md file
    with open(md_filename, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

    print(f"save as {md_filename}")

txt_file = "origin_note.txt"  #txt file name
md_file = "leetcode_notes.md"  #md file name
convert_txt_to_md(txt_file, md_file)
