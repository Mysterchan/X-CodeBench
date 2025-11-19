# ...existing code...
import os
import sys
import time
import subprocess

CUTTIME = 2  # seconds
PYTHON_EXEC = sys.executable
RUNS = 1  # number of runs per input per program

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

def _run_once(py_file: str, in_path: str):
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
        return elapsed, proc.stdout, proc.stderr, proc.returncode, False
    except subprocess.TimeoutExpired:
        return CUTTIME, b"", b"", -1, True

def _evaluate_solution(py_file, input_folder, output_folder, runs: int = RUNS, stop_on_fail: bool = True, is_optimized: bool = False):
    # Collect input/output files and ensure they match
    input_files = {name: os.path.join(input_folder, name)
                   for name in os.listdir(input_folder)
                   if name.endswith(".txt")}
    output_files = {name: os.path.join(output_folder, name)
                    for name in os.listdir(output_folder)
                    if name.endswith(".txt")}

    if not input_files:
        print(f"No input files in: {input_folder}")
        return None

    if set(input_files.keys()) != set(output_files.keys()):
        in_names = set(input_files.keys())
        out_names = set(output_files.keys())
        missing_expected = sorted(in_names - out_names, key=_numeric_sort_key)
        missing_inputs = sorted(out_names - in_names, key=_numeric_sort_key)
        if missing_expected:
            print(f"Missing expected outputs for: {', '.join(missing_expected)}")
        if missing_inputs:
            print(f"Missing inputs for: {', '.join(missing_inputs)}")
        return None

    names = sorted(input_files.keys(), key=_numeric_sort_key)

    total_time = 0.0
    wrong_no = 0

    for name in names:
        in_path = input_files[name]
        out_path = output_files[name]

        with open(out_path, "r", encoding="utf-8", errors="ignore") as fexp:
            expected = _norm_text(fexp.read()).lower()

        # First run: measure + validate
        elapsed, stdout, stderr, returncode, is_timeout = _run_once(py_file, in_path)
        total_time += elapsed if not is_timeout else CUTTIME

        if is_timeout:
            print(f"{name}: timeout (>{CUTTIME}s)")
            wrong_no += 1
            if is_optimized:
                print("Optimized code failed due to timeout.")
                return wrong_no, None, True  # Fail the comparison for optimized code
        elif returncode != 0:
            err = stderr.decode("utf-8", errors="ignore")
            print(f"{name}: runtime error, stderr:\n{err}")
            wrong_no += 1
            if is_optimized:
                print("Optimized code failed due to runtime error.")
                return wrong_no, None, True  # Fail the comparison for optimized code
        else:
            actual = _norm_text(stdout.decode("utf-8", errors="ignore")).lower()
            if actual != expected:
                print(f"wrong {name}")
                wrong_no += 1
                if is_optimized:
                    print("Optimized code failed due to incorrect output.")
                    return wrong_no, None, True  # Fail the comparison for optimized code

        # For original code, treat failures as correct by adding CUTTIME
        if not is_optimized and (is_timeout or returncode != 0 or actual != expected):
            print(f"{name}: Original code failed, treating as correct with CUTTIME.")
            total_time += CUTTIME

        # Additional runs: measure only
        for _ in range(runs - 1):
            elapsed2, _, _, _, timeout2 = _run_once(py_file, in_path)
            total_time += elapsed2 if not timeout2 else CUTTIME

    avg_time = total_time / (len(names) * runs)
    print(f"Total: {len(names)} Wrong: {wrong_no} AvgTime: {avg_time:.6f}s")
    return wrong_no, avg_time, False

