import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, how are you?"}]
)

print(response["choices"][0]["message"]["content"])
