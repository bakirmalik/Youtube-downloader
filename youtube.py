
'''
import os
import webbrowser

import urllib.request,urllib.error,urllib.parse

from bs4 import BeautifulSoup

# search for the best similar matching video
url = 'https://www.youtube.com/results?search_query' 

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
while True:
    query = input('Enter the song to be played: ')
    #check for injection and quit
    if(query == 'exit') : break
    
    elif query.startswith(("'","1=1")): break
    else:
        code = url + urllib.parse.urlencode({'':query})
        source_code = urllib.request.urlopen(code)
        soup = BeautifulSoup(source_code, "html.parser")





# fetches the url of the video
        songs = soup.findAll('div', {'class': 'yt-lockup-video'})
        song = songs[0].contents[0].contents[0].contents[0]
        link = song['href']
        webbrowser.open('https://www.youtube.com' + link)
        
