import openai
import dotenv
import os

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAIAdapter:
    def __init__(self):
        self.system_prompt = "あなたは端的に発言するAIです。"

        pass

    def _create_message(self, role, message):
        return {
            "role": role,
            "content": message
        }

    def _create_chat(self, question):
        system_message = self._create_message("system", self.system_prompt)
        user_message = self._create_message("user", question)

        messages = [
            system_message,
            user_message
        ]

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return res["choices"][0]["messasge"]["content"]


if __name__ == "__main__":
    adapter = OpenAIAdapter()
    print(adapter._create_chat("こんにちは"))
