import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system",
#          "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )
# print(completion.choices[0].message)

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                               messages=[{"role": "user", "content": "Hello world"}])
print(chat_completion)
