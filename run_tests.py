import nose
from webium.plugins.browser_closer import BrowserCloserPlugin


if __name__ == '__main__':
    nose.run_exit(argv=['nosetests', '-v', '--exe',
                        'tests',
                        '--with-xunit',
                        '--xunit-file=webium_xunit_output.xml',
                        '--whenclose=after_all',
                        ], addplugins=[BrowserCloserPlugin()],)
