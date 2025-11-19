if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
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