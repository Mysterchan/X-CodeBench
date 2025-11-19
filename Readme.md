# X-CodeBench: A Comprehensive and Multi-Modal Benchmark for Evaluating Large Language Models in Programming (ESTR4998)

## Overview

X-CodeBench is a comprehensive and multi-modal benchmark designed to evaluate the performance of large language models (LLMs) in programming tasks. It provides a diverse set of tasks and datasets to assess the capabilities of LLMs in code generation, optimization, reasoning, debugging, and translation across multiple programming languages and domains.

## Features

- **Multi-Modal Evaluation**: Includes tasks with and without images, enabling evaluation of LLMs in both textual and visual programming contexts.
- **Diverse Programming Tasks**: Covers code generation, optimization, reasoning, debugging, and translation tasks.
- **Support for Multiple Models**: Benchmarks popular LLMs such as GPT-4, Claude, and others.
- **Extensive Dataset**: Includes datasets from competitive programming platforms like AtCoder and Codeforces, as well as real-world debugging and data science scenarios.
- **Customizable Experiments**: Provides scripts and prompts for running tailored experiments.

## Folder Structure

### `experiment/`
Contains Python scripts for running experiments on various tasks:
- `adv_testcase_with_images.py`: Advanced test cases with images.
- `code_generation_with_images.py`: Code generation tasks with images.
- `code_optimization_without_images.py`: Code optimization tasks without images.
- `prompt_tasks.py`: Prompts for specific tasks.

### `results/`
Stores evaluation results for different models:
- Subfolders for each model (e.g., `gpt-4.1-mini/`, `claude-3-5-haiku-20241022/`).
- Contains results for tasks like `code_debug`, `evaluation`, and `codeforces`.

### `data/`
Includes datasets for benchmarking:
- **Data Science**: Buggy and fixed code with corresponding metadata.
- **Programming Contest**: Questions from AtCoder and Codeforces, with and without images.

## Supported Tasks

- **Code Generation**: Generate code from natural language descriptions.
- **Code Optimization**: Optimize existing code for performance and readability.
- **Code Reasoning**: Solve complex programming problems requiring logical reasoning.
- **Debugging**: Identify and fix bugs in code.
- **Code Translation**: Translate code between different programming languages.

## Contributing

Contributions are welcome! If you have ideas for new tasks, datasets, or features, feel free to open an issue or submit a pull request.
