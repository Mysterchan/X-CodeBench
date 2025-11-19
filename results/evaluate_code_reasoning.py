# ...existing code...
import os
import sys
import time
import subprocess
import json

CUTTIME = 2  # seconds
PYTHON_EXEC = sys.executable

def _norm_text(s: str) -> str:
    # Normalize EOLs, trim trailing spaces per line, and remove empty lines
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in s.split("\n")]
    lines = [line for line in lines if line.strip() != ""]
    return "\n".join(lines).strip()

def _numeric_sort_key(name: str):
    # Sort "1.txt", "2.txt" numerically by stem, fall back to lexicographic
    stem = os.path.splitext(os.path.basename(name))[0]
    try:
        return (0, int(stem))
    except ValueError:
        return (1, stem.lower())

def _evaluate_code_comparison(output_folder, question_folder, label):
    """Evaluate code reasoning results by comparing outputs to expected outputs."""

    # get all subfolders in output_folder
    total_question = 0
    total_correct = 0
    subfolders = [f.path for f in os.scandir(output_folder) if f.is_dir()]
    for subfolder in subfolders:
        # get all sub_subfolders in subfolder
        sub_subfolders = [f.path for f in os.scandir(subfolder) if f.is_dir()]
        for sub_subfolder in sub_subfolders:
            expected_answer_folder = os.path.join(question_folder, os.path.basename(subfolder), os.path.basename(sub_subfolder), "data.json")

            llm_answer_folder = os.path.join(output_folder, os.path.basename(subfolder), os.path.basename(sub_subfolder), "output.txt")

            with open(expected_answer_folder, "r", encoding="utf-8", errors="ignore") as fexp:
                expected = json.load(fexp)
            
            expected_output = _norm_text(expected["Sample Detail"][0]["output"]).lower()

            with open(llm_answer_folder, "r", encoding="utf-8", errors="ignore") as fllm:
                llm_output = _norm_text(fllm.read()).lower()

            
            # if the llm_output contain the expected output as suffix
            if llm_output.endswith(expected_output):
                total_correct += 1
            
            total_question += 1

    return total_question, total_correct
        