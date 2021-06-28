import requests
from bs4 import BeautifulSoup


URL= "https://en.wikipedia.org/wiki/History_of_Mexico"

def  get_citations_needed_count(url):
    page= requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    results=soup.find(class_='mw-parser-output')
    citation_results=results.findAll('a',title='Wikipedia:Citation needed')
    return len(citation_results)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_result=soup.find(class_='mw-parser-output')
    result = all_result.findAll('p')
    result_with_citations=[]
    for i in result:
        citation =i.findAll('a',title='Wikipedia:Citation needed')
        if len(citation)>0:
            for j in citation:
                result_with_citations.append(i.text.strip()) 

    return "\n\n".join(result_with_citations)





if __name__ == "__main__":
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))