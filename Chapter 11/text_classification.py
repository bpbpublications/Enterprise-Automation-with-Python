from transformers import pipeline

model = pipeline("sentiment-analysis")
print(model("We love this product. It is amazing."))
