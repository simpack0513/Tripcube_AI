import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.FineTuningJob.list()


# api key = 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

# 파인튜닝 방법
# openai --api-key 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 api fine_tuning.job.create -t data_prepared_train.jsonl -m davinci-002
