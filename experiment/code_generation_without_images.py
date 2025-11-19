if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .llm.deepseek import DeepSeekChatFunction

from .prompt_tasks import SYSTEM_PROMPT, SYSTEM_PROMPT_JP, SYSTEM_PROMPT_CN, SYSTEM_PROMPT_RU

import json
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv("API_CHAT")

def _message_construct(system_prompt, question_data):
    system_message = system_prompt.replace("{problem_statement}", question_data["Problem Statement"])
    system_message = system_message.replace("{constraints}", question_data["Constraints"])
    system_message = system_message.replace("{io_styles}", question_data["IO Styles"])

    samples_formatted = ""
    for idx, sample in enumerate(question_data["Sample Detail"]):
        samples_formatted += f"Sample Input {idx+1}:\n{sample['input']}Sample Output {idx+1}:\n{sample['output']}Explanation:{sample['explanation']}\n"

    # find "new_notes" in question_data key
    if "Notes" in question_data:
        samples_formatted += f"{question_data['Notes']}\n"

    system_message = system_message.replace("{samples}", samples_formatted)

    messages = [
        {
            "role": "system",
            "content": system_message,
        },
    ]
    return messages

def _message_code_parse(response_content):
    code_start = response_content.find("```python")
    if code_start == -1:
        return response_content.strip()
    code_start += len("```python")
    code_end = response_content.find("```", code_start)
    if code_end == -1:
        return response_content[code_start:].strip()
    code = response_content[code_start:code_end].strip()
    return code

if __name__ == "__main__":
    model_names = ["o4-mini", "claude-3-5-haiku-20241022"]
    dataset = "question_wo_images"
    tasks = "questions"
    res_name = "code_generation"
    platform = "atCoder"

    for model_name in model_names:
        model = ChatGPTChatFunction(model=model_name, openai_key= API_KEY, temperature=0)

        question_dir = os.path.join("data", "programming_contest", platform, dataset, tasks)
        result_dir = os.path.join("results", model_name, platform, dataset, res_name)
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        for fd in os.listdir(question_dir):
            fd_path =  os.path.join(question_dir, fd)
            if not os.path.isdir(fd_path):
                continue

            for sub_fd in os.listdir(fd_path):
                sub_fd_path = os.path.join(fd_path, sub_fd)
                if not os.path.isdir(sub_fd_path):
                    continue

                print(f"Processing {fd}/{sub_fd}...")
                question_files = [f for f in os.listdir(sub_fd_path) if f.endswith(".json")]
        
                for qf in question_files:
                    # pass if exists
                    if os.path.exists(os.path.join(result_dir, fd, sub_fd, qf.replace(".json", ".py"))):
                        continue

                    # select the system prompt based on language
                    if "cn" in qf:
                        system_prompt = SYSTEM_PROMPT_CN
                    elif "jp" in qf:
                        system_prompt = SYSTEM_PROMPT_JP
                    elif "ru" in qf:
                        system_prompt = SYSTEM_PROMPT_RU
                    else:
                        system_prompt = SYSTEM_PROMPT

                    print(os.path.join(sub_fd_path, qf))
                    with open(os.path.join(sub_fd_path, qf), "r", encoding="utf-8") as f:
                        question_data = json.load(f)
                    
                    messages = _message_construct(system_prompt, question_data)
                    model.conversation_history = messages
                    response_message, _, total_tokens = model.parse()

                    code = _message_code_parse(response_message["content"])
                    question_name = qf.replace(".json", "")
                    if not os.path.exists(os.path.join(result_dir, fd, sub_fd)):
                        os.makedirs(os.path.join(result_dir, fd, sub_fd))

                    with open(os.path.join(result_dir, fd, sub_fd, f"{question_name}.py"), "w", encoding="utf-8") as f:
                        f.write(code)
