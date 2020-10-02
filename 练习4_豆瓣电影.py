import requests
import json


def main():
    url = "https://movie.douban.com/j/search_subjects?"
    param = {
        "type": "movie",
        "tag": "欧美",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": "2"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }

    response = requests.get(url, params=param, headers=headers).json()

    data = json.dumps(response, ensure_ascii=False)
    print(data)

    with open(r"C:\Users\autof\Desktop\502s.text", "w", encoding="utf-8") as fp:
        fp.write(data)


if __name__ == "__main__":
    main()