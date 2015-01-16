from nose.plugins import Plugin
from webium.driver import close_driver


class WHEN_CLOSE(object):
    AFTER_TEST = 'after_test'
    AFTER_ALL = 'after_all'


class BrowserCloserPlugin(Plugin):
    enabled = True
    name = 'browser_closer'

    def options(self, parser, env):
        parser.add_option("--whenclose", action="store",
                          default='after_test',
                          dest="browser_closer_when",
                          metavar="STR",)

    def configure(self, options, conf):
        """Configure plugin. Plugin is enabled by default.
        """
        self.conf = conf
        self.when = options.browser_closer_when

    def afterTest(self, test):
        if self.when == WHEN_CLOSE.AFTER_TEST:
            close_driver()

    def finalize(self, result):
        if self.when == WHEN_CLOSE.AFTER_ALL:
            close_driver()