def _evaluate_code_comparison(optimized_root, original_root, testcase_root, label, runs: int = RUNS):
    if not os.path.isdir(optimized_root):
        print(f"[{label}] optimized dir not found: {optimized_root}")
        return
    if not os.path.isdir(original_root):
        print(f"[{label}] original dir not found: {original_root}")
        return
    if not os.path.isdir(testcase_root):
        print(f"[{label}] testcase dir not found: {testcase_root}")
        return

    summary = {"faster": 0, "slower": 0, "same": 0, "count": 0, "speedups": []}

    for subdir in os.listdir(optimized_root):
        subdir_path = os.path.join(optimized_root, subdir)
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

            orig_dir = os.path.join(original_root, subdir, subsubdir)
            if not os.path.isdir(orig_dir):
                print(f"[{label}] Original dir not found for {subdir}/{subsubdir}: {orig_dir}")
                continue

            # Choose original .py (first sorted)
            orig_candidates = sorted([f for f in os.listdir(orig_dir) if f.endswith(".py")])
            if not orig_candidates:
                print(f"[{label}] No original .py in {orig_dir}")
                continue
            orig_py = os.path.join(orig_dir, orig_candidates[0])

            for file_name in os.listdir(subsubdir_path):
                if not file_name.endswith(".py"):
                    continue
                opt_py = os.path.join(subsubdir_path, file_name)
                print(f"=== [{label}] Evaluating {subdir}/{subsubdir} ===")
                print(f"Original: {os.path.basename(orig_py)}")
                # ...existing code...
                orig_res = _evaluate_solution(orig_py, input_folder, output_folder, runs, is_optimized=False)
                if orig_res is None:
                    print("Skip: invalid testcases or original evaluation failed early.")
                    continue
                orig_wrong, orig_avg, orig_failed = orig_res
                if orig_failed or orig_avg is None:
                    print("Original failed (timeout/runtime error/incorrect output). Skipping comparison.")
                    continue

                opt_res = _evaluate_solution(opt_py, input_folder, output_folder, runs, is_optimized=True)
                if opt_res is None:
                    print("Skip: invalid testcases or optimized evaluation failed early.")
                    continue
                opt_wrong, opt_avg, opt_failed = opt_res
                if opt_failed or opt_avg is None:
                    print("Optimized failed (timeout/runtime error/incorrect output). Counting as failure and skipping comparison.")
                    continue
                # ...existing code...
                # Comparison only when both sides succeeded
                speedup = (orig_avg / opt_avg) if opt_avg > 0 else float("inf")
                summary["speedups"].append(speedup)
                summary["count"] += 1

                if abs(orig_avg - opt_avg) < 1e-9:
                    summary["same"] += 1
                    comp = "same"
                elif opt_avg < orig_avg:
                    summary["faster"] += 1
                    comp = "faster"
                else:
                    summary["slower"] += 1
                    comp = "slower"

                print(f"Result: orig_avg={orig_avg:.6f}s opt_avg={opt_avg:.6f}s speedup={speedup:.3f}x "
                      f"(opt is {comp}); wrong(orig,opt)=({orig_wrong},{opt_wrong})")


def main():
    model_names = ["gpt-4o-mini"]

    cur_dir = os.path.dirname(os.path.abspath(__file__))

    languages = ["py", "cpp", "java"]

    for model_name in model_names:
        model_dir = os.path.join(cur_dir, model_name)

        atcoder_dir = os.path.join(model_dir, "atCoder")
        atcoder_question_wo_images_dir = os.path.join(atcoder_dir, "question_wo_images")
        atcoder_question_w_images_dir = os.path.join(atcoder_dir, "question_with_images")

        codeforces_dir = os.path.join(model_dir, "codeforces")
        codeforces_question_w_images_dir = os.path.join(codeforces_dir, "question_with_images")

        atcoder_question_w_images_testcase_dir = os.path.join("data", "programming_contest", "atCoder", "question_with_images", "testcases")
        atcoder_question_wo_images_testcase_dir = os.path.join("data", "programming_contest", "atCoder", "question_wo_images", "testcases")
        codeforces_question_w_images_testcase_dir = os.path.join("data", "programming_contest", "codeforces", "question_with_images", "testcases")

        # For each language, compare optimized vs original
        for language in languages:
            ext = "TLE_solution" + (f"_{language}" if language != "cpp" else "")

            original_atcoder_wo = os.path.join("data", "programming_contest", "atCoder", "question_wo_images", ext)
            original_atcoder_w = os.path.join("data", "programming_contest", "atCoder", "question_with_images", ext)
            original_codeforces_w = os.path.join("data", "programming_contest", "codeforces", "question_with_images", ext)

            optimized_atcoder_wo = os.path.join(atcoder_question_wo_images_dir, "code_optimization", language)
            optimized_atcoder_w = os.path.join(atcoder_question_w_images_dir, "code_optimization", language)
            optimized_codeforces_w = os.path.join(codeforces_question_w_images_dir, "code_optimization", language)

            # AtCoder, wo_images
            _evaluate_code_comparison(
                optimized_atcoder_wo, original_atcoder_wo, atcoder_question_wo_images_testcase_dir, f"atcoder_wo_images_{language}", RUNS
            )
            # AtCoder, w_images
            _evaluate_code_comparison(
                optimized_atcoder_w, original_atcoder_w, atcoder_question_w_images_testcase_dir, f"atcoder_w_images_{language}", RUNS
            )
            # Codeforces, w_images
            _evaluate_code_comparison(
                optimized_codeforces_w, original_codeforces_w, codeforces_question_w_images_testcase_dir, f"codeforces_w_images_{language}", RUNS
            )

if __name__ == "__main__":
    main()
# ...existing code...