import requests
import json
import execjs
import bs4

url = "https://www.copy-manga.com/comic/xxx"
headers = 'xxx'
save_path = r"D:\Python_Project\pythonProject\xxx"

resp = requests.get(url=f"{url}/chapters",
                        headers={'User-Agent': headers},
                        stream=True
                        )
data_dict = json.loads(resp.text)
results_value = data_dict.get('results')
with open('copy_comic.js', 'r', encoding='UTF-8') as f:
    js_code = f.read()
result = execjs.compile(js_code).call('decrypt', results_value)
chapters = result['groups']['default']['chapters']
chapter_ids = [chapter['id'] for chapter in chapters]
cnt = 1
for chapter_id in chapter_ids:
    img_html = requests.get(url=f"{url}/chapter/{chapter_id}",
                        headers={'User-Agent': headers},
                        stream=True
                        )
    soup = bs4.BeautifulSoup(img_html.text, 'html.parser')
    content_key = soup.find('div', class_='imageData').get('contentkey')
    img_dict = execjs.compile(js_code).call('decrypt', content_key)
    for image in img_dict:
        img_data = requests.get(image['url'],
                            headers={'User-Agent': headers},
                            stream=True
                            )
        with open(f"{save_path}/{int(cnt):05}.jpg", 'wb') as f:
            f.write(img_data.content)
        cnt += 1
