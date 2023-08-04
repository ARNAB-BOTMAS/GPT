import openai

def open_ai(query):
    API_KEY = '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'
    prompt = query
    openai.api_key = API_KEY
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=500, temperature=0.7)
    ans = response['choices'][0]['text']
    return ans

# print(open_ai("hi"))
