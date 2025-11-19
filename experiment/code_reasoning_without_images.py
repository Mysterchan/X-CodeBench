if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction

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
