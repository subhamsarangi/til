import random
import string
from io import BytesIO
from PIL import Image

from django.utils.text import slugify
from django.core.validators import RegexValidator
from django.core.files.images import get_image_dimensions

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
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
langs = (
    ('en', 'English'),
    ('bn', 'Bangla'),
    ('hi', 'Hindi'),
    ('de', 'German'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('pe', 'Persian'),
    ('sv', 'Swedish'),
    ('fr', 'French'),
    ('ta', 'Tamil'),
    ('ka', 'Kannada'),
    ('oth', 'Others'),
)

movie_tv_genre = (
    ('dra', 'Drama'),
    ('scf', 'Sci-Fi'),
    ('thr', 'Thriller'),
    ('adv', 'Adventure'),
    ('ron', 'Romance'),
    ('co', 'Comedy'),
    ('rcm', 'Romcom'),
    ('fan', 'Fantasy'),
    ('sup', 'Superhero'),
    ('psy', 'Psychological Thriller'),
    ('lgl', 'Legal Drama'),
    ('mld', 'Military Drama'),
    ('mlt', 'Milirary Thriller'),
    ('his', 'Historical Fiction'),
    ('bio', 'Biopic'),
    ('doc', 'Documentary'),
    ('med', 'Medical Drama'),
    ('cor', 'Corporate'),
    ('dys', 'Dystopia'),
    ('uto', 'Utopia'),
    ('exp', 'Experimental'),
    ('noi', 'Film Noir'),
    ('mus', 'Musical'),
    ('oth', 'Others'),
)
watch_statuses = (
    ('w', 'Watched'),
    ('n', 'Not watched'),
    ('s', 'Started'),
    ('h', 'Halfway through'),
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
    r"^[a-zA-Z0-9 %&#?!;.,'+/*-]*$", "Alphanumeric characters, space and %&#?!;.,'+/*- are allowed.")
alphanumspacedash = RegexValidator(
    r'^[a-zA-Z0-9 -]*$', 'Alphanumeric characters, dash & space allowed.')
alphanumspacedashq = RegexValidator(
    r"^[a-zA-Z0-9 -']*$", 'Alphanumeric characters, dash, single-quote & space allowed.')
positivenum = RegexValidator(r'^[1-9]\d*$', 'Only Postive numbers allowed')
