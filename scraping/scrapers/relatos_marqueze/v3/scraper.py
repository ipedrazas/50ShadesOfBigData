# http://relatos.marqueze.net/feed/?format=rss2&paged=5
# http://codex.wordpress.org/WordPress_Feeds
import feedparser


feed = feedparser.parse('http://relatos.marqueze.net/feed/?format=rss2&paged=5')
print feed.entries[0].tags
# ['summary_detail', 'published_parsed', 'links', 'title', 'authors', 'slash_comments',
# 'comments', 'summary', 'content', 'guidislink', 'title_detail', 'link', 'author',
# 'published', 'author_detail', 'wfw_commentrss', 'id', 'tags']
