def get_channel_name(url):
    if url.startswith("https://t.me/"):
        return "@" + url[len("https://t.me/"):]
    else:
        return None
