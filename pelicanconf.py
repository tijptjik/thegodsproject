SITENAME = ''
SITENAME_SHORT = 'TGP'
SITETITLE = u'the god(s) project'
SITEURL = ''
TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors', 'liquid_tags.soundcloud']

# Facebook
FACEBOOK_APPID = '1792698777637826'

# NEST Template
THEME = 'nest'
SITESUBTITLE = u'the god(s) project'
# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Episodes','/episodes.html'), ('Contact','/contact.html'), ('About','/about.html')]
DISPLAY_PAGES_ON_MENU = False
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = 'tgpbanner2.png'
NEST_HEADER_LOGO = '/image/tgpthumbnail.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; the god(s) project 2016'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'home'
NEST_INDEX_HEADER_TITLE = u'the god(s) project'
NEST_INDEX_HEADER_SUBTITLE = False
NEST_INDEX_CONTENT_TITLE = u'Last Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'

# Static files
STATIC_PATHS = ['images', 'extra/ms-icon-144x144.png', 'extra/ms-icon-150x150.png', 'extra/ms-icon-310x310.png', 'extra/ms-icon-70x70.png', 'extra/android-icon-144x144.png', 'extra/android-icon-192x192.png', 'extra/android-icon-36x36.png', 'extra/android-icon-48x48.png', 'extra/android-icon-72x72.png', 'extra/android-icon-96x96.png', 'extra/apple-icon-114x114.png', 'extra/apple-icon-120x120.png', 'extra/apple-icon-144x144.png', 'extra/apple-icon-152x152.png', 'extra/apple-icon-180x180.png', 'extra/apple-icon-57x57.png', 'extra/apple-icon-60x60.png', 'extra/apple-icon-72x72.png', 'extra/apple-icon-76x76.png', 'extra/apple-icon-precomposed.png', 'extra/apple-icon.png', 'extra/browserconfig.xml', 'extra/CNAME', 'extra/favicon-16x16.png', 'extra/favicon-32x32.png', 'extra/favicon-96x96.png', 'extra/favicon.ico', 'extra/manifest.json']
EXTRA_PATH_METADATA = {
    'extra/ms-icon-144x144.png' : {'path' : 'ms-icon-144x144.png'},
    'extra/ms-icon-150x150.png' : {'path' : 'ms-icon-150x150.png'},
    'extra/ms-icon-310x310.png' : {'path' : 'ms-icon-310x310.png'},
    'extra/ms-icon-70x70.png' : {'path' : 'ms-icon-70x70.png'},
    'extra/android-icon-144x144.png' : {'path' : 'android-icon-144x144.png'},
    'extra/android-icon-192x192.png' : {'path' : 'android-icon-192x192.png'},
    'extra/android-icon-36x36.png' : {'path' : 'android-icon-36x36.png'},
    'extra/android-icon-48x48.png' : {'path' : 'android-icon-48x48.png'},
    'extra/android-icon-72x72.png' : {'path' : 'android-icon-72x72.png'},
    'extra/android-icon-96x96.png' : {'path' : 'android-icon-96x96.png'},
    'extra/apple-icon-114x114.png' : {'path' : 'apple-icon-114x114.png'},
    'extra/apple-icon-120x120.png' : {'path' : 'apple-icon-120x120.png'},
    'extra/apple-icon-144x144.png' : {'path' : 'apple-icon-144x144.png'},
    'extra/apple-icon-152x152.png' : {'path' : 'apple-icon-152x152.png'},
    'extra/apple-icon-180x180.png' : {'path' : 'apple-icon-180x180.png'},
    'extra/apple-icon-57x57.png' : {'path' : 'apple-icon-57x57.png'},
    'extra/apple-icon-60x60.png' : {'path' : 'apple-icon-60x60.png'},
    'extra/apple-icon-72x72.png' : {'path' : 'apple-icon-72x72.png'},
    'extra/apple-icon-76x76.png' : {'path' : 'apple-icon-76x76.png'},
    'extra/apple-icon-precomposed.png' : {'path' : 'apple-icon-precomposed.png'},
    'extra/apple-icon.png' : {'path' : 'apple-icon.png'},
    'extra/browserconfig.xml' : {'path' : 'browserconfig.xml'},
    'extra/CNAME' : {'path' : 'CNAME'},
    'extra/favicon-16x16.png' : {'path' : 'favicon-16x16.png'},
    'extra/favicon-32x32.png' : {'path' : 'favicon-32x32.png'},
    'extra/favicon-96x96.png' : {'path' : 'favicon-96x96.png'},
    'extra/favicon.ico' : {'path' : 'favicon.ico'},
    'extra/manifest.json' : {'path' : 'manifest.json'}
}

INDEX_SAVE_AS = 'blog.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Disable Tags
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

SOCIAL = [('Facebook','https://www.facebook.com/thegodsproject/'),('RTHK','http://programme.rthk.hk/channel/radio/programme.php?p=7395')]