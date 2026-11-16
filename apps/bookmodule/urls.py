from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links, name="books.html5_links"),
    path('html5/text/formatting', views.formatting, name="books.html5_formatting"),
    path('html5/listing', views.listing, name="books.html5_listing"),
    path('html5/tables', views.tables, name="books.html5_tables"),
    path('search', views.search, name='books.search'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    path('lab8/task1', views.lab8_task1, name='lab8_task1'),
    path('lab8/task2', views.lab8_task2, name='lab8_task2'),
    path('lab8/task3', views.lab8_task3, name='lab8_task3'),
    path('lab8/task4', views.lab8_task4, name='lab8_task4'),
    path('lab8/task5', views.lab8_task5, name='lab8_task5'),
    path('lab8/task7', views.lab8_task7, name='lab8_task7'),
    path('lab9/task1', views.lab9_task1, name='lab9_task1'),
    path('lab9/task2', views.lab9_task2, name='lab9_task2'),
    path('lab9/task3', views.lab9_task3, name='lab9_task3'),
    path('lab9/task4', views.lab9_task4, name='lab9_task4'),
    path('lab9/task5', views.lab9_task5, name='lab9_task5'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),
    path('lab10_part1/listbooks', views.lab10_listbooks, name='lab10_listbooks'),
    path('lab10_part1/addbook', views.lab10_addbook, name='lab10_addbook'),
    path('lab10_part1/editbook/<int:id>', views.lab10_editbook, name='lab10_editbook'),
    path('lab10_part1/deletebook/<int:id>', views.lab10_deletebook, name='lab10_deletebook'),
    path('lab10_part2/listbooks', views.lab10_part2_listbooks, name='lab10_part2_listbooks'),
    path('lab10_part2/addbook', views.lab10_part2_addbook, name='lab10_part2_addbook'),
    path('lab10_part2/editbook/<int:id>', views.lab10_part2_editbook, name='lab10_part2_editbook'),
    path('lab10_part2/deletebook/<int:id>', views.lab10_part2_deletebook, name='lab10_part2_deletebook'),
]


