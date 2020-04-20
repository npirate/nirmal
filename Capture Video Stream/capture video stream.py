import urllib.request as urllib2
link_to_movie = 'https://www.hotstar.com/movies/badhaai-ho/1000120365/watch'

file_name = 'themovie.mp4' 
response = urllib2.urlopen(link_to_movie)
with open(file_name,'wb') as f:
    f.write(response.read())
