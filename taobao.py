import requests, re, urllib.request, os

def get_html_code(url):
    html_code = requests.get(url).text
    return html_code
def get_mp4_code(html):
    reg = recompile(r'<div class="j-r-list-c">.*?</div>.*?</div>', re.s)
    return re.findall(reg, html)
def get_mp4_url(item):
    reg = re.compile(r'data-mp4="(.*?)">')
    return re.findall(reg, item)
def get_mp4_name(item):
    reg = re.compile(r'<a href="/detail-\d{8}.html">(.*?)</a>')
    return re.findall(reg, item)
