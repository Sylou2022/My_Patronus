# # -*- coding: utf-8 -*-

# import openai

# openai.api_key = ""

# prompt = "Quel est le sens de la vie ?"
# response = openai.Completion.create(
#  engine="text-davinci-002",
#  prompt=prompt,
#  temperature=0.5,
#  max_tokens=50,
#  n=1,
#  stop=None,
#  timeout=20,
# )

# print(response.choices[0].text)

import openai
openai.api_key = ""  # supply your API key however you choose

image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")

