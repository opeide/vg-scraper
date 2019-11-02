import time
import numpy
import requests
from bs4 import BeautifulSoup


def scrape():
    nArticles = 1000
    article_delimiter = '\n<|end|>\n'
    top_bottom_delimiter = '\n' #delimiter between headline and lead paragraph
    file_path = 'titles.txt'
    with open(file_path, 'w+') as f:
        print('scraping...')
        for offset in range(0,nArticles,20):
            print(offset)
            url = f'http://arkivet.vg.no/index.php?datofra=01.01.2000&datotil=29.10.2019&offset={offset}'
            response = requests.get(url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            stories = soup.find_all('span', class_='storyintro')
            for story in stories:
                topText = story.find('strong')
                if topText:
                    topText = topText.get_text()
                else:
                    topText = ''
                bottomText = story.find('field')
                if bottomText:
                    bottomText = bottomText.get_text()
                else:
                    bottomText = ''
                f.write(f'{topText}{top_bottom_delimiter}{bottomText}{article_delimiter}')


if __name__ == '__main__':
    scrape()