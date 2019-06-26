import random
import string
from io import BytesIO
from PIL import Image

from django.utils.text import slugify
from django.core.validators import RegexValidator
from django.core.files.images import get_image_dimensions

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """generating random strings"""
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(name, new_slug=None):
	slug = slugify(name)
	new_slug =  "{slug}_{randstr}".format(
	            slug=slug,
	            randstr=random_string_generator(size=8)
	        )
	return new_slug

def image_modification_tool(imgobj, bw):
    basewidth = bw
    img = Image.open(imgobj.file)
    if get_image_dimensions(imgobj.file)[0] > basewidth:
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        image_file = BytesIO()
        if imgobj.url.split('.')[-1] == 'png':
            img.save(image_file, 'PNG', quality=95)
        else:
            img.save(image_file, 'JPEG', quality=95)
        imgobj.file = image_file

top_five = (
    ('a', '1'),
    ('b', '2'),
    ('c', '3'),
    ('d', '4'),
    ('e', '5'),
)

watch_statuses = (
    ('h', 'Waiting For Next Release'),
    ('w', 'Completed'),
    ('s', 'Started Watching'),
    ('n', 'Wish to Watch'),
)
site_types = (
    ('ed', 'Educational'),
    ('sr', 'Subreddit'),
    ('yt', 'Youtube Channel'),
    ('nm', 'News & Magazine'),
    ('ut', 'useful Tools'),
    ('po', 'Portfolio'),
    ('pr', 'Programming'),
    ('ar', 'Art'),
    ('mo','Money'),
)
alphasymspace = RegexValidator(
    r"^[a-zA-Z0-9 %&#?!();.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")
alphanumspacedash = RegexValidator(
    r'^[a-zA-Z0-9 -]*$', 'Alphanumeric characters, dash & space allowed.')
alphanumspacedashq = RegexValidator(
    r"^[a-zA-Z0-9 -']*$", 'Alphanumeric characters, dash, single-quote & space allowed.')
positivenum = RegexValidator(r'^[1-9]\d*$', 'Only Postive numbers allowed')
