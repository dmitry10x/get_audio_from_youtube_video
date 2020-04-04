import pafy

url = 'https://www.youtube.com/watch?v=BqWPqZK-Ikg'
video = pafy.new(url)

bestaudio = video.getbestaudio()
bestaudio.download()


