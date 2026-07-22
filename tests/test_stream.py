from app.ai.clients.ollama_client import OllamaClient

client = OllamaClient()

messages = [
    {
        "role": "user",
        "content": "Say hello in one sentence."
    }
]

print("\nStreaming Response:\n")

for chunk in client.stream_chat(messages):
    print(chunk, end="", flush=True)

print("\n\nFinished.")