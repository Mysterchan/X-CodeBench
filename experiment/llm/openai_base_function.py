from openai import OpenAI
from openai import AsyncOpenAI
import json
import abc
import time
from termcolor import colored

class openai_base_chat_model:
    base_url_ = ""  # Placeholder for subclass-specific base_url_

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
        self.base_url = type(self).base_url_
        self.TRY_TIME = 6
        self.client = OpenAI(api_key=openai_key, base_url=self.base_url)  # Initialize OpenAI client here
        self.Ayncclient = AsyncOpenAI(api_key=openai_key, base_url=self.base_url)  # Initialize AsyncOpenAI client here

    def __init_subclass__(cls, base_url_, **kwargs):
        '''
        This method is called when a new subclass is created. It enforces that each subclass
        specifies its own base_url_.
        '''
        super().__init_subclass__(**kwargs)
        if not base_url_:
            raise ValueError(f"Subclass {cls.__name__} must define a non-empty base_url_.")
        cls.base_url_ = base_url_  # Assign the base_url_ to the subclass

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

        json_data = {
            "model": self.model,
            "messages": use_messages,
            "max_tokens": 8192,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'temperature': self.temperature,
        }
        try:
            response = self.client.chat.completions.create(
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

        json_data = {
            "model": self.model,
            "messages": use_messages,
            "max_tokens": 8192,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'temperature': self.temperature,
        }
        try:
            response = await self.Ayncclient.chat.completions.create(
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

        return message, 0, total_tokens

    async def aparse(self):
        '''
        This function is used to parse the input into the satisfied format for the chat_completion_request function and run it. 
        '''
        conversation_history = self.conversation_history

        json_data = await self.achat_completion_request(
            conversation_history
        )
        total_tokens = json_data['usage']['total_tokens']
        message = json_data["choices"][0]["message"]

        return message, 0, total_tokens