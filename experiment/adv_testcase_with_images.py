if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .llm.deepseek import DeepSeekChatFunction

from .prompt_tasks import SYSTEM_PROMPT_ADVERSARIAL_TEST_GENERATION_FEW_SHOT

import json
import dotenv
dotenv.load_dotenv()

API_KEY = os.getenv("API_CHAT")

import os
import re
import base64

def _encode_image_base64(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def _extract_md_images(text: str):
    # Captures paths in ![alt](path)
    return re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text or "")

def _strip_md_images(text: str) -> str:
    return re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text or '').strip()

def _build_user_content_with_images(text: str, question_dir: str):
    """
    Convert a text (which may include markdown image tags) into OpenAI multimodal content,
    preserving the original order: text, image, text, image, ...
    It resolves images from:
      - {question_dir}/images/{filename}
      - {question_dir}/{filename}
      - or uses the URL directly if it's http(s).
    """
    if not text:
        return text

    pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    matches = list(pattern.finditer(text))
    if not matches:
        return text  # fallback to plain text

    content = []
    last = 0

    for m in matches:
        # preceding text
        pre = text[last:m.start()]
        if pre:
            content.append({"type": "text", "text": pre})

        alt = m.group(1)
        ref = m.group(2).strip()

        # If ref is a URL, use directly
        if ref.startswith("http://") or ref.startswith("https://"):
            content.append({"type": "image_url", "image_url": {"url": ref}})
        else:
            name = os.path.basename(ref)
            # Try {question_dir}/images/{name} first, then {question_dir}/{name}
            path1 = os.path.join(question_dir, "images", name)
            path2 = os.path.join(question_dir, name)
            img_path = path1 if os.path.exists(path1) else (path2 if os.path.exists(path2) else None)

            if img_path:
                ext = os.path.splitext(img_path)[1].lower()
                mime = (
                    "image/png" if ext == ".png"
                    else "image/jpeg" if ext in (".jpg", ".jpeg")
                    else "image/webp" if ext == ".webp"
                    else "application/octet-stream"
                )
                b64 = _encode_image_base64(img_path)
                content.append({"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}})
            else:
                # Fallback: keep the original markdown tag as text if the file isn't found
                content.append({"type": "text", "text": m.group(0)})

        last = m.end()

    # trailing text
    tail = text[last:]
    if tail:
        content.append({"type": "text", "text": tail})

    return content

def _message_construct(question_data, code, question_dir):
    system_message = SYSTEM_PROMPT_ADVERSARIAL_TEST_GENERATION_FEW_SHOT.replace("{problem_statement}", question_data["Problem Statement"])
    system_message = system_message.replace("{constraints}", question_data["Constraints"])
    system_message = system_message.replace("{io_styles}", question_data["IO Styles"])

    system_message = system_message.replace("{buggy_code}", code)

    system_message = _build_user_content_with_images(system_message, question_dir)

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
    model_names = ["gpt-4o-mini","gpt-4.1-mini"]
    dataset = "question_with_images"
    tasks = "questions"
    res_name = "adv_tescase"
    platforms = ["atCoder", "codeforces"]
    languages = ["py", "cpp", "java"]


    for model_name in model_names:

        model = ChatGPTChatFunction(model=model_name, openai_key= API_KEY, temperature=0)

        for platform in platforms:
            for language in languages:
                    extension = "Wrong_solution"
                    question_dir = os.path.join("data", "programming_contest", platform, dataset, tasks)
                    result_dir = os.path.join("results", model_name, platform, dataset, res_name, language)

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
                                if os.path.exists(os.path.join(result_dir, fd, sub_fd, "input.txt")):
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
                                
                                messages = _message_construct(question_data, unoptimized_code, os.path.join(question_dir, fd, sub_fd))
                                model.conversation_history = messages
                                print(messages)

                                response_message, _, total_tokens = model.parse()

                                code = _message_code_parse(response_message["content"])
                                question_name = qf.replace(".json", "")
                                if not os.path.exists(os.path.join(result_dir, fd, sub_fd)):
                                    os.makedirs(os.path.join(result_dir, fd, sub_fd))

                                with open(os.path.join(result_dir, fd, sub_fd, "input.txt"), "w", encoding="utf-8") as f:
                                    f.write(code)
