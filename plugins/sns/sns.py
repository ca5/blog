from pelican import signals, contents
from datetime import datetime
from pytz import timezone
import twitter
import sys



class SnsGenerator(object):

    def __init__(self, context, settings, path, theme, output_path, *null):

        self.output_path = output_path
        self.context = context
        self.now = datetime.now()
        self.siteurl = settings.get('SITEURL')

        self.default_timezone = settings.get('TIMEZONE', 'UTC')
        self.timezone = getattr(self, 'timezone', self.default_timezone)
        self.timezone = timezone(self.timezone)

        self.format = 'xml'

        self.changefreqs = {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
        }

        self.priorities = {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        }

        config = settings.get('SITEMAP', {})
        self.twitter_consumer_key = settings.get('TWITTER_CONSUMER_KEY')
        self.twitter_consumer_secret = settings.get('TWITTER_CONSUMER_SECRET')
        self.twitter_token_key = settings.get('TWITTER_TOKEN_KEY')
        self.twitter_token_secret = settings.get('TWITTER_TOKEN_SECRET')

    def generate_output(self, writer):
        # search latest_article
        articles = self.context['articles']
        if articles is not None:
            latest_article = None;
            for article in articles:
                if latest_article is None \
                    or article.date > latest_article.date:
                    latest_article = article
            latest_article_url = '' if latest_article.url == 'index.html' else latest_article.url
            tweet = '[Blog update] %s %s' % (latest_article.title, self.siteurl + '/' + latest_article_url)

            print '---last update notification--------'
            print tweet
            print '-----------------------------------'

            print 'are you sure to tweet?[Y/n]'
            input_line = sys.stdin.readline().rstrip()
            if input_line.lower() in ['y', 'yes']:
                api = twitter.Api(consumer_key=self.twitter_consumer_key,
                          consumer_secret=self.twitter_consumer_secret,
                          access_token_key=self.twitter_token_key,
                          access_token_secret=self.twitter_token_secret)
                api.PostUpdate(tweet)
            else:
                print 'skip tweeting'


def get_generator(generators):
    return SnsGenerator

def register():
    signals.get_generators.connect(get_generator)
