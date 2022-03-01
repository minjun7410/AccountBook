from django.shortcuts import render
from .models import AccountBook
import calendar
import datetime
weekdays = [1,2,3,4,5,6,0]
# Create your views here.
def account(request):
    if request.method == 'GET':
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        querysets = AccountBook.objects.filter(email=request.session['email_id'],
                                               month=current_month,
                                               year=current_year).order_by('day')
        monthrange = calendar.monthrange(current_year, current_month)  # return (start weekday, day_num)
        day_data = [(weekdays[datetime.date(current_year, current_month, _).weekday()], []) for _ in range(1, monthrange[1]+1)]  # index: day-1, value: (weekday, query list)
        for query in querysets:
            day_data[query.day-1][1].append(query)
        day_table = [[None for _ in range(7)] for _ in range(5)]
        day = 0
        for i in range(5):
            for j in range(7):
                if day >= monthrange[1]: break
                if j == day_data[day][0]:
                    print(day)
                    day_table[i][j] = (day+1, day_data[day-1][1])
                    day += 1

        return render(request, 'account_book/account.html', {'username': request.session['username'],
                                                             'current_year': current_year,
                                                             'current_month': current_month,
                                                             'monthrange': monthrange,
                                                             'day_table': day_table,
                                                             'irange': range(5),
                                                             'jrange': range(7)})
    else:
        return render(request, 'account_book/account.html', {'username': request.session['username']})

