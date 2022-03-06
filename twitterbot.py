import tweepy
from wordcloud_generate import generate_wordcloud_word
import random
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
    mentions = client.get_users_mentions(id=1178574797669883904, max_results=100)
    my_username = client.get_user(id=1178574797669883904).data.username
    replied_ids = open("replied_ids.txt", "r")
    replied_ids_list = [replied_id for replied_id in replied_ids]
    print(replied_ids_list)
    replied_ids.close()
    if len(mentions) == 0:
        return "No mentions for now"
    for mention in reversed(mentions[0]):
        text = mention.text
        tweet_id = mention.id
        if (f"{tweet_id}\n" not in replied_ids_list) and ("get word cloud " in text):
            try:
                requested_word = text.replace("get word cloud ", "")
                requested_word_split = requested_word.split()
                for word in requested_word_split:
                    if word.startswith("@"):
                        requested_word_split.remove(word)
                print(requested_word_split)
                if len(requested_word_split) == 1:
                    background_color = random.choice(["black", "white"])
                else:
                    background_color = requested_word_split[-1]
                requested_word = requested_word_split[0]
                generate_wordcloud_word(requested_word, tweet_id, background_color)
                client.create_tweet(
                    text=f"You can find the wordcloud here https://wordcloudbot9ja.herokuapp.com/{tweet_id}/{requested_word}",
                    in_reply_to_tweet_id=tweet_id,
                )
                client.like(tweet_id)
                print("liked")
                client.retweet(tweet_id)
                replied_ids = open("replied_ids.txt", "a")
                replied_ids.write(f"{tweet_id}\n")
                replied_ids.close()
            except:
                requested_word = requested_word.replace(" get word cloud ", "")
                requested_word_split = requested_word.split()
                pass

        else:
            print("replied or not a bot request")
