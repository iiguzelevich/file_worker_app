from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from file_worker_app.models import AudiofromPDF, PDFfromTXT, GIFfromVideo
from publications.forms import CommentForm
from publications.models import *

from file_worker_app.views import menu, loads, myfiles


def publish_pdf(request, file_name):
    file = PDFfromTXT.objects.get(
        owner__username=request.user,
        file_name=file_name,
    )
    publish_file = PublishedFiles.objects.create(
        owner=request.user,
        file_name=file.file_name,
        is_published=1,
        format_file='pdf',
        file_source=file.pdf_file
    )
    file.is_published = True
    file.save(update_fields=["is_published"])

    return redirect('my_pdf_files')


def publish_audio(request, file_name):
    file = AudiofromPDF.objects.get(
        owner__username=request.user,
        file_name=file_name
    )
    publish_file = PublishedFiles.objects.create(
        owner=request.user,
        file_name=file.file_name,
        is_published=1,
        format_file='mp3',
        file_source=file.audio_file
    )
    file.is_published = True
    file.save(update_fields=["is_published"])

    return redirect('my_audio_files')


def publish_gif(request, file_name):
    file = GIFfromVideo.objects.get(
        owner__username=request.user,
        file_name=file_name
    )
    publish_file = PublishedFiles.objects.create(
        owner=request.user,
        file_name=file.file_name,
        is_published=1,
        format_file='gif',
        file_source=file.gif_file
    )
    file.is_published = True
    file.save(update_fields=["is_published"])

    return redirect('my_gif_files')


def publish(request):
    files = PublishedFiles.objects.all().order_by('-uploaded_at')
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'files': files
    }
    return render(request, 'publications/published.html', context=context)


@login_required(login_url="login")
def comment_file(request, file_name):
    user = request.user
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.published_file = PublishedFiles.objects.get(
                file_name=file_name
            )
            comment.owner = user
            comment.save()
            return redirect(request.path)
    form = CommentForm()

    file = PublishedFiles.objects.get(file_name=file_name)
    comments = Comments.objects.filter(
        published_file=file
    ).order_by('-uploaded_at')

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'form': form,
        'comments': comments,
        'file': file,
    }
    return render(request, 'publications/comment.html', context=context)


@login_required(login_url="login")
def subscribe(request, file_name):
    file = PublishedFiles.objects.get(file_name=file_name)
    (subscript, _) = Subscription.objects.get_or_create(owner=file.owner)

    (sub, _) = Subscriber.objects.get_or_create(
        subscriber_user=request.user,
        subscription=subscript
    )

    return redirect('publish')
