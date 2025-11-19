if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    __package__ = "Code_Understanding.experiment.llm"

import json
import abc
import time
from termcolor import colored
from anthropic import Anthropic, AsyncAnthropic


class anthropic_base_chat_model:
    def __init__(self, model="", openai_key="") -> None:
        '''
        This class is the base class for all chat endpoints supporting openai sdk.  (gpt/ deepseek/ etc.)
        model: name of the model
        openai_key: openai api key

        conversation_history: list of messages (a tuple, role: str, content: str) in the conversation
        '''
        super().__init__()
        self.model = model
        print("==========")
        print(self.model)
        print("==========")
        self.conversation_history = []
        self.openai_key = openai_key
        self.TRY_TIME = 6
        self.client = Anthropic(api_key=openai_key)  # Initialize OpenAI client here
        self.Ayncclient = AsyncAnthropic(api_key=openai_key)  # Initialize AsyncOpenAI client here

    def add_message(self, message):
        self.conversation_history.append(message)

    def change_messages(self, messages):
        self.conversation_history = messages

    def display_conversation(self, detailed=False):
        role_to_color = {
            "system": "red",
            "user": "green",
            "assistant": "blue",
        }
        for message in self.conversation_history:
            print_obj = f"{message['role']}: {message['content']} "
            print(
                colored(
                    print_obj,
                    role_to_color[message["role"]],
                )
            )

    def chat_completion_request(self, messages):
        use_messages = []
        for message in messages:
            if not("valid" in message.keys() and message["valid"] == False):
                use_messages.append(message)

        system_message = use_messages[0]["content"]
        use_messages = use_messages[1:]

        json_data = {
            "model": self.model,
            "messages": use_messages,
            "max_tokens": 1024,
            "system": system_message,
        }
        try:
            response = self.client.messages.create(
                **json_data
            )
            json_data = response.model_dump_json()
            return json.loads(json_data)
        
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"OpenAI calling Exception: {e}")
            return self.chat_completion_request(messages)

    async def achat_completion_request(self, messages):
        use_messages = []
        for message in messages:
            if not("valid" in message.keys() and message["valid"] == False):
                use_messages.append(message)

        system_message = use_messages[0]["content"]
        use_messages = use_messages[1:]

        json_data = {
            "model": self.model,
            "messages": use_messages,
            "max_tokens": 1024,
            "system": system_message,
        }
        try:
            response = await self.Ayncclient.messages.create(
                **json_data
            )
            json_data = response.model_dump_json()
            return json.loads(json_data)
        
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"OpenAI calling Exception: {e}")
            return await self.achat_completion_request(messages)
        
    def parse(self):
        '''
        This function is used to parse the input into the satisfied format for the chat_completion_request function and run it. 
        '''
        conversation_history = self.conversation_history

        json_data = self.chat_completion_request(
            conversation_history
        )
        total_tokens = json_data['usage']['total_tokens']
        message = json_data["choices"][0]["message"]

        message['content'] = message['content'].strip()

        return message, 0, total_tokens

    async def aparse(self):
        '''
        This function is used to parse the input into the satisfied format for the chat_completion_request function and run it. 
        '''
        conversation_history = self.conversation_history

        json_data = await self.achat_completion_request(
            conversation_history
        )
        total_tokens = json_data['usage']['input_tokens'] + json_data['usage']['output_tokens']
        message = json_data["content"][0]["text"]
        message = {"content": message}
        message['content'] = message['content'].strip()
        return message, 0, total_tokens