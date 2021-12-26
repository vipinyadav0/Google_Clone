from django.shortcuts import render

import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    if request.method=='POST':

        search = request.POST['search']
        # contextt = {'search':search}
        url = 'https://www.ask.com/web?q=' + search
        result = requests.get(url)
        soup = bs(result.text, 'lxml')

        all_lists = soup.find_all('div',{'class':'PartialSearchResults-item'})

        final_result = []
        search_k = []
        search_k.append(search)

        for result in all_lists:
            query_title = result.find(class_='PartialSearchResults-item-title').text
            query_url = result.find('a').get('href')
            query_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((query_title, query_url, query_desc))

        context ={
            'final_result': final_result,
            'search':search_k
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')