from datetime import date

from django.db.models import Sum
from django.shortcuts import render

from .models import DistributionSetting, Expense, Income


def financial_summary(request):
  today = date.today()
  month = request.GET.get('month', today.month)
  year = request.GET.get('year', today.year)

  incomes = Income.objects.filter(date__year=year, date__month=month)
  expenses = Expense.objects.filter(date__year=year, date__month=month)

  total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
  total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
  net_profit = total_income - total_expense

  distribution = DistributionSetting.objects.last()
  owner_share = (distribution.owner_percentage / 100) * net_profit if distribution else 0
  investor_share = (distribution.investor_percentage / 100) * net_profit if distribution else 0

  context = {
    'incomes': incomes,
    'expenses': expenses,
    'total_income': total_income,
    'total_expense': total_expense,
    'net_profit': net_profit,
    'owner_share': owner_share,
    'investor_share': investor_share,
    'month': month,
    'year': year,
  }
  return render(request, 'financials/summary.html', context)