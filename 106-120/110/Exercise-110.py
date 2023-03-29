def clean_hashtags(input_file, output_file, length):
    # Read hashtags
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Process hashtags
    hashtags = content.split()
    short_hashtags = [
        hashtag for hashtag in hashtags if len(hashtag) <= length + 1
    ]
    unique_short_hashtags = sorted(set(short_hashtags))
    
    # Write hashtags to the file
    with open(output_file, 'w') as file:
        for hashtag in unique_short_hashtags:
            file.write(hashtag + '\n')