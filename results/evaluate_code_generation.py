# ...existing code...
import os
import sys
import time
import subprocess

CUTTIME = 5  # seconds
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

def _evaluate_solution(py_file, input_folder, output_folder):
    # Collect input/output files and ensure they match
    input_files = {name: os.path.join(input_folder, name)
                   for name in os.listdir(input_folder)
                   if name.endswith(".txt")}
    output_files = {name: os.path.join(output_folder, name)
                    for name in os.listdir(output_folder)
                    if name.endswith(".txt")}

    if not input_files:
        print(f"No input files in: {input_folder}")
        return

    if set(input_files.keys()) != set(output_files.keys()):
        in_names = set(input_files.keys())
        out_names = set(output_files.keys())
        missing_expected = sorted(in_names - out_names, key=_numeric_sort_key)
        missing_inputs = sorted(out_names - in_names, key=_numeric_sort_key)
        if missing_expected:
            print(f"Missing expected outputs for: {', '.join(missing_expected)}")
        if missing_inputs:
            print(f"Missing inputs for: {', '.join(missing_inputs)}")
        return

    names = sorted(input_files.keys(), key=_numeric_sort_key)

    total_time = 0.0
    wrong_no = 0

    for name in names:
        in_path = input_files[name]
        out_path = output_files[name]

        with open(out_path, "r", encoding="utf-8", errors="ignore") as fexp:
            expected = _norm_text(fexp.read()).lower()

        try:
            with open(in_path, "rb") as fin:
                start = time.perf_counter()
                proc = subprocess.run(
                    [PYTHON_EXEC, py_file],
                    stdin=fin,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=CUTTIME
                )
                elapsed = time.perf_counter() - start
            total_time += elapsed
        except subprocess.TimeoutExpired:
            total_time += CUTTIME
            print(f"{name}: timeout (>{CUTTIME}s)")
            wrong_no += 1
            return 1

        if proc.returncode != 0:
            stderr = proc.stderr.decode("utf-8", errors="ignore")
            print(f"{name}: runtime error, stderr:\n{stderr}")
            wrong_no += 1
            return 1

        actual = _norm_text(proc.stdout.decode("utf-8", errors="ignore")).lower()



        if actual != expected:
            # check if float number of each line matches by line, using abs error <= 1e-6
            actual_lines = actual.split("\n")
            expected_lines = expected.split("\n")
            if len(actual_lines) != len(expected_lines):
                print(f"wrong {name}")
                wrong_no += 1
                return 1
            
            # check if each line contain float numbers
            all_float_match = True
            for act_line, exp_line in zip(actual_lines, expected_lines):
                act_parts = act_line.split()
                exp_parts = exp_line.split()
                if len(act_parts) != len(exp_parts):
                    all_float_match = False
                    break
                for act_part, exp_part in zip(act_parts, exp_parts):
                    try:
                        act_num = float(act_part)
                        exp_num = float(exp_part)
                        if abs(act_num - exp_num) > 1e-6:
                            all_float_match = False
                            break
                    except ValueError:
                        all_float_match = False
                        break
                if not all_float_match:
                    break

            if not all_float_match:
                print(f"wrong {name}")
                wrong_no += 1
                return 1
            

    print(f"Total: {len(names)} Wrong: {wrong_no}")
    return wrong_no > 0

def _evaluate_code_generation(code_generation_root, testcase_root, label):
    if not os.path.isdir(code_generation_root):
        print(f"[{label}] code_generation dir not found: {code_generation_root}")
        return
    if not os.path.isdir(testcase_root):
        print(f"[{label}] testcase dir not found: {testcase_root}")
        return
    
    total_wrong = {"en": 0, "jp": 0, "ru":0 , "cn": 0}
    total_question = {"en": 0, "jp": 0, "ru":0 , "cn": 0}

    for subdir in os.listdir(code_generation_root):
        subdir_path = os.path.join(code_generation_root, subdir)
        if not os.path.isdir(subdir_path):
            continue

        for subsubdir in os.listdir(subdir_path):
            subsubdir_path = os.path.join(subdir_path, subsubdir)
            if not os.path.isdir(subsubdir_path):
                continue

            testcase_dir = os.path.join(testcase_root, subdir, subsubdir)
            input_folder = os.path.join(testcase_dir, "input")
            output_folder = os.path.join(testcase_dir, "output")

            if not (os.path.isdir(input_folder) and os.path.isdir(output_folder)):
                print(f"[{label}] Missing input/output for {subdir}/{subsubdir} at {testcase_dir}")
                continue

            for file_name in os.listdir(subsubdir_path):
                if not file_name.endswith(".py"):
                    continue
                py_file = os.path.join(subsubdir_path, file_name)
                print(f"=== [{label}] Evaluating {subdir}/{subsubdir}/{file_name} ===")
                temp = _evaluate_solution(py_file, input_folder, output_folder)
                
                prefix = "jp" if "jp" in file_name.lower() else ("ru" if "ru" in file_name.lower() else ("cn" if "cn" in file_name.lower() else "en"))
                total_wrong[prefix] += 1 if not temp else 0
                total_question[prefix] += 1

    print(f"[{label}] Summary: Total Questions: {total_question}, Total Wrong: {total_wrong}")