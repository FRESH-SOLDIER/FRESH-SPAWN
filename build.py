# Rebuilds index.html from src/template.html + src/data.json.
# Wraps the page in a full HTML document (doctype, charset, viewport, SEO tags).
import json, re
SITE = {'title': 'Fresh Spawn', 'url': 'https://fresh-soldier.github.io/FRESH-SPAWN/', 'desc': 'Discover new and upcoming games you have not seen yet. Browse new releases and hidden gems by genre, and find games similar to the ones you love.', 'embed': False, 'ld_name': 'Fresh Spawn', 'lede': 'Discover new and upcoming games: new releases, announced games, hidden gems by genre, and a similar-game finder. Data and images from RAWG.'}
t = open('src/template.html').read()
d = open('src/data.json').read()
if SITE['embed']:
    d = '{"embed":true,' + d[1:]   # live site plays Deezer previews in the page
i = t.index('</style>') + len('</style>')
head, body = t[:i], t[i:]
ld = json.dumps({"@context": "https://schema.org", "@type": "WebSite", "name": SITE['ld_name'], "url": SITE['url'], "description": SITE['desc'], "inLanguage": "en"})
esc = lambda s: s.replace('&', '&amp;').replace('"', '&quot;')
seo = ('<meta name="description" content="%s">' % esc(SITE['desc'])
  + '<link rel="canonical" href="%s">' % SITE['url']
  + '<meta property="og:type" content="website"><meta property="og:site_name" content="%s">' % esc(SITE['title'])
  + '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s">' % (esc(SITE['title']), esc(SITE['desc']), SITE['url'])
  + '<meta property="og:image" content="%s">' % (SITE['url'] + 'og.png') + '<meta name="twitter:image" content="%s">' % (SITE['url'] + 'og.png') + '<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#14182B">'
  + '<script type="application/ld+json">%s</script>' % ld)
reset = '<style>:root{color-scheme:light}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
# the template's own <title> and <meta> lines stay inside head
html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
  '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
  + seo + reset + head + '</head><body>'
  + body.replace('/*DATA*/', d) + '<noscript><p style="max-width:60ch;margin:24px auto;padding:0 16px">%s</p></noscript></body></html>' % esc(SITE['lede']))
open('index.html', 'w').write(html)
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>%s</loc></url></urlset>' % SITE['url'])
open('robots.txt', 'w').write('User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n' % SITE['url'])
print('built index.html', len(html), 'bytes')
