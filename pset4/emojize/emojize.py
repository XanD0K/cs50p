import emoji


text = input("Input: ").strip()

print("Output:", emoji.emojize(text, language="alias"))