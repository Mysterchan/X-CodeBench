if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    __package__ = "Code_Understanding.experiment"

from .llm.chatfunction import ChatGPTChatFunction
from .llm.deepseek import DeepSeekChatFunction

SYSTEM_PROMPT_PROGRAM_REPAIR = """
You are a professional data visualization programmer tasked with debugging and repairing Python code for matplotlib or seaborn. 
You will be provided with a natural-language description of the intended plot, the buggy code, the actual (incorrect) rendered image, and the expected (correct) image. 
Your goal is to produce a corrected Python script that generates the desired visualization.
You will NOT return anything except for the corrected program.

Requirements:
1. Carefully analyze the provided description, buggy code, and images to identify the issue.
2. Modify the code to fix the bug while preserving the intended functionality and adhering to best practices.
3. Ensure the corrected code produces the expected visualization as described.

You are given the following Questions:
{question}

Corrected Code:
"""

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
    problem_statement = question_data.get("Description", "")
    input_payload = question_data.get("Input Payload", "")

    input_payload = input_payload.replace("{{}}", code)

    final_input = f"{problem_statement}\n{input_payload}"

    print("Final Input:", final_input)

    system_message = SYSTEM_PROMPT_PROGRAM_REPAIR.replace("{question}", final_input)
    system_message = _build_user_content_with_images(system_message, question_dir)

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
    
    if "```" in response_content:
        code_start = response_content.find("```")
        code_start += len("```")
        code_end = response_content.find("```", code_start)
        if code_end == -1:
            code = response_content[code_start:].strip()
        else:
            code = response_content[code_start:code_end].strip()

        return code

    return response_content.strip()

if __name__ == "__main__":
    model_names = ["gpt-4.1-mini"]
    res_name = "code_debug"
    platform = "data"
    language = "py"

    for model_name in model_names:
        model = ChatGPTChatFunction(model=model_name, openai_key= API_KEY, temperature=0)

        question_dir = os.path.join("data", "datascience", platform)
        result_dir = os.path.join("results", model_name, "code_debug")

        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        for fd in os.listdir(question_dir):
            fd_path =  os.path.join(question_dir, fd)
            if not os.path.isdir(fd_path):
                continue

            print(f"Processing {fd}...")

            question_json_path = os.path.join(question_dir, fd, "data.json")
            buggy_code_path = os.path.join(question_dir, fd, "Buggy_code.py")

            with open(question_json_path, "r", encoding="utf-8") as f:
                question_data = json.load(f)
            
            with open(buggy_code_path, "r", encoding="utf-8") as f:
                buggy_code = f.read()

            messages = _message_construct(question_data, buggy_code, os.path.join(question_dir, fd))

            model.conversation_history = messages

            response_message, _, total_tokens = model.parse()
            code = _message_code_parse(response_message["content"])
            if not os.path.exists(os.path.join(result_dir, fd)):
                os.makedirs(os.path.join(result_dir, fd))


            with open(os.path.join(result_dir, fd, "code.py"), "w", encoding="utf-8") as f:
                f.write(code)