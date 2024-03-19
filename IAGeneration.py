import ollama

def Creator():
  response = ollama.chat(model='MistralCreator', messages=[
    {
      'role': 'assistant',
      'content': 'Why is the sky blue?',
    },
  ])

  print(response['message']['content'])
  return response['message']['content']

def Detector(text):
  responseCreator = ollama.chat(model='MistralDetector', messages=[
    {
      'role': 'assistant',
      'content': text,
    },
  ])

  print(responseCreator['message']['content'])
  if responseCreator['message']['content'] == "YES":
    return "AI"
  else:
    return "HUMAN"
