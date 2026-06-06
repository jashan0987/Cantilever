import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return " ".join(words)


# ✅ TEST PART (add this at bottom)
if __name__ == "__main__":
    text = "This Movie was AMAZING!!!"
    print(clean_text(text))