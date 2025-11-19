if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .prompt_tasks import SYSTEM_PROMPT_CODE_OPTIMIZATION

import json
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv("API_CHAT")

def _message_construct(question_data, unoptimized_code):
    system_message = SYSTEM_PROMPT_CODE_OPTIMIZATION.replace("{problem_statement}", question_data["Problem Statement"])
    system_message = system_message.replace("{constraints}", question_data["Constraints"])
    system_message = system_message.replace("{io_styles}", question_data["IO Styles"])

    samples_formatted = ""
    for idx, sample in enumerate(question_data["Sample Detail"]):
        samples_formatted += f"Sample Input {idx+1}:\n{sample['input']}Sample Output {idx+1}:\n{sample['output']}Explanation:{sample['explanation']}\n"

    # find "new_notes" in question_data key
    if "Notes" in question_data:
        samples_formatted += f"{question_data['Notes']}\n"

    system_message = system_message.replace("{samples}", samples_formatted)

    system_message = system_message.replace("{inefficient_code}", unoptimized_code)

    messages = [
        {
            "role": "user",
            "content": system_message,
        },
    ]
    return messages

def _message_code_parse(response_content):
    if "```python" in response_content: 
        code_start = response_content.find("```python")
        code_start += len("```python")
        code_end = response_content.find("```", code_start)
        if code_end == -1:
            code = response_content[code_start:].strip()
        else:
            code = response_content[code_start:code_end].strip()

        return code
    
    if "```cpp" in response_content: 
        code_start = response_content.find("```cpp")
        code_start += len("```cpp")
        code_end = response_content.find("```", code_start)
        if code_end == -1:
            code = response_content[code_start:].strip()
        else:
            code = response_content[code_start:code_end].strip()

        return code

    if "```java" in response_content: 
        code_start = response_content.find("```java")
        code_start += len("```java")
        code_end = response_content.find("```", code_start)
        if code_end == -1:
            code = response_content[code_start:].strip()
        else:
            code = response_content[code_start:code_end].strip()

        return code
    

    return response_content.strip()