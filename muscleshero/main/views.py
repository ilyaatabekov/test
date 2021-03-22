from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def weak(request):
    return  render(request, 'main/weak.html')

def weak_1(request):
    return render(request, 'main/weak_1.html')

def day1(request):
    return  render(request, 'main/days_1/day1.html')

def day2(request):
    return  render(request, 'main/days_1/day2.html')

def day3(request):
    return  render(request, 'main/days_1/day3.html')

def day4(request):
    return  render(request, 'main/days_1/day4.html')

def day5(request):
    return  render(request, 'main/days_1/day5.html')

def day6(request):
    return  render(request, 'main/days_1/day6.html')

def day7(request):
    return  render(request, 'main/days_1/day7.html')


def weak_2(request):
    return render(request, 'main/weak_2.html')

def day1_2(request):
    return  render(request, 'main/days_2/day1_2.html')

def day2_2(request):
    return  render(request, 'main/days_2/day2_2.html')

def day3_2(request):
    return  render(request, 'main/days_2/day3_2.html')

def day4_2(request):
    return  render(request, 'main/days_2/day4_2.html')

def day5_2(request):
    return  render(request, 'main/days_2/day5_2.html')

def day6_2(request):
    return  render(request, 'main/days_2/day6_2.html')

def day7_2(request):
    return  render(request, 'main/days_2/day7_2.html')