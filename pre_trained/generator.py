from transformers import pipeline, set_seed
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
# from transformers import GPT2Tokenizer, TFGPT2Model


def gpt2(prompt):
    model = pipeline('text-generation', model='gpt2')
    set_seed(42)
    
    responses = model(prompt, max_length=30, num_return_sequences=5)
    return list(map(lambda x: x['generated_text'], responses))


def blenderbot(prompt):
    tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
    model = TFAutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
    responses = model.generate(**tokenizer(prompt, return_tensors="tf", truncation=True, max_length=30))
    print(responses)
    return tokenizer.batch_decode(responses, skip_special_tokens=True)