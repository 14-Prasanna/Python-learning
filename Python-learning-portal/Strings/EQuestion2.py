def frfind(text, word):

    index = text.lower().rfind(word.lower())

    if index != -1:
        print(f"Last occurrence of {word} starts at index {index}")
    else:
        print(f"{word} not found")


str1 = """Emma isa data scientistwho knowsPython. Emmaworks atgoogle."""

frfind(str1, "Emma")