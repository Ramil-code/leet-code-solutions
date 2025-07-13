cache={}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        url_new=get_new-info(url)
        cache[url]=new_url
        return new_url