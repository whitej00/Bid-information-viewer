from django.shortcuts import render
from . view_config import *
from .forms import SearchForm, SelectForm

def bid_field(request):
    items = ()
    selectform = SelectForm()
    searchform = SearchForm()

    if request.method == "POST" :
        if 'searchf' in request.POST:
            searchform = SearchForm(request.POST)
            if searchform.is_valid() :
                search_keys = cats_analogue[searchform.cleaned_data['searchform']]
                for search_key in search_keys :
                    items = cur.execute(find_tenders.format(search_key)).fetchall()
        if 'selectf' in request.POST:
            selectform = SelectForm(request.POST)
            if selectform.is_valid() :
                search_keys = cats_analogue[selectform.cleaned_data['selectform']]
                for search_key in search_keys :
                    items = cur.execute(find_tenders.format(search_key)).fetchall()

    return render(request, 'bid/bid_field.html', { 'items' : items, 'searchform' : searchform, 'selectform' : selectform })

def moniter_field(request):
    items = cur.execute(monitering_tenders).fetchall()
    qtys = cur.execute(total_qty).fetchone()
    tenders = cur.execute(all_tenders).fetchall()
    total = cur.execute(all_total).fetchone()

    return render(request, 'bid/moniter_field.html', { 'items' : items, 'qtys' : qtys, 'tenders' : tenders, 'total' : total })

def bid_dtfield(request, idk):
    item = cur.execute(detail_tenders.format(idk)).fetchone()
    return render(request, 'bid/bid_dtfield.html', { 'item' : item })
