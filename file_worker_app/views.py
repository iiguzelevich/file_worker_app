from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *
from .utils import *

menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'Publications', 'url_name': 'publish'},
    # {'title': 'About us', 'url_name': 'about'},
    # {'title': 'Services', 'url_name': 'services'},
    # {'title': 'News', 'url_name': 'news'},
    # {'title': 'Contact', 'url_name': 'contact'},
]
loads = [
    {'title': 'Load txt', 'url_name': 'load_txt'},
    {'title': 'Load pdf', 'url_name': 'load_pdf'},
    {'title': 'Load video', 'url_name': 'load_video'},
]
myfiles = [
    {'title': 'PDF Files', 'url_name': 'my_pdf_files'},
    {'title': 'Audio Files', 'url_name': 'my_audio_files'},
    {'title': 'GIF Files', 'url_name': 'my_gif_files'},
]


def index(request):
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
    }

    return render(request, 'file_worker_app/index.html', context=context)


def my_files(request):
    files = User.objects.filter(txttopdf__owner=request.user)
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'files': files
    }

    return render(request, 'file_worker_app/my_files.html', context=context)


def home(request):
    return HttpResponse('HOME')


def about(request):
    return HttpResponse('about')


def services(request):
    return HttpResponse('services')


def news(request):
    return HttpResponse('news')


def contact(request):
    return HttpResponse('contact')


@login_required(login_url="login")
def load_txt(request):
    user = request.user
    error = ''
    if request.method == 'POST':
        form = AddTextFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_text = form.cleaned_data.get('text_file')
            file_name = form.cleaned_data.get('file_name')

            file = TXTtoPDF.objects.create(
                owner=user,
                file_name=file_name,
                text_file=file_text
            )
            file_convert = convert_from_txt_to_pdf(
                file_text, user.id, file_name,
            )

            pdf_file = PDFfromTXT.objects.create(
                owner=user,
                original_file=file,
                file_name=file_name,
                pdf_file=f'user_{user.id}/pdf_files/{file_name}.pdf',
                format_file='text'

            )
            return redirect('home')
        else:
            error = 'Error'
    form = AddTextFileForm()
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'form': form,
        'error': error
    }
    return render(request, 'file_worker_app/load_txt.html', context=context)


@login_required(login_url="login")
def load_pdf(request):
    user = request.user
    error = ''
    if request.method == 'POST':
        form = AddPDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data.get('pdf_file')
            file_name = form.cleaned_data.get('file_name')

            file = PDFtoAudio.objects.create(
                owner=user,
                file_name=file_name,
                pdf_file=pdf_file,
            )

            file_convert = convert_from_pdf_to_audio(
                pdf_file, user.id, file_name
            )

            audio_file = AudiofromPDF.objects.create(
                owner=user,
                original_file=file,
                file_name=file_name,
                audio_file=f'user_{user.id}/audio_files/{file_name}.mp3'
            )

            return redirect('home')

        else:
            error = 'Error'

    form = AddPDFFileForm()
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'form': form,
        'error': error
    }
    return render(request, 'file_worker_app/load_pdf.html', context=context)


@login_required(login_url="login")
def load_video(request):
    user = request.user
    error = ''
    if request.method == 'POST':
        form = AddVideoFileForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = form.cleaned_data.get('video_file')
            file_name = form.cleaned_data.get('file_name')
            start = form.cleaned_data.get('start')
            stop = form.cleaned_data.get('stop')
            file = VideoToGIF.objects.create(
                owner=user,
                file_name=file_name,
                video_file=video_file
            )

            file_convert = convert_from_video_to_gif(
                video_file, user.id, file_name, start, stop,
            )

            gif_file = GIFfromVideo.objects.create(
                owner=user,
                original_file=file,
                file_name=file_name,
                gif_file=f'user_{user.id}/gif_files/{file_name}.gif'
            )
            return redirect('home')
        else:
            error = 'Error'
    form = AddVideoFileForm()
    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'form': form,
        'error': error
    }
    return render(request, 'file_worker_app/load_video.html', context=context)


