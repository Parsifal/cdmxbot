def process_tweet(status):
    print(u'{1} (https://twitter.com/{0}/status/{2}) - @{0}'.format(
        status.user.screen_name,
        status.text[:20] + '...' if len(status.text) > 10 else status.text,
        status.id_str
    ))
