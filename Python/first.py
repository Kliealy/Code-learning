import requests

m_url = 'https://dl.stream.qqmusic.qq.com/C400001MEsH00VICBA.m4a?guid=1693308126&vkey=F0765618E41A7386834D4C12DFEDF903AB02F2496BD3C2389ACF0349BF8D837415AA938CA5F1604FFD78E1DD49D2A2A1572716D4E44939FC&uin=482165350&fromtag=120032'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.0.0'
}

m_resp = requests.get(m_url, headers=headers)

with open('再回首.mp3', 'wb') as f:
    f.write(m_resp.content)
