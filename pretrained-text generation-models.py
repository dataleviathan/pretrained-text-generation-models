pip install transformers torch

from transformers import pipeline

# Load GPT-2 text generation model
generator = pipeline('text-generation', model='gpt2')

# Set your prompt
prompt = 'In the future, education will'

# Generate text
result = generator(prompt, max_length=50, temperature=0.7)
print(result[0]['generated_text'])

# Experiment with different prompts
prompt = 'The impact of AI on the future of work'
result = generator(prompt, max_length=50, temperature=0.8)
print(result[0]['generated_text'])

prompt = 'Once upon a time, there was a kingdom'
result = generator(prompt, max_length=100, temperature=0.6)
print(result[0]['generated_text'])

prompt = 'In the future, education will'
result = generator(prompt, max_length=50, temperature=0.7)
print(result[0]['generated_text'])

prompt = 'The impact of AI on the future of work'
result = generator(prompt, max_length=50, temperature=0.8)
print(result[0]['generated_text'])

prompt = 'Once upon a time, there was a kingdom'
result = generator(prompt, max_length=100, temperature=0.6)
print(result[0]['generated_text'])
