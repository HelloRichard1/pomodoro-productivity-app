from transformers import pipeline
import torch

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

device = "cuda" if torch.cuda.is_available() else "cpu"

generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto" if device == "cuda" else None,
    trust_remote_code=True,
)


def ask_llm(prompt: str):

    response = generator(
        prompt,
        max_new_tokens=300,
        temperature=0.3,
        do_sample=True,
    )

    return response[0]["generated_text"]
