if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    __package__ = "Code_Understanding.experiment.llm"

from .openai_base_function import openai_base_chat_model

class ChatGPTChatFunction(openai_base_chat_model, base_url_=""):
    def __init__(self, model="", openai_key="", temperature = 0):
        super().__init__(model, openai_key)
        self.temperature = temperature

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

        message['content'] = message['content'].strip()
        
        return message, 0, total_tokens
    
    def parse(self):
        '''
        This function is used to parse the input into the satisfied format for the chat_completion_request function and run it. 
        '''
        conversation_history = self.conversation_history

        json_data = self.chat_completion_request(
            conversation_history
        )
        print(json_data)
        total_tokens = json_data['usage']['total_tokens']
        message = json_data["choices"][0]["message"]

        message['content'] = message['content'].strip()
        return message, 0, total_tokens