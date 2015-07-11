from pelican import signals, contents
from datetime import datetime
from pytz import timezone



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
            print tweet


def get_generator(generators):
    return SnsGenerator

def register():
    signals.get_generators.connect(get_generator)
