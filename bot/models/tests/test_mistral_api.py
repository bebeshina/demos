import io

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from transformers import AutoTokenizer

api_key = "API_TOKEN"
model = "mistral-tiny"

client = MistralClient(api_key=api_key)


def test_run(message):
    tokenizer = AutoTokenizer.from_pretrained("openaccess-ai-collective/tiny-mistral")

    # using jinja template to format the message in order to provide instructions on how the bot must conduct itself

    chat_template = io.open("mistral-instruct.jinja", "r", encoding="utf-8").read()
    chat_template = chat_template.replace('    ', '').replace('\n', '')
    tokenizer.chat_template = chat_template
    msg_dic = [{"role": "user", "content": "quelle sont les specificités de la boite robotisé ?"}]
    cont = tokenizer.apply_chat_template(msg_dic, tokenize=False, add_generation_prompt=True)
    print(cont)

    # providing the formatted content (containing instructions in addition to messages)

    messages = [
        ChatMessage(role="user", content=cont)
    ]
    chat_response = client.chat(
        model=model,
        messages=messages,
    )
    print(chat_response.choices[0].message.content)

    # @todo handle bot response length, prepare .js version



