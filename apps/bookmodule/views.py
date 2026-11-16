from django.shortcuts import render , redirect, get_object_or_404
from apps.bookmodule.models import Book


from django.http import HttpResponse
from django.shortcuts import render

from django.urls import path
from . import views

from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from django.db.models import Count
from .models import Student, Address

from django.db.models import Sum, F, FloatField, ExpressionWrapper
from django.db.models.functions import Cast

from .models import Publisher
from django.db.models import Sum

from django.db.models import Min

from django.db.models import Avg, Min, Max

from django.db.models import Count, Q

from .forms import BookForm

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }

    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1

    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}

    return render(request, 'bookmodule/show.html', context)
def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")
    
def listing(request):
    return render(request, "bookmodule/listing.html")    

def tables(request):
    return render(request, "bookmodule/tables.html")

def search(request):

    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request, "bookmodule/search.html")


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def complex_query(request):
    mybooks = ( 
        Book.objects 
        .filter(author__isnull=False) 
        .filter(title__icontains='the') 
        .filter(edition__gte=2) 
        .exclude(price__lt=100)[:10]
     )
    if len(mybooks) >= 1:
        return render(
            request,
            'bookmodule/bookList.html',
            {'books': mybooks}
         )
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))

    return render(
        request,
        'bookmodule/lab8_task1.html',
        {'books': books}
    )

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) &
        (
            Q(title__icontains='co') |
            Q(author__icontains='co')
        )
    )
    return render(
        request,
        'bookmodule/lab8_task2.html',
        {'books': books}
    )

def lab8_task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        ~(
            Q(title__icontains='co') |
            Q(author__icontains='co')
        )
    )

    return render(
        request,
        'bookmodule/lab8_task3.html',
        {'books': books}
    )

def lab8_task4(request):
    books = Book.objects.order_by('title')

    return render(
        request,
        'bookmodule/lab8_task4.html',
        {'books': books}
    )

def lab8_task5(request):
    result = Book.objects.aggregate(
    total_books=Count('id'),
    total_price=Sum('price'),
    average_price=Avg('price'),
    maximum_price=Max('price'),
    minimum_price=Min('price')
    )

    return render(
        request,
        'bookmodule/lab8_task5.html',
        {'result': result}
    )

def lab8_task7(request):
    cities = Address.objects.annotate(
         student_count=Count('student')
    )

    return render(
        request,
        'bookmodule/lab8_task7.html',
        {'cities': cities}
    )

def lab9_task1(request):
    total_quantity = Book.objects.aggregate(
        total=Sum('quantity')
    )['total'] or 0

    books = Book.objects.annotate(
        availability=ExpressionWrapper(
            Cast(F('quantity'), FloatField()) * 100.0 / total_quantity
            if total_quantity else 0.0,
            output_field=FloatField()
        )
    )
    return render(
        request,
        'bookmodule/lab9_task1.html',
        {'books': books}
    )
def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('book__quantity')
    )

    return render(
        request,
        'bookmodule/lab9_task2.html',
        {'publishers': publishers}
    )

def lab9_task3(request):
    publishers = Publisher.objects.annotate(
             oldest_date=Min('book__pubdate')
    )

    return render(
        request,
        'bookmodule/lab9_task3.html',
        {'publishers': publishers}
    )

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        average_price=Avg('book__price'),
        minimum_price=Min('book__price'),
        maximum_price=Max('book__price')
    )

    return render(
        request,
        'bookmodule/lab9_task4.html',
        {'publishers': publishers}
    )

def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        highly_rated_count=Count(
        'book',
        filter=Q(book__rating__gte=4)
        )
    )

    return render(
        request,
        'bookmodule/lab9_task5.html',
        {'publishers': publishers}
    )

def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        books_count=Count(
            'book',
            filter=Q(
                book__price__gt=50,
                book__quantity__lt=5,
                book__quantity__gte=1
            )
        )
    )

    return render(
        request,
        'bookmodule/lab9_task6.html',
        {'publishers': publishers}
    )

def lab10_listbooks(request):
    books = Book.objects.all()

    return render(
        request,
        'bookmodule/lab10_listbooks.html',
        {'books': books}
    )

def lab10_addbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')

        Book.objects.create(
                title=title,
                author=author,
                price=price,
                edition=edition
        )

        return redirect('lab10_listbooks')

    return render(
        request,
        'bookmodule/lab10_addbook.html'
    )

def lab10_editbook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.edition = request.POST.get('edition')

        book.save()

        return redirect('lab10_listbooks')

    return render(
        request,
        'bookmodule/lab10_editbook.html',
        {'book': book}
    )

def lab10_deletebook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect('lab10_listbooks')

    return render(
        request,
        'bookmodule/lab10_deletebook.html',
        {'book': book}
    )

def lab10_part2_listbooks(request):
    books = Book.objects.all()

    return render(
        request,
        'bookmodule/lab10_part2_listbooks.html',
        {'books': books}
    )

def lab10_part2_addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lab10_part2_listbooks')
    else:
        form = BookForm()

    return render(
        request,
        'bookmodule/lab10_part2_addbook.html',
        {'form': form}
    )

def lab10_part2_editbook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('lab10_part2_listbooks')
    else:
        form = BookForm(instance=book)

    return render(
        request,
        'bookmodule/lab10_part2_editbook.html',
        {'form': form, 'book': book}
    )

def lab10_part2_deletebook(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect('lab10_part2_listbooks')

    return render(
        request,
        'bookmodule/lab10_part2_deletebook.html',
        {'book': book}
    )