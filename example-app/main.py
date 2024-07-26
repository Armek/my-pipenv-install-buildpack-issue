from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

translator = pipeline("translation_en_to_fr", model=model, tokenizer=tokenizer, device='cuda')

text = "This is a test"

result = translator(text)

print(result)
