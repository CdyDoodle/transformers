from src.transformers import (
    AutoModelForSequenceClassification,
)

model = AutoModelForSequenceClassification.from_pretrained(
    "google-bert/bert-base-cased", num_labels=2
)
