if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .llm.deepseek import DeepSeekChatFunction

from .prompt_tasks import SYSTEM_PROMPT_CODE_REASONING_FEW_SHOT

import json
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv("API_CHAT")

def _message_construct(question_data, code):
    system_message = SYSTEM_PROMPT_CODE_REASONING_FEW_SHOT.replace("{problem_statement}", question_data["Problem Statement"])
    system_message = system_message.replace("{constraints}", question_data["Constraints"])
    system_message = system_message.replace("{io_styles}", question_data["IO Styles"])

    system_message = system_message.replace("{code}", code)

    input_ = question_data["Sample Detail"][0]["input"]

    system_message = system_message.replace("{input}", input_)

    messages = [
        {
            "role": "user",
            "content": system_message,
        },
    ]
    return messages

def _message_code_parse(response_content):
    if response_content.count("```") >= 2:
        parts = response_content.split("```")
        code = "\n".join(parts[-2].split("\n")[1:-1])
        return code
    
    return response_content.strip()

if __name__ == "__main__":
    model_names = ["gpt-4.1-mini", "gemini-2.5-flash-nothinking", "o4-mini", "claude-3-5-haiku-20241022"]
    dataset = "question_wo_images"
    tasks = "questions"
    res_name = "code_reasoning"
    platform = "atCoder"
    languages = ["py", "cpp", "java"]


    for model_name in model_names:
        model = ChatGPTChatFunction(model=model_name, openai_key= API_KEY, temperature=0)
        for language in languages:

            question_dir = os.path.join("data", "programming_contest", platform, dataset, tasks)
            result_dir = os.path.join("results", model_name, platform, dataset, res_name, language)

            extension = "grouth_solution"
            if language != "cpp":
                extension += "_" +language
            
            code_dir = os.path.join("data", "programming_contest", platform, dataset, extension)

            if not os.path.exists(result_dir):
                os.makedirs(result_dir)

            for fd in os.listdir(code_dir):
                fd_path =  os.path.join(code_dir, fd)
                if not os.path.isdir(fd_path):
                    continue

                for sub_fd in os.listdir(fd_path):
                    sub_fd_path = os.path.join(fd_path, sub_fd)
                    if not os.path.isdir(sub_fd_path):
                        continue

                    print(f"Processing {fd}/{sub_fd}...")
                    question_files = [f for f in os.listdir(sub_fd_path) if f.endswith(f".{language}") and "1" in f]
            
                    for qf in question_files:
                        # pass if exists
                        if os.path.exists(os.path.join(result_dir, fd, sub_fd, "output.txt")):
                            continue

                        print(os.path.join(sub_fd_path, qf))
                        print(os.path.join(question_dir, fd, sub_fd, "data.json"))

                        # get the question_data:
                        question_json_path = os.path.join(question_dir, fd, sub_fd, "data.json")
                        with open(question_json_path, "r", encoding="utf-8") as f:
                            question_data = json.load(f)

                        # get the unoptimized code
                        code_path = os.path.join(sub_fd_path, qf)
                        with open(code_path, "r", encoding="utf-8") as f:
                            unoptimized_code = f.read()
                        
                        messages = _message_construct(question_data, unoptimized_code)
                        model.conversation_history = messages

                        response_message, _, total_tokens = model.parse()

                        code = _message_code_parse(response_message["content"])
                        question_name = qf.replace(".json", "")
                        if not os.path.exists(os.path.join(result_dir, fd, sub_fd)):
                            os.makedirs(os.path.join(result_dir, fd, sub_fd))

                        with open(os.path.join(result_dir, fd, sub_fd, "output.txt"), "w", encoding="utf-8") as f:
                            f.write(code)
