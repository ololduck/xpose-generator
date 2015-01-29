# xpose-generator

This simple script is something I did rather quickly to generate the website we
needed to create in the context of the [presentations done in third year of CS
engineering at ESIPE][1].

It is very simple: it takes the information describe in `a`, a text file
containing meta-information, and every markdown file it finds in `content`, and
generates the proper html tree in `build`.

## Installation / Upgrade

    pip install -U xpose-generator

Once this is done, you can call `xposegen`, in the directory of your choice,
where there is a [`a`][2] file, and a `content/` directory.

## How to write content:

Write the `a` file required by ESIPE's integration system, following the
instructions [here][2].

Simply write a .md file in `content/`, write a line `Title: My Title Here` on
top of the file, and then write your content. Note: For presentation purpose,
don't write `h1` tags, aka `#`, in markdown. 

Here be samples (and dragons):

    Title: This is my test page
    NavOrder: 1
    ## Hello, world

    Hello, world. I am writing some stuff in markdown.
    [This is a link to another page, with header][hello.html#title]

*note*: if you have many pages, set the `Order: <incremental_number>` property,
so the pages will be in that order on the navigation menu.

If you have images, etc... Just put it in `content/` with everything else.

So you have (approximately, you may have more files in `content/`...) this
structure:

    [paul@styx:xpose] master ± tree
    .
    ├── a
    └── content
        └── index.md

To have more information about how to write markdown, check [github's guide to
markdown][3]. This will give you the basis. To know more about the supported
syntax, see the documentation of [python-markdown][4]. The following extensions
are used: [extra][5], [admonition][6], [codehilite][7], [headerid][8],
[sane_lists][9]

# Contributing

Please, feel free to clone the repository, make your stuff, and eventually make
a pull request to merge what you did? That would be nice.

Also, even if you don't want to merge your code, an email will be appreciated.

## TODO

* Support subdirectory use in `content/`
* Add support for custom css
* do not hard-code everything; add support for cli args, or conffile
* Decrease every header if a `# title` is detected.
* Use the generated `h1` title as page's title, and strip it from final HTML.
* Add `next` and `prev` buttons on every page, linking to the next page in
  NavOrder.


[1]: http://www-igm.univ-mlv.fr/~dr/xall.php
[2]: http://www-igm.univ-mlv.fr/~dr/XPOSE/modalites.html
[3]: https://help.github.com/articles/markdown-basics
[4]: http://pythonhosted.org//Markdown
[5]: http://pythonhosted.org//Markdown/extensions/extra.html
[6]: http://pythonhosted.org//Markdown/extensions/admonition.html
[7]: http://pythonhosted.org//Markdown/extensions/code_hilite.html
[8]: http://pythonhosted.org//Markdown/extensions/header_id.html
[9]: http://pythonhosted.org//Markdown/extensions/sane_lists.html

<!-- vim: tw=80:spell:spelllang=en
-->
