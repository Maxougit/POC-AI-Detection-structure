import ollama

def Creator():
  response = ollama.chat(model='MistralCreator', messages=[
    {
      'role': 'assistant',
      'content': 'Tell me a story',
    },
  ])

  # print(response['message']['content'])
  return response['message']['content']

def Detector(text):
  responseCreator = ollama.chat(model='MistralDetector', messages=[
    {
      'role': 'assistant',
      'content': text,
    },
  ])

  # print(responseCreator['message']['content'])
  if responseCreator['message']['content'].find("YES") != -1:
    return "AI"
  elif responseCreator['message']['content'].find("NO") != -1:
    return "HUMAN"
  else:
    return "UNKNOWN"
