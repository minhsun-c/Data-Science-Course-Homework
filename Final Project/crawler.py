import requests
from bs4 import BeautifulSoup

rellink = []

def getContent(url):
    crawl = Crawler()
    crawl.direct(url)
    p1 = crawl.browser.find(id='main')
    if p1:
        rst = p1.find('p')
        if rst == None:
            return None
        rst = rst.text
        if rst[-1] == ':':
            rst = rst[:len(rst)-1] + '.'
        return rst
    else:
        return None
    
class Crawler:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    def direct(self, url):
        self.url = url
        response = requests.get(url, headers=self.headers)
        self.browser = BeautifulSoup(response.content, 'html.parser')
        
class Header_Crawler(Crawler):
    def getHeader(self):
        self.navbar = [i.text.lower() for i in self.browser.find(id='subtopnav').find_all('a') if i.text != '']
        self.navlink = [i['href'] for i in self.browser.find(id='subtopnav').find_all('a') if i.text != '']
        global rellink
        for i in range(len(self.navlink)):
            nv = self.navlink[i].split('/')[1]
            rl = f'https://www.w3schools.com/{nv}/'
            rellink.append((self.navbar[i], rl))
    def legalChoice(self, keyword_l):
        for keyword in keyword_l.split():
            keyword = keyword.lower()
            if keyword == 'cpp':
                keyword = 'c++'
            for idx, nav in enumerate(self.navbar):
                if nav == keyword:
                    return nav, self.navlink[idx]
        return None, None
        
        
class W3S_Crawler(Crawler):
    def setLang(self, lang):
        self.lang = lang
        for rl in rellink:
            if rl[0] == lang:
                self.url_pre = rl[1]
    def getChoice(self, lang):
        print(self.url)
        self.setLang(lang)
        menu = self.browser.find(id="leftmenuinnerinner").find_all()
        self.titles = []
        self.choices = []
        self.setLang(lang)
        for idx, element in enumerate(menu):
            if element.name == 'a':
                self.choices.append((element.text, 'a', self.url_pre+element['href']))
            elif element.name == 'div':
                title = element.text.split('\n')[1]
                sub = [(i.text, self.url_pre+i['href']) for i in element.find_all('a')]
                self.choices.append([title, 'div', sub])
            elif element.name == 'h2':
                self.choices.append((element.text, 'h2'))
                self.titles.append((element.text, idx))
    def legalChoice(self, keywords):
        a_poss = []
        title_poss = []
        for keyword in keywords.split():
            keyword = keyword.lower()
            for idx, choice in enumerate(self.choices):
                if choice[1] == 'a' and self.isLegal(keyword, choice[0]):
                    content = getContent(choice[2])
                    if content == None: continue
                    a_poss.append((choice[0], choice[2], content))
                elif choice[1] == 'div':
                    if len(a_poss) != 0 and choice[0] == a_poss[-1][0]:
                        a_poss.pop()
                    for id, ch in enumerate(choice[2]):
                        if self.isLegal(keyword, ch[0]):
                            content = getContent(ch[1])
                            if content == None: continue
                            a_poss.append((ch[0], ch[1], content))
                elif choice[1] == 'h2' and self.isLegal(keyword, choice[0]):
                    if self.choices[idx+1][1] == 'a':
                        content = getContent(self.choices[idx+1][2])
                        if content == None: continue
                        title_poss.append((choice[0], self.choices[idx+1][2], content))
                    elif self.choices[idx+1][1] == 'div':
                        content = getContent(self.choices[idx+1][2][0][1])
                        if content == None: continue
                        title_poss.append((choice[0], self.choices[idx+1][2][0][1], content))
        return a_poss, title_poss
    def isLegal(self, keyword, ref):
        return keyword in ref.lower()


        
        
        
if __name__ == '__main__':
    w3s = W3S_Crawler('https://www.w3schools.com/python/default.asp')
    w3s.getChoice()
    w3s.legalChoice('list')
