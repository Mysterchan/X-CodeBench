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

# ...existing code...
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

def _message_construct(system_prompt, question_data, question_dir):
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

    # Build multimodal content if markdown images are present
    user_content = _build_user_content_with_images(system_message, question_dir)

    messages = [
        {
            "role": "user",
            "content": user_content,
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
