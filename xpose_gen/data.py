codehilite_css = '#content .codehilite code,#content .codehilite pre{color:#fdce93;background-color:#3f3f3f;padding:1.5em;}.codehilite .hll{background-color:#222}.codehilite .c{color:#7f9f7f}.codehilite .err{color:#e37170;background-color:#3d3535}.codehilite .g{color:#7f9f7f}.codehilite .k{color:#f0dfaf}.codehilite .l{color:#ccc}.codehilite .n{color:#dcdccc}.codehilite .o{color:#f0efd0}.codehilite .x{color:#ccc}.codehilite .p{color:#41706f}.codehilite .cm{color:#7f9f7f}.codehilite .cp{color:#7f9f7f}.codehilite .c1{color:#7f9f7f}.codehilite .cs{color:#cd0000;font-weight:bold}.codehilite .gd{color:#cd0000}.codehilite .ge{color:#ccc;font-style:italic}.codehilite .gr{color:red}.codehilite .gh{color:#dcdccc;font-weight:bold}.codehilite .gi{color:#00cd00}.codehilite .go{color:gray}.codehilite .gp{color:#dcdccc;font-weight:bold}.codehilite .gs{color:#ccc;font-weight:bold}.codehilite .gu{color:purple;font-weight:bold}.codehilite .gt{color:#0040D0}.codehilite .kc{color:#dca3a3}.codehilite .kd{color:#ffff86}.codehilite .kn{color:#dfaf8f;font-weight:bold}.codehilite .kp{color:#cdcf99}.codehilite .kr{color:#cdcd00}.codehilite .kt{color:#00cd00}.codehilite .ld{color:#cc9393}.codehilite .m{color:#8cd0d3}.codehilite .s{color:#cc9393}.codehilite .na{color:#9ac39f}.codehilite .nb{color:#efef8f}.codehilite .nc{color:#efef8f}.codehilite .no{color:#ccc}.codehilite .nd{color:#ccc}.codehilite .ni{color:#c28182}.codehilite .ne{color:#c3bf9f;font-weight:bold}.codehilite .nf{color:#efef8f}.codehilite .nl{color:#ccc}.codehilite .nn{color:#8fbede}.codehilite .nx{color:#ccc}.codehilite .py{color:#ccc}.codehilite .nt{color:#9ac39f}.codehilite .nv{color:#dcdccc}.codehilite .ow{color:#f0efd0}.codehilite .w{color:#ccc}.codehilite .mf{color:#8cd0d3}.codehilite .mh{color:#8cd0d3}.codehilite .mi{color:#8cd0d3}.codehilite .mo{color:#8cd0d3}.codehilite .sb{color:#cc9393}.codehilite .sc{color:#cc9393}.codehilite .sd{color:#cc9393}.codehilite .s2{color:#cc9393}.codehilite .se{color:#cc9393}.codehilite .sh{color:#cc9393}.codehilite .si{color:#cc9393}.codehilite .sx{color:#cc9393}.codehilite .sr{color:#cc9393}.codehilite .s1{color:#cc9393}.codehilite .ss{color:#cc9393}.codehilite .bp{color:#efef8f}.codehilite .vc{color:#efef8f}.codehilite .vg{color:#dcdccc}.codehilite .vi{color:#ffffc7}.codehilite .il{color:#8cd0d3}'
admonition_css = 'div.admonition {margin-top: 10px;margin-bottom: 10px;padding: 7px;}div.admonition dt {font-weight: bold;}div.admonition dl {margin-bottom: 0;}p.admonition-title {margin: 0px 10px 5px 0px;font-weight: bold;}div.body p.centered {text-align: center;margin-top: 25px;}div.admonition, div.warning {font-size: 0.9em;margin: 1em 0 1em 0;border: 1px solid #86989B;border-radius: 2px;background-color: #f7f7f7;padding: 0;}div.admonition p, div.warning p {margin: 0.5em 1em 0.5em 1em;padding: 0;}div.admonition pre, div.warning pre {margin: 0.4em 1em 0.4em 1em;}div.admonition p.admonition-title,div.warning p.admonition-title {margin-top: 1em;padding-top: 0.5em;font-weight: bold;}div.warning {border: 1px solid #940000;}div.warning p.admonition-title {}div.admonition ul, div.admonition ol,div.warning ul, div.warning ol {margin: 0.1em 0.5em 0.5em 3em;padding: 0;}'
template_string = u'''
<!doctype html>
<html>
<head>
<title>{{site_title}}</title>
<link rel="stylesheet" type="text/css" title="Xposés" href="http://www-igm.\
univ-mlv.fr/~dr/XPOSE/style.css"/>
<link rel="stylesheet" type="text/css" href="admonition.css" />
<link rel="stylesheet" type="text/css" href="codehilite.css" />
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
<li><a href={{page.html_path}}#{{header.id}}>{{header.title}}</a></li>
{% endfor %}
</ul>
{% endfor %}
</div>
'''
