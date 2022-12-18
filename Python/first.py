import requests

m_url = 'https://dl.stream.qqmusic.qq.com/C400003pyeir0FV236.m4a?guid=9892066488&vkey=3E2FF712482A60B3C9EB32F1E75DE7770F3CFB47489C806F690428457532B73E393953D4DC970EF946CA9F7059422B8035EBE7EF2197FCC0&uin=482165350&fromtag=120032'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.0.0'
}

m_resp = requests.get(m_url, headers=headers)

with open('The Night.mp3', 'wb') as f:
    f.write(m_resp.content)
