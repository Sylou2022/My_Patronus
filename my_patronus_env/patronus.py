
# -*- coding: utf-8 -*-

import openai
from PIL import Image

openai.api_key = ""

prompt = "Quel est le sens de la vie ?"
response = openai.Completion.create(
 engine="text-davinci-002",
 prompt=prompt,
 temperature=0.5,
 max_tokens=50,
 n=1,
 stop=None,
 timeout=20,
)

print(response.choices[0].text)

# sys.stdout.buffer.write(reponse.choice[0].text.encode)
