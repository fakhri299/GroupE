import requests
import re
from bs4 import BeautifulSoup
import os

download_dir=os.path.expanduser("~/Downloads")
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/58.0.3029.110 Safari/537.36'}


#NR-finds_exploit_url finds exploit-db links if possible

def find_exploit_url(cve_identifier):
    search_url = f"https://cve.mitre.org/cgi-bin/cvename.cgi?name={cve_identifier}"
    response=requests.get(search_url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    links= soup.find_all('a')
    exploit_links=[]
    for link in links:
        href=link.getText('href')
        if href and "exploit-db.com" in href:
            exploit_links.append(href)
    url_pattern = re.compile(r'^URL:(https?://[^\s]+)')
    urls = [url_pattern.match(line).group(1) for line in exploit_links if url_pattern.match(line)]
    return urls

#NR-getcontent(cve_id) gets exploit-db download link

def getcontent(cve_id):
    links=find_exploit_url(cve_id)
    if len(links)>=1:
        mlink=links[0]
        if mlink.endswith('/'):
            mlink = mlink.rstrip('/')
        parts=mlink.split('/')
        elink=parts[-1]
        return f"https://www.exploit-db.com/download/{elink}"
    else:
        return "0"