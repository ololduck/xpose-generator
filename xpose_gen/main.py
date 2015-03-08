# -*- coding: utf8 -*-
import os
import re
import sys
import codecs
import shutil
import logging
from markdown import Markdown
from jinja2 import Template
from zipfile import ZipFile
from errno import EEXIST
from .data import codehilite_css, admonition_css, template_string


logging.basicConfig()


# Regex for markdown files
content_file_re = re.compile(r'[A-Za-z0-9\-_]+\.md')

# See the python-markdown documentation on the syntax provided by these
# markdown extensions
exts = ['markdown.extensions.' + ext
        for ext in ['extra', 'admonition', 'codehilite', 'headerid',
                    'meta', 'sane_lists']]


class A(object):
    "Contains the information give by dr's `a` file."
    def __init__(self, fname='a'):
        with codecs.open(fname, encoding='utf-8') as f:
            self.a = f.read()
        t = self.a.split('\n')
        if len(t) <= 2:
            logging.warn('You have less than 3 lines in your `a` file, you \
                    should probably go read how to write it on the xpose page')
        self.author = t[0]
        self.title = t[1]
        self.classifiers = t[2:]


def zipit(inpath='build/html', topath='build', title=None):
    "zips a directory to title.zip. Every file will be in the zipfile as\
            title/filename"
    with ZipFile(os.path.sep.join([topath, str(title) + '.zip']), 'w') as zipf:
        for fname in os.listdir(inpath):
            zipf.write(os.path.sep.join([inpath, fname]),
                       os.path.sep.join([str(title), fname]))


def slugify(s):
    """
    Slugify a string

    >>> slugify("Hello, I'm a slug!")
    hello_im_a_slug
    """
    pathed_title = s.lower().replace(' ', '_')
    return re.sub('[\'\"\?,:]', '', pathed_title)


def makedirs(path):
    "This is akin unix's `mkdir -p`"
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def write_css(to='build/html'):
    with codecs.open(os.path.sep.join([to, 'admonition.css']), 'w+') as f:
        f.write(admonition_css)
    with codecs.open(os.path.sep.join([to, 'codehilite.css']), 'w+') as f:
        f.write(codehilite_css)


def copy_ressources(frompath='content', to='build',
                    types=r'[a-zA-Z0-9_\-\.]+\.(^md)'):
    "Copy everything where the filename matches param types"
    for fname in os.listdir(frompath):
        if not re.match(".*\.(" + types + ")", fname):
            continue
        path = os.path.sep.join([frompath, fname])
        shutil.copy2(path, os.path.sep.join([to, fname]))


def _get_files_info(frompath):
    "parses and gets meta-information from every file matching `path`"
    md = Markdown(extensions=exts, output_format='html5')
    files = []
    for path in os.listdir(os.path.sep.join([os.getcwd(), frompath])):
        if not content_file_re.match(path):
            continue
        p = os.path.sep.join([os.getcwd(), "content", path])
        with codecs.open(p, encoding='utf-8') as f:
            content = f.read()
        html = md.convert(content)
        titles = []
        h2_re = re.compile(
            r'<h2 id="([a-z0-9\-]+)">([_a-zA-Z0-9\- !,\.]+)</h2>')
        for line in html.splitlines():
            match = h2_re.match(line)
            if match:
                titles.append({'id': match.group(1),
                               'title': match.group(2)})
        if 'title' not in md.Meta:
            logging.error("You forgot to set the Title meta-information in %s"
                          % path)
            sys.exit(1)
        fdict = {'path': path, 'title': md.Meta['title'][0],
                 'headers': titles, 'html': html,
                 'html_path': re.sub('\.md', '.html', path)}
        if "navorder" not in md.Meta:
            logging.warn("No NavOrder set for file %s. Navigation menu may be"
                         " erronous. See documentation." % fdict['path'])
        else:
            fdict.update({'order': md.Meta['navorder'][0]})
        files.append(fdict)
    return files


def gen_html(frompath='content', to='build/html'):
    "generate that shit. Returns the 'slugified' version of the site title."
    site_template = Template(template_string)
    files = sorted(_get_files_info(frompath),
                   key=lambda e: e['order'] if 'order' in e else e['title'])
    a = A()
    for d in files:
        real_html = site_template.render(site_title=a.title,
                                         page_title=d['title'],
                                         content=d['html'],
                                         navigation=files)
        path = d['path'].replace('.md', '.html')
        with codecs.open(os.path.sep.join([to, path]),
                         'w+',
                         encoding='utf-8') as f:
            f.write(real_html)
    return slugify(a.title)


def main():
    makedirs(os.path.sep.join(['build', 'html']))
    pathed_title = gen_html()
    copy_ressources()
    write_css(os.path.sep.join(['build', 'html']))
    shutil.copy2('a', os.path.sep.join(['build', 'html', 'a']))
    zipit(inpath=os.path.sep.join(['build', 'html']),
          topath='build',
          title=pathed_title)

if __name__ == '__main__':
    main()
