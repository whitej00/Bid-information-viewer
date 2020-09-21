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