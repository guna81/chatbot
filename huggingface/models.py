from transformers import pipeline, set_seed
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
# from transformers import GPT2Tokenizer, TFGPT2Model


gpt_model = pipeline('text-generation', model='gpt2')

def gpt2(prompt):
    set_seed(42)
    
    responses = gpt_model(prompt, max_length=30, num_return_sequences=5)
    return list(map(lambda x: x['generated_text'], responses))


tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
blenderbot_model = TFAutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

def blenderbot(prompt):
    responses = blenderbot_model.generate(**tokenizer(prompt, return_tensors="tf", truncation=True, max_length=30))
    print(responses)
    return tokenizer.batch_decode(responses, skip_special_tokens=True)