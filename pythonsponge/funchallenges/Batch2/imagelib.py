# this should go to a helper file
from io import BytesIO
import pyodide_js
import struct
import js


async def load_package(pkg):
    await pyodide_js.loadPackage(pkg)


def load_image(link):
    from PIL import Image
    # Download image from internet
    x = js.XMLHttpRequest.new()
    x.open('get', link, False)
    x.overrideMimeType('text/plain; charset=x-user-defined')
    x.send()
    response = b''.join([struct.pack('B', (ord(cp)) & 0xff)
                        for cp in x.response])  # binary encode
    image = Image.open(BytesIO(response))
    return image
