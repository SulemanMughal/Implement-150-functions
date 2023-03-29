def clean_hashtags():
    with open('hashtags.txt', 'r') as file:
        content = file.read()
    hashtags = content.split()
    short_hashtags = [
        hashtag for hashtag in hashtags if len(hashtag) <= 5
    ]
    result = sorted(set(short_hashtags))
    return result
    
    
print(clean_hashtags())