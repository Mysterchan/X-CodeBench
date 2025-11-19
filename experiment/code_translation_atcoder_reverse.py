if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .llm.deepseek import DeepSeekChatFunction
from bert_score import score 

from .prompt_translation import (SYSTEM_PROMPT_EN_RU, SYSTEM_PROMPT_RU_EN, SYSTEM_PROMPT_EN_JP, SYSTEM_PROMPT_JP_EN, SYSTEM_PROMPT_EN_CN,
                                    USER_PROMPT_EN_RU, USER_PROMPT_RU_EN, USER_PROMPT_EN_JP, USER_PROMPT_JP_EN, USER_PROMPT_EN_CN)
    

import json
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv("API_CHAT")

def compute_bertscore(candidate, reference, lang="en"):
    """
    Compute BERTScore for a candidate and reference text.
    """
    P, R, F1 = score([candidate], [reference], lang=lang)
    return P.item(), R.item(), F1.item()

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
    platform = "atCoder"
    
    source_lang = "ru"
    destination_lang = "en"

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

    total = 0

    contest_dirs = [d for d in os.listdir(question_dir) if os.path.isdir(os.path.join(question_dir, d))]
    for contest in contest_dirs:

        task_dirs = [d for d in os.listdir(os.path.join(question_dir, contest)) if os.path.isdir(os.path.join(question_dir, contest, d))]

        for task in task_dirs:
            if total >= 1:
                break
            # find data.json in each task dir
            en_question_files = [f for f in os.listdir(os.path.join(question_dir, contest, task)) if f.endswith("data.json")][0]

            print(f"Translating {os.path.join(question_dir, contest, task, en_question_files)}...")
            with open(os.path.join(question_dir, contest, task, en_question_files), "r", encoding="utf-8") as f:
                en_question_data = json.load(f)

            en_statement = str(en_question_data["new_statement"])
            en_constraints = str(en_question_data["new_constraints"])
            en_io_styles = str(en_question_data["new_io_styles"])
            en_samples = list(en_question_data["sample_detail"])


            ru_question_files = [f for f in os.listdir(os.path.join(question_dir, contest, task)) if f.endswith(f"data_{source_lang}.json")]

            with open(os.path.join(question_dir, contest, task, ru_question_files[0]), "r", encoding="utf-8") as f:
                ru_question_data = json.load(f)

            ru_statement = str(ru_question_data["new_statement"])
            ru_constraints = str(ru_question_data["new_constraints"])
            ru_io_styles = str(ru_question_data["new_io_styles"])
            ru_samples = list(ru_question_data["sample_detail"])


            messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, ru_statement)
            translated_statement = _translate_statement(model, messages)
            
            # Compute BERTScore with en_statement
            P, R, F1 = compute_bertscore(translated_statement, en_statement, lang="en")
            print(f"BERTScore for statement - Precision: {P}, Recall: {R}, F1: {F1}")
            
            # Translate constraints
            messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, ru_constraints)
            translated_constraints = _translate_statement(model, messages)
            
            # Compute BERTScore with en_constraints
            P, R, F1 = compute_bertscore(translated_constraints, en_constraints, lang="en")
            print(f"BERTScore for constraints - Precision: {P}, Recall: {R}, F1: {F1}")
            
            # Translate io_styles
            messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, ru_io_styles)
            translated_io_styles = _translate_statement(model, messages)
            
            # Compute BERTScore with en_io_styles
            P, R, F1 = compute_bertscore(translated_io_styles, en_io_styles, lang="en")
            print(f"BERTScore for io_styles - Precision: {P}, Recall: {R}, F1: {F1}")
            
            # Translate samples
            new_samples = ru_samples
            for idx, sample in enumerate(new_samples):
                if len(sample["new_explanation_html"].strip()) == 0:
                    continue
                messages = _message_construct(USER_PROMPT, SYSTEM_PROMPT, sample["new_explanation_html"])
                translated_sample = _translate_statement(model, messages)
                
                # Compute BERTScore with en_samples[idx]["new_explanation_html"]
                P, R, F1 = compute_bertscore(translated_sample, en_samples[idx]["new_explanation_html"], lang="en")
                print(f"BERTScore for sample {idx} - Precision: {P}, Recall: {R}, F1: {F1}")


            total += 1