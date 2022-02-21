from django.shortcuts import render
from .models import AccountBook
import calendar
import datetime

# Create your views here.
def account(request):
    querysets = AccountBook.objects.filter(email=request.session['email'])
    if request.method == 'GET':
        current_year = datetime.date.year
        current_month = datetime.date.month
        print(querysets)
        return render(request, 'account_book/account.html', {'username': request.session['username']})
    else:
        return render(request, 'account_book/account.html', {})

