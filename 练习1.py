import requests


def main():

    url = "https://www.bilibili.com/"
    respone = requests.get(url)
    data = respone.text
    print(data)

    with open(r"C:\Users\autof\Desktop\百片.text", "w", encoding="utf-8") as fp:
        fp.write(data)


if __name__ == '__main__':
    main()