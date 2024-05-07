#!/usr/bin/env python
"""
This example downloads a collection of images from https://http.cat/

Rather than downloading the images one-by-one, it runs multiple instances
of the download() function to complete the process faster.
"""

import tempfile
import urllib.request

from concurrently import concurrently


def save_http_cat(status_code):
    """
    Saves the JPEG from https://http.cat/ associated with this status code.

    Returns the path to the downloaded file.
    """
    _, path = tempfile.mkstemp(suffix=f"_{status_code}.jpg")
    urllib.request.urlretrieve(f"https://http.cat/{status_code}", path)
    return path


if __name__ == "__main__":
    codes = [200, 201, 202, 301, 302, 400, 405, 410, 418, 420, 451, 500]

    for input, output in concurrently(save_http_cat, inputs=codes):
        print(input, output)
