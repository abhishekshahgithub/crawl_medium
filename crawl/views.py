from django.http import Http404
from django.shortcuts import render

from crawl.models import search_tag

from .forms import search_tag_form
from django.http import HttpResponse, HttpResponseRedirect
# from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import requests 
# ...
def index(request):
    
	search = search_tag.objects.all()

	data = []
	for i in search:
		data.append(i.tag)

	form = search_tag_form(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form = search_tag_form()
		# return HttpResponseRedirect(instance.get_absolute_url())
	tag = []
	for i in range(0, len(search)): 
		if i == (len(search)-1): 
			tag.append(str(search[i]))


	url = "https://medium.com/search?q="+tag[0]
	r = requests.get(url)	
	soup = BeautifulSoup(r.content)
	soup.find_all("h3")

	data2 = []

	for link in soup.find_all("h3"):
		data2.append(link.text)

	data = []

	for link in soup.find_all("h3"):
		data.append(link.text)


	context ={
		"form": form,
		"search": search,
		"data": data,
		"data2": data2
	}

	return render(request, 'crawl/index.html', context)
