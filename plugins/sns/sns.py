import sys
from HTMLParser import HTMLParser
import twitter
import facebook
from pelican import signals, contents
from pelican.utils import truncate_html_words

# html tag stripper
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

class SnsGenerator(object):

    def __init__(self, context, settings, path, theme, output_path, *null):

        self.output_path = output_path
        self.context = context
        self.siteurl = settings.get('SITEURL')
        self.sitelogo= settings.get('SITE_LOGO')
        self.summary_max_length= settings.get('SUMMARY_MAX_LENGTH')

        config = settings.get('SITEMAP', {})
        self.twitter_consumer_key = settings.get('TWITTER_CONSUMER_KEY')
        self.twitter_consumer_secret = settings.get('TWITTER_CONSUMER_SECRET')
        self.twitter_token_key = settings.get('TWITTER_TOKEN_KEY')
        self.twitter_token_secret = settings.get('TWITTER_TOKEN_SECRET')
        self.facebook_token = settings.get('FACEBOOK_TOKEN')

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
            #  
            # print 'are you sure to share?[Y/n]'
            # input_line = sys.stdin.readline().rstrip()
            # if input_line.lower() in ['y', 'yes']:
            #     graph = facebook.GraphAPI(access_token=self.facebook_token)
            #     attachment =  {
            #             'name': self.context['SITENAME'].encode('utf-8'),
            #             'link': (self.siteurl + '/' + latest_article_url).encode('utf-8'),
            #             'caption': latest_article.title.encode('utf-8'),
            #             'description': strip_tags(latest_article.content).encode('utf-8'),
            #             'picture': (self.siteurl + '/' + self.sitelogo).encode('utf-8')
            #         }
            #     graph.put_wall_post(message=tweet.encode('utf-8'), attachment=attachment)
            # else:
            #     print 'skip sharing'


def get_generator(generators):
    return SnsGenerator

def register():
    signals.get_generators.connect(get_generator)
