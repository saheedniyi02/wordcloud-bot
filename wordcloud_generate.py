import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# get a pickled dataframe
data = pd.read_pickle("util_files/posts.pkl")


def generate_statement_with_word(word):
    word = word.lower()
    new_column = []
    for statement in data:
        if word in statement:
            statement = statement.replace(word, "")
            new_column.append(statement)
    return new_column


def generate_wordcloud_word(word, tweet_id, background_color):
    background_color_colormap = {"white": "spring", "black": "hsv"}
    statements_with_word = generate_statement_with_word(word)
    print(f"There are {len(statements_with_word)} statements with {word} in the data")
    text = " ".join(txt for txt in statements_with_word)
    print(
        "There are {} words in the combination of all texts.".format(
            len(text.split(" "))
        )
    )
    stopwords = set(STOPWORDS)
    stopwords.update(["https"])
    wordcloud = WordCloud(
        stopwords=stopwords,
        max_font_size=100,
        random_state=42,
        width=1600,
        height=800,
        min_font_size=2,
        max_words=4000,
        relative_scaling=0.1,
        colormap=background_color_colormap[background_color],
        background_color=background_color,
    ).generate(text)
    wordcloud_img = wordcloud.to_image()
    wordcloud_img.save(f"static/{tweet_id}.jpg")
