import os
import json

CONFIG_FILE = "config.json"
LANGUAGE_DIR = "language"

def choose_language():
    languages = [f for f in os.listdir(LANGUAGE_DIR) if f.endswith('.json')]
    print("请选择语言 / Please select a language:")
    for idx, lang_file in enumerate(languages, 1):
        print(f"{idx}. {lang_file}")
    while True:
        choice = input("输入序号 / Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(languages):
            return languages[int(choice) - 1]
        else:
            print("无效选择，请重新输入 / Invalid choice, try again.")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def load_language(lang_file):
    with open(os.path.join(LANGUAGE_DIR, lang_file), "r", encoding="utf-8") as f:
        return json.load(f)

# 检查配置文件和语言设置
config = load_config()
if "language" not in config:
    lang_file = choose_language()
    config["language"] = lang_file
    save_config(config)
else:
    lang_file = config["language"]

lang = load_language(lang_file)

input_path = input(lang.get("input_path", "Please enter the input path:"))
output_path = input(lang.get("output_path", "Please input the output path:"))

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    lines = infile.readlines()
    if lines:
        outfile.write(lines[0])  # 保留标题行
        for idx, line in enumerate(lines[1:], start=1):
            outfile.write(f"{idx}: {line}")
print(lang.get("done", "处理完成，结果已保存"))
