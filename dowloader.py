from pprint import pprint


def yt(link):
    # https://rapidapi.com/DataFanatic/api/youtube-media-downloader
    import requests
    import json

    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId": link}

    headers = {
        "X-RapidAPI-Key": "ed3a186353mshe8c319bda5f4f7ep193ae1jsnf1dabca08444",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    pprint(rest)
    return {'video': rest['videos']['items'][1]['url']}


def tk(link):
    import requests
    import json

    url = "https://tiktok-downloader-download-videos-without-watermark1.p.rapidapi.com/media-info/"

    querystring = {"link": link}

    headers = {
        "X-RapidAPI-Key": "ed3a186353mshe8c319bda5f4f7ep193ae1jsnf1dabca08444",
        "X-RapidAPI-Host": "tiktok-downloader-download-videos-without-watermark1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)

    return {'video': rest['result']['video']['url_list'][0]}


def ig(link):
    import requests
    import json
    url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "ed3a186353mshe8c319bda5f4f7ep193ae1jsnf1dabca08444",
        "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)

    return {'video': rest['video']}


def pn(link):
    import requests
    import json
    url = "https://pinterest-video-and-image-downloader.p.rapidapi.com/pinterest"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "ed3a186353mshe8c319bda5f4f7ep193ae1jsnf1dabca08444",
        "X-RapidAPI-Host": "pinterest-video-and-image-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rest = json.loads(response.text)
    return {'video': rest['data']['url']}
