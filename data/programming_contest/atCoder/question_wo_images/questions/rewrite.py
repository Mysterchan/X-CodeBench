import os
import json

# cur_dir 

cur_dir = os.path.dirname(os.path.abspath(__file__))

# get all folders in cur_dir
folders = [f for f in os.listdir(cur_dir) if os.path.isdir(os.path.join(cur_dir, f))]
for fd in folders:

    # get all folders in fd
    sub_folders = [sf for sf in os.listdir(os.path.join(cur_dir, fd)) if os.path.isdir(os.path.join(cur_dir, fd, sf))]

    for sub_fd in sub_folders:
        print(f"Processing {fd}/{sub_fd}...")
        # get data_cn.json
        data_cn_path = os.path.join(cur_dir, fd, sub_fd, "data_cn.json")
        if os.path.exists(data_cn_path):
            print("Found data_cn.json")
            with open(data_cn_path, "r", encoding="utf-8") as f:
                data_cn = json.load(f)
            
            data = {}
            data["Title"] = data_cn.get("title", "")
            data["Source"] = data_cn.get("source", "")
            data["Name"] = data_cn.get("name", "")
            data["Time Limit"] = data_cn.get("time_limit", "")
            data["Memory Limit"] = data_cn.get("memory_limit", "")
            data["Problem Statement"] = data_cn.get("new_statement", "")
            data["Statement Images"] = data_cn.get("statement_images", [])
            data["Constraints"] = data_cn.get("new_constraints", "")
            data["IO Styles"] = data_cn.get("new_io_styles", "")
            temp = data_cn.get("sample_detail", "")
            data["Sample Detail"] = []
            for sample in temp:
                data["Sample Detail"].append({
                    "input": sample.get("input", ""),
                    "output": sample.get("output", ""),
                    "explanation": sample.get("new_explanation_html", ""),
                    "images": sample.get("images", [])
                })

            data["Language"] = "cn"

            # write to data.json
            data_path = os.path.join(cur_dir, fd, sub_fd, "data_cn.json")
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        # get data.json
        data_path = os.path.join(cur_dir, fd, sub_fd, "data.json")
        if os.path.exists(data_path):
            print("Found data.json")
            with open(data_path, "r", encoding="utf-8") as f:
                data_en = json.load(f)
            
            data = {}
            data["Title"] = data_en.get("title", "")
            data["Source"] = data_en.get("source", "")
            data["Name"] = data_en.get("name", "")
            data["Time Limit"] = data_en.get("time_limit", "")
            data["Memory Limit"] = data_en.get("memory_limit", "")
            data["Problem Statement"] = data_en.get("new_statement", "")
            data["Statement Images"] = data_en.get("statement_images", [])
            data["Constraints"] = data_en.get("new_constraints", "")
            data["IO Styles"] = data_en.get("new_io_styles", "")
            temp = data_en.get("sample_detail", "")
            data["Sample Detail"] = []
            for sample in temp:
                data["Sample Detail"].append({
                    "input": sample.get("input", ""),
                    "output": sample.get("output", ""),
                    "explanation": sample.get("new_explanation_html", ""),
                    "images": sample.get("images", [])
                })

            data["Language"] = "en"

        
            # write to data.json
            data_path = os.path.join(cur_dir, fd, sub_fd, "data.json")
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        
        # get data_jp.json
        data_jp_path = os.path.join(cur_dir, fd, sub_fd, "data_jp.json")
        if os.path.exists(data_jp_path):
            print("Found data_jp.json")
            with open(data_jp_path, "r", encoding="utf-8") as f:
                data_jp = json.load(f)
            
            data = {}
            data["Title"] = data_jp.get("title", "")
            data["Source"] = data_jp.get("source", "")
            data["Name"] = data_jp.get("name", "")
            data["Time Limit"] = data_jp.get("time_limit", "")
            data["Memory Limit"] = data_jp.get("memory_limit", "")
            data["Problem Statement"] = data_jp.get("new_statement", "")
            data["Statement Images"] = data_jp.get("statement_images", [])
            data["Constraints"] = data_jp.get("new_constraints", "")
            data["IO Styles"] = data_jp.get("new_io_styles", "")
            temp = data_jp.get("sample_detail", "")
            data["Sample Detail"] = []
            for sample in temp:
                data["Sample Detail"].append({
                    "input": sample.get("input", ""),
                    "output": sample.get("output", ""),
                    "explanation": sample.get("new_explanation_html", ""),
                    "images": sample.get("images", [])
                })

            data["Language"] = "jp"

            # write to data.json
            data_path = os.path.join(cur_dir, fd, sub_fd, "data_jp.json")
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        # get data_ru.json

        data_ru_path = os.path.join(cur_dir, fd, sub_fd, "data_ru.json")
        if os.path.exists(data_ru_path):
            print("Found data_ru.json")
            with open(data_ru_path, "r", encoding="utf-8") as f:
                data_ru = json.load(f)
            
            data = {}
            data["Title"] = data_ru.get("title", "")
            data["Source"] = data_ru.get("source", "")
            data["Name"] = data_ru.get("name", "")
            data["Time Limit"] = data_ru.get("time_limit", "")
            data["Memory Limit"] = data_ru.get("memory_limit", "")
            data["Problem Statement"] = data_ru.get("new_statement", "")
            data["Statement Images"] = data_ru.get("statement_images", [])
            data["Constraints"] = data_ru.get("new_constraints", "")
            data["IO Styles"] = data_ru.get("new_io_styles", "")
            temp = data_ru.get("sample_detail", "")
            data["Sample Detail"] = []
            for sample in temp:
                data["Sample Detail"].append({
                    "input": sample.get("input", ""),
                    "output": sample.get("output", ""),
                    "explanation": str(sample.get("new_explanation_html", "")),
                    "images": sample.get("images", [])
                })

            data["Language"] = "ru"

            # write to data.json
            data_path = os.path.join(cur_dir, fd, sub_fd, "data_ru.json")
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            

            