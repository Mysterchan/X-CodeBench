if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .prompt_translation import (SYSTEM_PROMPT_EN_RU, SYSTEM_PROMPT_RU_EN, SYSTEM_PROMPT_EN_JP, SYSTEM_PROMPT_JP_EN, SYSTEM_PROMPT_EN_CN,
                                    USER_PROMPT_EN_RU, USER_PROMPT_RU_EN, USER_PROMPT_EN_JP, USER_PROMPT_JP_EN, USER_PROMPT_EN_CN)
    

import json
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv("API_CHAT")

def _message_construct(user_prompt, system_prompt, statement):
    user_prompt = user_prompt.replace("{statement}", statement)
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]
    return messages

def _translate_statement(model, messages):
    model.conversation_history = messages
    response_message, _, total_tokens = model.parse()
    response_message = response_message["content"]
    return response_message
