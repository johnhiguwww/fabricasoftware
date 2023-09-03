from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Movie1,Movie2,Movie3
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from datetime import datetime

# Create your views here.
def HomePage(request):
    if request.method == 'POST':
        moviename1 = request.POST.get('moviename1')
        synopsis1 = request.POST.get('synopsis1')
        moviename2 = request.POST.get('moviename2')
        synopsis2 = request.POST.get('synopsis2')
        moviename3 = request.POST.get('moviename3')
        synopsis3 = request.POST.get('synopsis3')

        movie1 = Movie1(movie1=moviename1, synopsis1=synopsis1)
        movie1.save()
        
        movie2 = Movie2(movie2=moviename2, synopsis2=synopsis2)
        movie2.save()
        
        movie3 = Movie3(movie3=moviename3, synopsis3=synopsis3)
        movie3.save()
        return GenerateMovieRanker(request, moviename1, synopsis1, moviename2, synopsis2, moviename3, synopsis3)
    return render(request, 'home.html')


def GenerateMovieRanker(request, moviename1, synopsis1, moviename2, synopsis2, moviename3, synopsis3):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="movie_ranker.pdf"'
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d/%m/%Y")

    p = canvas.Canvas(response, pagesize=landscape(letter))

    p.drawString(100, 750, "Movie 1:")
    p.drawString(150, 730, "Name: " + moviename1)
    p.drawString(150, 710, "Synopsis: " + synopsis1)

    p.drawString(100, 650, "Movie 2:")
    p.drawString(150, 630, "Name: " + moviename2)
    p.drawString(150, 610, "Synopsis: " + synopsis2)

    p.drawString(100, 550, "Movie 3:")
    p.drawString(150, 530, "Name: " + moviename3)
    p.drawString(150, 510, "Synopsis: " + synopsis3)

    p.drawString(100, 430, f"DATA: {formatted_datetime}")
    
    p.showPage()
    p.save()

    return response