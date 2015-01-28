# -*- coding: utf8 -*-
import os
import re
import codecs
import shutil
from markdown import Markdown
from jinja2 import Template

site_template = Template(u'''
<!doctype html>
<html>
<head>
<title>{{site_title}}: {{page_title}}</title>
<link rel="stylesheet" type="text/css" title="Xposés" href="http://www-igm.'''
                         '''univ-mlv.fr/~dr/XPOSE/style.css"/>
<meta charset='utf-8' />
</head>
<body>
<div id="content">
<h1>{{site_title}}</h1>
{{content}}
</div>
<div id="navigation">
{% for page in navigation %}
<h2>{{page.title}}</h2>
<ul>
{% for header in page.headers %}
<li><a href={{page.path}}#{{header.id}}>{{header.title}}</a></li>
{% endfor %}
</ul>
{% endfor %}
</div>
''')


class A(object):
    "Contains the information give by dr's `a` file."
    def __init__(self, fname='a'):
        with codecs.open(fname, encoding='utf-8') as f:
            self.a = f.read()
        t = self.a.split('\n')
        self.author = t[0]
        self.title = t[1]
        self.classifiers = t[2:]


# Regex for markdown files
content_file_re = re.compile(r'[A-Za-z0-9\-_]+\.md')

# See the python-markdown documentation on the syntax provided by these
# markdown extensions
exts = ['markdown.extensions.' + ext
        for ext in ['extra', 'admonition', 'codehilite', 'headerid',
                    'meta', 'sane_lists']]


def copy_ressources(frompath='content', to='build', types=r'png|jpg|gif'):
    "Copy everything where the filename matches param types"
    for fname in os.listdir(frompath):
        if not re.match(".*\.(" + types + ")", fname):
            continue
        path = os.path.sep.join([frompath, fname])
        shutil.copy2(path, os.path.sep.join([to, fname]))


def gen():
    "generate that shit"
    files = []
    md = Markdown(extensions=exts, output_format='html5')
    for path in os.listdir(os.path.sep.join([os.getcwd(), 'content'])):
        if not content_file_re.match(path):
            continue
        p = os.path.sep.join([os.getcwd(), "content", path])
        with codecs.open(p, encoding='utf-8') as f:
            content = f.read()
        html = md.convert(content)
        titles = []
        h2_re = re.compile(
            r'<h2 id="([a-z0-9\-]+)">([_a-zA-Z0-9\-\ \!\,]+)</h2>')
        for line in html.splitlines():
            match = h2_re.match(line)
            if match:
                titles.append({'id': match.group(1),
                               'title': match.group(2)})
        files.append({'path': path, 'title': md.Meta['title'][0],
                      'headers': titles, 'html': html})
    a = A()
    for d in files:
        real_html = site_template.render(site_title=a.title,
                                         page_title=d['title'],
                                         content=d['html'],
                                         navigation=files)
        path = d['path'].replace('.md', '.html')
        if not os.path.exists('build'):
            os.mkdir('build')
        with codecs.open(os.path.sep.join(['build', path]),
                         'w+',
                         encoding='utf-8') as f:
            f.write(real_html)


def main():
    gen()
    copy_ressources()
    shutil.copy2('a', os.path.sep.join(['content', 'a']))

if __name__ == '__main__':
    main()
