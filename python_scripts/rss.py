import feedparser
rss_url = 'https://www.heise.de/rss/heise.rdf'
feed = feedparser.parse(rss_url).entries
for l in range(len(feed)):
    print({
        "title": feed[l].title,
        "content": feed[l].summary
    })
