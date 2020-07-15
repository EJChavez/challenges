# API = application programming interface
import requests
from bs4 import BeautifulSoup
import pprint

# requests lets us download the HTML that we want to use
# BeautifulSoup is what lets us search through the HTML
for item in range(1, 3):
    res = requests.get(f'https://news.ycombinator.com/news?p={item}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    votes = soup.select('.score')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = votes[index].getText()
            points2 = points.rsplit()
            if int(points2[0]) > 100:
                hn.append({'title': title, 'link': href, 'votes': int(points2[0])})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, votes))
