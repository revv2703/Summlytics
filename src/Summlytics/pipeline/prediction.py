from Summlytics.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_eval_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        summarizer = pipeline(task="summarization", model=self.config.model_path, tokenizer=tokenizer)
        gen_kwargs = {
            "max_length": 128,
            "num_beams": 8,
            "length_penalty": 0.7,
        }
        response = summarizer(text, **gen_kwargs)[0]['summary_text']

        print(f"Dialogue: {text}")
        print(f"Model summary: {response}")

        return response