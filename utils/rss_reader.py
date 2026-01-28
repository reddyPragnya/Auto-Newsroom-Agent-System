import feedparser

def fetch_rss_articles(feed_url):
    feed = feedparser.parse(feed_url)
    return [{"title": entry.title, "summary": entry.summary} for entry in feed.entries]