from django.shortcuts import render, get_object_or_404
from shop.models import Item, Review
from django.http import HttpResponse


def year_archive(request, year):
    if year is not None:
        return HttpResponse('{}년도 자료 입니다.'.format(year))
    else:
        return HttpResponse('해당년도 자료는 없습니다.')

def my_sum(request, x, y):
    result = x + y
    output = '{} = {} + {}'.format(result, x, y)
    return HttpResponse(output)

def item_list(request):
    items = Item.objects.all()
    # return render(
    #     request,                    # 요청 정보
    #     'shop/item_list.html',    # 템플릿 이름
    #     {'item_list': items})      # 템플릿에 전달할 정보를 사전형태
    # request.GET 객체에게 키값이 'q'로 지정된 값을 요구해서 변수 q에 저장
    q = request.GET.get('q', '')  # 키값이 'q'로 지정된 값이 없으면 None이 반환됨 - 처음 화면을 띄우면 모든 items가 나타남
    if q:  # q가 널 아니면 items에 filter 조건 추가
        items = items.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {
        'item_list': items,
        'q': q,
    })

def item_detail(request, pk):  # 과제추가 - 현재 다른 연결이 딱히 없음
    item = get_object_or_404(Item, pk=pk)
    all_review = Review.objects.all()
    my_review = {}
    mystr = item.reviews
    for r in all_review:
        my_review[r.review_cmt] = str(mystr).find(r.review_cmt)
    return render(request, 'shop/item_detail.html', {
        'item': item,
        'item_review': all_review
    })


class MyClass:
    x = 10
    y = 20
    