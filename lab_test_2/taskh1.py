import re

def extract_tags(text: str):
    # Regex ensures tags aren't part of another word
    mentions = [m.lower() for m in re.findall(r'(?<!\w)@([a-z0-9_]+)', text, flags=re.IGNORECASE)]
    hashtags = [h.lower() for h in re.findall(r'(?<!\w)#([a-z0-9_]+)', text, flags=re.IGNORECASE)]
    return mentions, hashtags


if __name__ == "__main__":
    text = input("Enter text: ")
    mentions, hashtags = extract_tags(text)
    print("mentions =", mentions)
    print("hashtags =", hashtags)
