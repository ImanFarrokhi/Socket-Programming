from typing import Dict, List
import urllib.request
#testing Git

def make_file(url: str, filename: str) -> None:
    html_res = urllib.request.urlopen(url)
    html_content = html_res.read()
    with open(f"serverfile/{filename}", "w") as file:
        file.write(html_content.decode())


def get_websites() -> List[Dict[str, str]]:
    return [
        {
            "url": "https://www.python.org",
            "filename": "python.org.html"
        },
        {
            "url": "https://leetcode.com/",
            "filename": "leetcode.com.html"
        },
        {
            "url": "https://www.hackerrank.com/",
            "filename": "www.hackerrank.com.html"
        },
        {
            "url": "https://codeforces.com/",
            "filename": "codeforces.com.html"
        },
        {
            "url": "https://www.ldoceonline.com/",
            "filename": "www.ldoceonline.com.html"
        },
        {
            "url": "https://dictionary.cambridge.org",
            "filename": "dictionary.cambridge.org.html"
        },
        {
            "url": "https://vmusic.ir/",
            "filename": "vmusic.ir.html"
        },
        {
            "url": "https://www.speedtest.net/",
            "filename": "www.speedtest.net.html"
        },
        {
            "url": "https://www.typingtest.com/",
            "filename": "www.typingtest.com.html"
        },
        {
            "url": "https://kaboompics.com/",
            "filename": "kaboompics.com.html"
        },
    ]


if __name__ == "__main__":
    websites = get_websites()
    for website in websites:
        print(website["url"])
        make_file(website["url"], website["filename"])