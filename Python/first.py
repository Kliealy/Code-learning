import requests

m_url = 'https://dl.stream.qqmusic.qq.com/C400004Rhcva2nyTJ0.m4a?guid=3801622700&vkey=A35E21D4D91029D65DB70135AA41DD4F8134150A3C95972CDA697456D8D77F0B66A8E7049B90FC600E81F2E076F8528A2E6CC7DEC8735020&uin=482165350&fromtag=120032'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
m_resp = requests.get(m_url, headers=headers)
with open('zzz.mp3', 'wb') as f:
    f.write(m_resp.content)

