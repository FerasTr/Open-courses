from bs4 import BeautifulSoup
import requests
import re
import sys

def main(argv):
    if (len(argv) == 0):
        sites=[
        'https://moodlearn.ariel.ac.il/course/index.php?categoryid=906&perpage=1000&browse=courses&page=0',
        'https://moodlearn.ariel.ac.il/course/index.php?categoryid=909&perpage=1000&browse=courses&page=0',
        'https://moodlearn.ariel.ac.il/course/index.php?categoryid=916&perpage=1000&browse=courses&page=0'
        ]
    else:
        sites=['https://moodlearn.ariel.ac.il/course/index.php?categoryid=' + argv[0] + '&perpage=1000&browse=courses&page=0']

    for site in sites:
        web = requests.get(site)
        soup = BeautifulSoup(web.text, 'html.parser')
        links = soup.find_all('i', class_="icon fa fa-unlock-alt fa-fw ")
        for tag in links:
            tag = tag.find_previous("a")
            link = tag.get('href',None)
            if link is not None:
                print link

if __name__ == "__main__":
   main(sys.argv[1:])
