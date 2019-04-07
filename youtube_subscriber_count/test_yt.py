import urllib2

data = {
        "blacksheep": "AIzaSyBpHk5xwwRH1HQALYiL4l1QcKz4h1E3nD8" ,
        "parithabangal": "UCueYcgdqos0_PzNOq81zAFg",
        "behindwoods": "behindwoodstv"
}

channel_id = 'UCzh5hQc_O3r3xjh9sXrM7-A'
yt_command = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+ channel_id + "&key=" + your_key

name = "behindwoodstv"
yt_command2 = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + name+ "&key="+ your_key

res = urllib2.urlopen(yt_command2)

#res = urllib2.urlopen(yt_command)
print res.read()

