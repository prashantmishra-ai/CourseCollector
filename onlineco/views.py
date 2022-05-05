
from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request, 'index2.html')
def about(request):
    return render(request, 'about.html')
def search(request):   
    if request.POST:
        query = request.POST.get('query')
        learning = request.POST.get('learning')
        import json
        import yaml
        client_id  = '{yourudemyClientID}'
        client_secret = '{ClientSecret}'
        import requests
        params  = f'{client_id}:{client_secret}'
        header = {
            'Authorization': 'Basic {BASE64_ENCODED(yourudemyClientID:ClientSecret)}'
        }
        if (learning != 'none'):
            query = query+' for '+learning
        data = requests.get(f'https://www.udemy.com/api-2.0/courses/?page=1&page_size=48&search={query}', headers=header, auth=(client_id, client_secret))
        jsondata = yaml.load(json.dumps(data.json()), Loader=yaml.FullLoader) #unicode to default json
        # for maindata in jsondata.get('results'):
        #     print('Course ID: ',maindata.get('id'))
        #     print('Course Name: ',maindata.get('title'))
        #     print('Course Image: ',maindata.get('image_240x135'))
        #     print('Paid: ',maindata.get('is_paid'))
        #     print('Course Header: ',maindata.get('headline'))
        #     print('Course Link: ','https://www.udemy.com'+maindata.get('url'))
        #     print('Predictive Score: ',maindata.get('predictivescore'))
        #     print('\n')

        # COURSES FROM YOUTUBE
        import json


        print(" YOUR COURSES FROM YOUTUBE: ")

        API_KEY = "{YoutubeAPIKey}"

        yt_search = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=45&q={query+'Courses'}&type=video&key={API_KEY}"
        yt_results = requests.get(yt_search)
        print(yt_results)
        myjsondata = yt_results.json()

        for i in myjsondata.get('items'):
            j = i.get('snippet')
            print("Title : ", j.get('title'))
            print("Description : ", j.get('description'))
            print("Image: ", j.get('thumbnails').get('default').get('url'))
        #     print("Paid : False")
            print('\n')
        params = {
            'title' : query,
            'udemy' : jsondata.get('results'),
            'youtube' : myjsondata.get('items')
        }
        return render(request, 'search2.html', params)
