from django.shortcuts import render
from . view_config import *
from .forms import SearchForm, SelectForm
from django.core.paginator import Paginator
import time

def search_field(request):
    items = ()
    selectform = SelectForm()
    searchform = SearchForm()

    if request.method == "POST" :
        if 'searchf' in request.POST:
            searchform = SearchForm(request.POST)
            if searchform.is_valid() :
                items = cur.execute(find_tender.format(searchform.cleaned_data['searchform'])).fetchall()
                    
        if 'selectf' in request.POST:
            selectform = SelectForm(request.POST)
            if selectform.is_valid() :
                search_keys = cats_analogue[selectform.cleaned_data['selectform']]
                for search_key in search_keys :
                    items = cur.execute(find_tender.format(search_key)).fetchall()

    return render(request, 'bid/search_field.html', { 'items' : items, 'searchform' : searchform, 'selectform' : selectform })

def moniter_field(request):
    boards_all = cur.execute(monitering_tender).fetchall()
    paginator = Paginator(boards_all, 10) #한 페이지 당 몇개 씩 보여줄 지 지정 
    page = request.GET.get('page') 
    boards = paginator.get_page(page)
    return render(request, "bid/moniter_field.html", {"boards":boards})

def detail_field(request, idk):
    item = cur.execute(detail_tender.format(idk)).fetchone()
    return render(request, 'bid/detail_field.html', { 'item' : item })
