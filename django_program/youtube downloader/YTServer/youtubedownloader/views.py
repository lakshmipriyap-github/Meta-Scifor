# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *
from django.http import HttpResponse
from yt_dlp import YoutubeDL


def youtube(request):

    if request.method == 'POST':
        #getting link from frontend
        link = request.POST['link']
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'C:/Users/vinod/Downloads/%(title)s.%(ext)s',
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            return HttpResponse(f"Download complete. File name : {info_dict['title']}")
    return render(request, 'ytdownload.html')