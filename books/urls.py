from django.urls import path
from .views import views
from .views.modelview import AuthorViewSet

urlpatterns= [
    path('books/', views.RetrieveBooks.as_view()),
    path('books/create/', views.CreateBook.as_view()),
    path('books/<int:book_id>/', views.RetrieveBookAPIView.as_view()),
    path('books/list/', views.ListBooksAPIView.as_view()),
    path('authors/', views.RetrieveAuthors.as_view()),
    path('authors/create/', views.CreateAuthor.as_view()),
    path('authors/<int:author_id>/', views.RetrieveAuthorAPIView.as_view()),
    path('authors/list/', views.ListAuthorsAPIView.as_view()),

    path('viewset/authors/list/', AuthorViewSet.as_view({'get':'list'})),
    path('viewset/authors/create/', AuthorViewSet.as_view({'post':'create'})),
    path('viewset/authors/<int:author_id>/', AuthorViewSet.as_view(
        {
            'get':'retrieve', 
            'put':'partial_update', 
            'delete':'destroy'
        }
    )),

]