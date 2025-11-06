from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

result = classifier("I've been waiting for a Hugging Face course my whole life.")
print(result)

