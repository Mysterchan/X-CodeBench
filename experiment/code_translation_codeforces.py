if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .llm.deepseek import DeepSeekChatFunction

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


if __name__ == "__main__":
    model_name = "gpt-4o-mini"
    dataset = "question_with_images"
    platform = "codeforces"
    
    source_lang = "en"
    destination_lang = "jp"

    if destination_lang == "ru":
        SYSTEM_PROMPT = SYSTEM_PROMPT_EN_RU
        USER_PROMPT = USER_PROMPT_EN_RU
    
    elif destination_lang == "jp":
        SYSTEM_PROMPT = SYSTEM_PROMPT_EN_JP
        USER_PROMPT = USER_PROMPT_EN_JP

    elif destination_lang == "cn":
        SYSTEM_PROMPT = SYSTEM_PROMPT_EN_CN
        USER_PROMPT = USER_PROMPT_EN_CN

    elif source_lang == "ru" and destination_lang == "en":
        SYSTEM_PROMPT = SYSTEM_PROMPT_RU_EN
        USER_PROMPT = USER_PROMPT_RU_EN

    elif source_lang == "jp" and destination_lang == "en":
        SYSTEM_PROMPT = SYSTEM_PROMPT_JP_EN
        USER_PROMPT = USER_PROMPT_JP_EN

    model = ChatGPTChatFunction(model=model_name, openai_key= API_KEY, temperature=0)
    question_dir = os.path.join("data_construction", "programming_contest", platform, dataset, "questions")

    contest_dirs = [d for d in os.listdir(question_dir) if os.path.isdir(os.path.join(question_dir, d))]
    for contest in contest_dirs:

        task_dirs = [d for d in os.listdir(os.path.join(question_dir, contest)) if os.path.isdir(os.path.join(question_dir, contest, d))]

        for task in task_dirs:
            # find data.json in each task dir
            question_files = [f for f in os.listdir(os.path.join(question_dir, contest, task)) if f.endswith("data.json")][0]

            # check if data_{destination_lang}.json already exists
            if os.path.exists(os.path.join(question_dir, contest, task, f"data_{destination_lang}.json")):
                print(f"data_{destination_lang}.json already exists in {os.path.join(question_dir, contest, task)}. Skipping...")
                continue

            print(f"Translating {os.path.join(question_dir, contest, task, question_files)}...")
            with open(os.path.join(question_dir, contest, task, question_files), "r", encoding="utf-8") as f:
                question_data = json.load(f)

            new_question_data = dict(question_data)

            statement = str(question_data["new_statement"])
            io_styles = str(question_data["new_io_styles"])
            notes = str(question_data["new_notes"])


            # Translate statement
            messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, statement)
            response_message = _translate_statement(model, messages)
            new_question_data["new_statement"] = response_message


            # Translate io_styles
            messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, io_styles)
            response_message = _translate_statement(model, messages)
            new_question_data["new_io_styles"] = response_message

            # Translate notes
            messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, notes)
            response_message = _translate_statement(model, messages)
            new_question_data["new_notes"] = response_message

            # save new_question_data

            res_path = os.path.join(question_dir, contest, task, f"data_{destination_lang}.json")
            with open(res_path, "w", encoding="utf-8") as f:
                json.dump(new_question_data, f, ensure_ascii=False, indent=4)