@login_required(login_url="login")
def my_pdf_files(request):
    files = PDFfromTXT.objects.filter(
        owner__username=request.user
    ).order_by('-uploaded_at')

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'files': files,
    }

    return render(request, 'file_worker_app/my_pdf_files.html', context=context)


@login_required(login_url="login")
def my_audio_files(request):
    files = AudiofromPDF.objects.filter(
        owner__username=request.user
    ).order_by('-uploaded_at')

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'files': files
    }

    return render(request, 'file_worker_app/my_audio_files.html',
                  context=context)


@login_required(login_url="login")
def my_gif_files(request):
    files = GIFfromVideo.objects.filter(
        owner__username=request.user
    ).order_by('-uploaded_at')

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'selected': 0,
        'files': files
    }

    return render(request, 'file_worker_app/my_gif_files.html', context=context)


def edit_file_pdf(request, file_name):
    file = PDFfromTXT.objects.get(
        owner__username=request.user,
        file_name=file_name
    )

    if request.method == 'POST':
        form = EditPDFfromTextForm(request.POST)
        if form.is_valid():
            new_file_name = form.cleaned_data.get('file_name')
            old_path = file.pdf_file.path
            old_name = file.file_name
            new_path = old_path.replace(f'{old_name}', f'{new_file_name}')
            os.rename(old_path, new_path)
            file.pdf_file = (
                f'user_{request.user.id}/pdf_files/{new_file_name}.pdf'
            )
            file.file_name = new_file_name
            file.save()
        return redirect('home')
    form = EditPDFfromTextForm()

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'file': file,
        'form': form
    }
    return render(request, 'file_worker_app/edit_pdf_file.html',
                  context=context)


def delete_file_pdf(request, file_name):
    file = PDFfromTXT.objects.get(
        owner__username=request.user,
        file_name=file_name
    ).delete()
    return redirect('home')


def edit_file_audio(request, file_name):
    file = AudiofromPDF.objects.get(
        owner__username=request.user,
        file_name=file_name
    )

    if request.method == 'POST':
        form = EditAudiofromPDFForm(request.POST)
        if form.is_valid():
            new_file_name = form.cleaned_data.get('file_name')
            old_path = file.audio_file.path
            old_name = file.file_name
            new_path = old_path.replace(f'{old_name}', f'{new_file_name}')
            os.rename(old_path, new_path)
            file.audio_file = (
                f'user_{request.user.id}/audio_files/{new_file_name}.mp3'
            )
            file.file_name = new_file_name
            file.save()
        return redirect('home')
    form = EditPDFfromTextForm()

    context = {
        'FileWorker': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'file': file,
        'form': form
    }
    return render(request, 'file_worker_app/edit_audio_file.html',
                  context=context)


def delete_file_audio(request, file_name):
    file = AudiofromPDF.objects.get(
        owner__username=request.user,
        file_name=file_name,
    ).delete()
    return redirect('home')


def edit_file_gif(request, file_name):
    file = GIFfromVideo.objects.get(
        owner__username=request.user,
        file_name=file_name
    )
    if request.method == 'POST':
        form = EditGIFfromVideoForm(request.POST)
        if form.is_valid():
            new_file_name = form.cleaned_data.get('file_name')
            old_path = file.gif_file.path
            old_name = file.file_name
            new_path = old_path.replace(f'{old_name}', f'{new_file_name}')
            os.rename(old_path, new_path)
            file.gif_file = (
                f'user_{request.user.id}/gif_files/{new_file_name}.gif'
            )
            file.file_name = new_file_name
            file.save()
        return redirect('home')
    form = EditGIFfromVideoForm()

    context = {
        'title': 'FileWorker',
        'menu': menu,
        'loads': loads,
        'myfiles': myfiles,
        'file': file,
        'form': form
    }
    return render(request, 'file_worker_app/edit_gif_file.html',
                  context=context)


def delete_file_gif(request, file_name):
    file = GIFfromVideo.objects.get(
        owner__username=request.user,
        file_name=file_name
    ).delete()
    return redirect('home')
