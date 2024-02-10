from Summlytics.entity import TrainModelConfig
from Summlytics.logging import logger
from transformers import TrainingArguments, Trainer, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
import os


class TrainModel:
    def __init__(self, config: TrainModelConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        seq2seq_data_collator=DataCollatorForSeq2Seq(tokenizer, model=model)

        dataset = load_from_disk(self.config.data_path)

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            # eval_steps=self.config.eval_steps,
            eval_steps=500,
            save_steps=int(float(self.config.save_steps)),  # workaround here
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=dataset['test'],
            eval_dataset=dataset['validation'],
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator
        )

        logger.info("Starting model training")

        trainer.train()
        model.save_pretrained(os.path.join(self.config.root_dir, 'pegasus-samsum-model'))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, 'pegasus-samsum-tokenizer'))

        logger.info("Model training completed")