import os
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_wordcloud(
    directory,
    file_filter=lambda root, dirs, files: True,
    encoding="utf-8",
    wordlist_filter=lambda word: True,
    wordcloud_params={},
):
    text = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file_filter(root, dirs, files):
                continue
            with open(os.path.join(root, file), "r", encoding=encoding) as f:
                text += f.read()

    wordlist = jieba.cut(text, cut_all=True)
    wordlist = filter(wordlist_filter, wordlist)
    wl = " ".join(wordlist)

    default_params = {
        "font_path": "simhei.ttf",
        "background_color": "white",
        "max_words": 2000,
        "width": 1000,
        "height": 860,
        "margin": 2,
    }
    if wordcloud_params is not None:
        default_params.update(wordcloud_params)
    return WordCloud(**default_params).generate(wl)


if __name__ == "__main__":
    wc = generate_wordcloud(".", wordlist_filter=lambda word: len(word) > 1)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
