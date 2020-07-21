from flask import request
from urllib.parse import urlparse, urljoin


def is_safe_url(target):
    # print("request.host_url:", request.host_url)

    ref_url = urlparse(request.host_url)

    # print("ref_url:", ref_url)

    # print("target:", target)

    test_url = urlparse(urljoin(request.host_url, target))

    # print("test_url:", test_url)

    # print("ref_url.netloc:", ref_url.netloc)

    # print("test_url.netloc:", test_url.netloc)

    # print("test_url.scheme:", test_url.scheme)

    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

# is_safe_url('https://www.cnblogs.com/xiaxiaoxu/p/10409886.html')
