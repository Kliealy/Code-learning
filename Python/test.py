import urllib.request

response = urllib.request.urlopen('https://www.mjtv.me/index.php/vod/play/id/6290/sid/1/nid/10.html')
print(response.read().decode('utf-8'))

