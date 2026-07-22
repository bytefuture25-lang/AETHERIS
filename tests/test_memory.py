from app.memory.extractor import MemoryExtractor

extractor = MemoryExtractor()

tests = [
    "My name is Harsh",
    "I'm building ÆTHERIS",
    "My favorite language is Python",
    "I use VS Code",
    "Today is very hot",
]

for text in tests:
    print("=" * 60)
    print(text)

    memories = extractor.extract(text)

    if not memories:
        print("No memory detected.")
        continue

    for memory in memories:
        print(memory)