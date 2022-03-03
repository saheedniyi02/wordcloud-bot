import tweepy
from wordcloud_generate import generate_wordcloud_word
from credentials import (
    access_token,
    bearer_token,
    API_KEY,
    API_SECRET_KEY,
    access_token_secret,
)

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

replied_ids = open("util_files/replied_ids.txt", "r")
replied_ids_list = [replied_id for replied_id in replied_ids]


def reply_tweets():
    mentions = client.get_users_mentions(id=1178574797669883904, max_results=5)
    my_username = client.get_user(id=1178574797669883904).data.username
    replied_ids = open("replied_ids.txt", "r")
    replied_ids_list = [replied_id for replied_id in replied_ids]
    replied_ids.close()
    if len(mentions) == 0:
        return "No mentions for now"
        print(mentions[0])
    for mention in reversed(mentions[0]):
        text = mention.text
        tweet_id = mention.id
        print(text)

        if (f"{tweet_id}\n" not in replied_ids_list) and ("get word cloud " in text):
            try:
                requested_word = text.replace("@" + my_username, "")
                requested_word = requested_word.replace("get word cloud ", "")
                requested_word = requested_word.replace(" ", "")
                generate_wordcloud_word(requested_word)
                client.create_tweet(
                    text="You can find the wordcloud <a href=" "> Link </a>",
                    in_reply_to_tweet_id=tweet_id,
                )
                replied_ids = open("replied_ids.txt", "a")
                replied_ids.write(f"{tweet_id}\n")
                print(replied_ids)
                replied_ids.close()
            except:
                return
