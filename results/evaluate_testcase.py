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

def _run_once(file: str, in_path: str, language: str):
    try:
        if language == "py":
            cmd = [PYTHON_EXEC, file]
        elif language == "cpp":
            executable = os.path.splitext(file)[0]
            subprocess.run(["g++", "-o", executable, file], check=True, timeout=CUTTIME)
            cmd = [executable]
        elif language == "java":
            print(f"Compiling and running Java file: {file}")
            if os.path.basename(file) != "Main.java":
                temp_file = os.path.join(os.path.dirname(file), "Main.java")
                with open(file, "r", encoding="utf-8", errors="ignore") as fin, \
                     open(temp_file, "w", encoding="utf-8", errors="ignore") as fout:
                    fout.write(fin.read())
                try:
                    subprocess.run(["javac", temp_file], check=True, timeout=CUTTIME)
                    cmd = ["java", "-cp", os.path.dirname(file), "Main"]
                finally:
                    os.remove(temp_file)
            else:
                subprocess.run(["javac", file], check=True, timeout=CUTTIME)
                cmd = ["java", "-cp", os.path.dirname(file), "Main"]
        else:
            raise ValueError(f"Unsupported language: {language}")

        with open(in_path, "rb") as fin:
            start = time.perf_counter()
            proc = subprocess.run(
                cmd,
                stdin=fin,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=CUTTIME
            )
            elapsed = time.perf_counter() - start
        return elapsed, proc.stdout, proc.stderr, proc.returncode, False
    except subprocess.TimeoutExpired:
        print(f"Timeout expired for {file}")
        return CUTTIME, b"", b"", -1, True
    except subprocess.CalledProcessError as e:
        print(f"Compilation or execution error for {file}: {e.stderr.decode('utf-8', errors='ignore')}")
        return CUTTIME, b"", b"", -1, True

def _evaluate_solution(file, input_path, language: str):
    try:
        elapsed, stdout, stderr, returncode, is_timeout = _run_once(file, input_path, language)
        if is_timeout or returncode != 0:
            return None  # Indicates failure
        output = _norm_text(stdout.decode("utf-8", errors="ignore")).lower()
        return output, elapsed, False
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None

def _evaluate_testcase(file_correct, file_buggy, input_folder, output_folder, runs: int = RUNS, language: str = "py"):
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
        print("Input and output files do not match.")
        return None

    names = sorted(input_files.keys(), key=_numeric_sort_key)

    for name in names:
        in_path = input_files[name]
        out_path = output_files[name]

        with open(out_path, "r", encoding="utf-8", errors="ignore") as fexp:
            expected = _norm_text(fexp.read()).lower()

        # Run the correct solution
        elapsed_correct, stdout_correct, stderr_correct, returncode_correct, is_timeout_correct = _run_once(file_correct, in_path, language)
        if is_timeout_correct or returncode_correct != 0:
            print(f"{name}: Correct solution failed (timeout or runtime error).")
            return False

        # Run the buggy solution
        elapsed_buggy, stdout_buggy, stderr_buggy, returncode_buggy, is_timeout_buggy = _run_once(file_buggy, in_path, language)
        if is_timeout_buggy or returncode_buggy != 0:
            print(f"{name}: Buggy solution failed (timeout or runtime error).")
            return False

        # Normalize outputs
        output_correct = _norm_text(stdout_correct.decode("utf-8", errors="ignore")).lower()
        output_buggy = _norm_text(stdout_buggy.decode("utf-8", errors="ignore")).lower()

        # Check if the test case differentiates the solutions
        if output_correct == output_buggy:
            print(f"{name}: Test case failed (outputs are the same).")
            return False

    print("Test case passed (outputs are different).")
    return True


def _evaluate_adv_testcases(adv_dir, correct_solution, buggy_solution, language):
    if not os.path.isdir(adv_dir):
        print(f"Advanced testcases directory not found: {adv_dir}")
        return

    if not os.path.isdir(correct_solution):
        print(f"Correct solution not found: {correct_solution}")
        return

    if not os.path.isdir(buggy_solution):
        print(f"Buggy solution not found: {buggy_solution}")
        return

    summary = {"valid": 0, "invalid": 0, "count": 0}

    for root, _, files in os.walk(adv_dir):
        for file in files:
            if file == "input.txt":
                input_path = os.path.join(root, file)
                summary["count"] += 1
                print(f"Evaluating {input_path}...")
                print(os.path.relpath(input_path, adv_dir))

                task_name = input_path.split(os.sep)[-2]
                contest_name = input_path.split(os.sep)[-3]

                new_correct_solution = os.path.join(correct_solution, contest_name, task_name, "submission_1"+f".{language}")
                new_buggy_solution = os.path.join(buggy_solution, contest_name, task_name, "submission_1"+f".{language}")
                
                # get the 
                if new_correct_solution == "data\\programming_contest\\atCoder\\question_with_images\\grouth_solution_java\\abc417\\e\\submission_1.java":
                    summary["invalid"] += 1
                    continue
                print(f"Correct solution: {new_correct_solution}")

                print(f"Buggy solution: {new_buggy_solution}")

                # Run the correct solution
                correct_res = _evaluate_solution(new_correct_solution, input_path, language)
                if correct_res is None:
                    print(f"Invalid testcase: Error in correct solution for {input_path}")
                    summary["invalid"] += 1
                    continue
                correct_output, correct_time, correct_failed = correct_res

                # Run the buggy solution
                buggy_res = _evaluate_solution(new_buggy_solution, input_path, language)
                if buggy_res is None:
                    print(f"Invalid testcase: Error in buggy solution for {input_path}")
                    summary["invalid"] += 1
                    continue
                buggy_output, buggy_time, buggy_failed = buggy_res

                # Check for runtime cutoff
                if correct_time > CUTTIME or buggy_time > CUTTIME:
                    print(f"Invalid testcase: Runtime exceeded cutoff for {input_path}")
                    summary["invalid"] += 1
                    continue

                # Check if the testcase differentiates the solutions
                if correct_output != buggy_output:
                    print(f"Valid testcase: Differentiates solutions for {input_path}")
                    summary["valid"] += 1
                else:
                    print(f"Invalid testcase: Does not differentiate solutions for {input_path}")
                    summary["invalid"] += 1

                print("================================")

    print(f"Summary for {adv_dir}:")
    print(f"Total testcases: {summary['count']}")
    print(f"Valid: {summary['valid']}, Invalid: {summary['invalid']}")