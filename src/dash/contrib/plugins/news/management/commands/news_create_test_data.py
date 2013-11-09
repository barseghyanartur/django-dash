import subprocess
import random
import os
import uuid
import logging
import zipfile
import shutil

from six import text_type, PY3
from six.moves.urllib import request

if PY3:
    from string import punctuation
else:
    from string import translate, maketrans, punctuation

import radar

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.conf import settings

from dash.contrib.plugins.news.models import NewsItem, NEWS_IMAGES_STORAGE_PATH

logger = logging.getLogger(__file__)

FACTORY = """
    Sed dictum in tellus non iaculis. Aenean ac interdum ipsum. Etiam tempor quis ante vel rhoncus. Nulla
    facilisi. Curabitur iaculis consequat odio ut imperdiet? Integer accumsan; nisl vitae fermentum malesuada,
    sapien nulla sodales orci, et elementum lacus purus vel purus! Nullam orci neque, tristique in porta id,
    pretium ac sem. Fusce non est risus. Fusce convallis tellus augue, quis volutpat tellus dapibus sagittis.
    Integer lacinia commodo risus vel cursus. Etiam vitae dui in dolor porta luctus sed id elit. Nulla et est
    nec magna facilisis sagittis. Praesent tincidunt dictum lectus, sed aliquam eros. Donec placerat tortor ut
    lorem facilisis congue. Quisque ac risus nibh. Etiam ultrices nibh justo; sed mollis ipsum dapibus vitae.Ut
    vitae molestie erat. Mauris ac justo quis ante posuere vehicula. Vivamus accumsan mi volutpat diam lacinia,
    vitae semper lectus pharetra. Cras ultrices arcu nec viverra consectetur. Cras placerat ante quis dui
    consequat cursus. Nulla at enim dictum, consectetur ligula eget, vehicula nisi. Suspendisse eu ligula vitae
    est tristique accumsan nec adipiscing risus.Donec tempus dui eget mollis fringilla. Fusce eleifend lacus lectus,
    vel ornare felis lacinia ut. Morbi vel adipiscing augue. Vestibulum ante ipsum primis in faucibus orci luctus et
    ultrices posuere cubilia Curae; Cras mattis pulvinar lacus, vitae pulvinar magna egestas non. Aliquam in urna
    quis leo feugiat faucibus. Aliquam erat volutpat. Maecenas non mauris libero. Suspendisse nisi lorem, cursus a
    tristique a, porttitor in nisl. Mauris pellentesque gravida mi non mattis. Cras mauris ligula, interdum semper
    tincidunt sed, ornare a ipsum. Nulla ultrices tempus tortor vitae vehicula.Etiam at augue suscipit, vehicula
    sapien sit amet; eleifend orci. Etiam venenatis leo nec cursus mattis. Nulla suscipit nec lorem et lobortis.
    Donec interdum vehicula massa sed aliquam. Praesent eleifend mi sed mi pretium pellentesque. In in nisi tincidunt,
    commodo lorem quis; tincidunt nisl. In suscipit quam a vehicula tincidunt! Fusce vitae varius nunc. Proin at
    ipsum ac tellus hendrerit ultricies. Phasellus auctor hendrerit sapien viverra facilisis. Suspendisse lacus erat,
    cursus at dolor in, vulputate convallis sapien. Etiam augue nunc, lobortis vel viverra sit amet, pretium et
    lacus.Pellentesque elementum lectus eget massa tempus elementum? Nulla nec auctor dolor. Aliquam congue purus
    quis libero fermentum cursus. Etiam quis massa ac nisl accumsan convallis vitae ac augue. Mauris neque est,
    posuere quis dolor non, volutpat gravida tortor. Cum sociis natoque penatibus et magnis dis parturient montes,
    nascetur ridiculus mus. Vivamus ullamcorper, urna at ultrices aliquam, orci libero gravida ligula, non pulvinar
    sem magna sed tortor. Sed elementum leo viverra ipsum aliquet convallis. Suspendisse scelerisque auctor sapien.
    Mauris enim nisl, sollicitudin at rhoncus vitae, convallis nec mauris. Phasellus sollicitudin dui ut luctus
    consectetur. Vivamus placerat, neque id sagittis porttitor, nunc quam varius dolor, sit amet egestas nulla
    risus eu odio. Mauris gravida eleifend laoreet. Aenean a nulla nisl. Integer pharetra magna adipiscing, imperdiet
    augue ac, blandit felis. Cras id aliquam neque, vel consequat sapien.Duis eget vulputate ligula. Aliquam ornare
    dui non nunc laoreet, non viverra dolor semper. Aenean ullamcorper velit sit amet dignissim fermentum! Aenean urna
    leo, rutrum volutpat mauris nec, facilisis molestie tortor. In convallis pellentesque lorem, a lobortis erat
    molestie et! Ut sed sem a odio aliquam elementum. Morbi pretium velit libero, adipiscing consequat leo dignissim
    eu. Mauris vestibulum feugiat risus; quis pharetra purus tincidunt quis. Morbi semper tincidunt lorem id iaculis.
    Quisque non pulvinar magna. Morbi consequat eleifend neque et iaculis. Fusce non laoreet urna. Donec ut nunc
    ultrices, fringilla nunc ut, tempor elit. Phasellus semper sapien augue, in gravida neque egestas at.
    Integer dapibus lacus vitae luctus sagittis! Suspendisse imperdiet tortor eget mattis consectetur. Aliquam viverra
    purus a quam lacinia euismod. Nunc non consequat mi; ac vehicula lacus. Pellentesque accumsan ac diam in fermentum!
    Maecenas quis nibh sed dolor adipiscing facilisis. Aenean vel arcu eu est fermentum egestas vulputate eget purus.
    Sed fermentum rhoncus dapibus. Quisque molestie magna eu accumsan lobortis. Vestibulum cursus euismod posuere.
    Aliquam eu dapibus urna. Nulla id accumsan justo. Vivamus vitae ullamcorper tellus. Class aptent taciti sociosqu
    ad litora torquent per conubia nostra, per inceptos himenaeos.Donec pulvinar tempus lectus vitae ultricies.
    Vestibulum sagittis orci quis risus ultricies feugiat. Nunc feugiat velit est, at aliquam massa tristique eu.
    Aenean quis enim vel leo vestibulum volutpat in non elit. Quisque molestie tincidunt purus; ac lacinia mauris
    rhoncus in. Nullam id arcu at mauris varius viverra ut vitae massa. In ac nunc ipsum. Proin consectetur urna sit
    amet mattis vulputate. Nullam lacinia pretium tempus. Aenean quis ornare metus, tempus volutpat neque. Mauris
    volutpat scelerisque augue; at lobortis nulla rhoncus vitae. Mauris at lobortis turpis. Vivamus et ultrices lacus.
    Donec fermentum neque in eros cursus, ac tincidunt sapien consequat. Curabitur varius commodo rutrum. Nulla
    facilisi. Ut feugiat dui nec turpis sodales aliquam. Quisque auctor vestibulum condimentum. Quisque nec eros
    lorem. Curabitur et felis nec diam dictum ultrices vestibulum ac eros! Quisque eu pretium lacus. Morbi bibendum
    sagittis rutrum. Nam eget tellus quam. Nullam pharetra vestibulum justo. Donec molestie urna et scelerisque
    laoreet? Sed consectetur pretium hendrerit. Quisque erat nulla, elementum sit amet nibh vel, posuere pulvinar
    nulla. Donec elementum adipiscing dictum! Nam euismod semper nisi, eu lacinia felis placerat vel! Praesent eget
    dapibus turpis, et fringilla elit. Maecenas quis nunc cursus felis fringilla consequat! Cum sociis natoque
    penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed ullamcorper libero quis nisl sollicitudin,
    ut pulvinar arcu consectetur. Donec nisi nibh, condimentum et lectus non, accumsan imperdiet ipsum. Maecenas vitae
    massa eget lorem ornare dignissim. Nullam condimentum mauris id quam tincidunt venenatis. Aenean mattis viverra
    sem, vitae luctus velit rhoncus non. Vestibulum leo justo, rhoncus at aliquam et, iaculis sed dolor. Integer
    bibendum vitae urna in ornare! Cras accumsan nulla eu libero tempus, in dignissim augue imperdiet. Vivamus a
    lacinia odio. Curabitur id egestas eros. Integer non rutrum est. In nibh sem, tempus ac dignissim vel, ornare ac
    mi. Nulla congue scelerisque est nec commodo. Phasellus turpis lorem, sodales quis sem id, facilisis commodo
    massa. Vestibulum ultrices dolor eget purus semper euismod? Fusce id congue leo. Quisque dui magna, ullamcorper
    et leo eget, commodo facilisis ipsum. Curabitur congue vitae risus nec posuere. Phasellus tempor ligula in nisl
    pellentesque mattis. Sed nunc turpis, pharetra vel leo ac, lacinia cursus risus. Quisque congue aliquet volutpat.
    Integer dictum est quis semper tristique. Donec feugiat vestibulum tortor, id fringilla nisi lobortis eu. Nam
    hendrerit egestas sem, non mollis tortor iaculis quis. Phasellus id aliquet erat. Nunc facilisis nisi dolor,
    quis semper dui euismod vel. Cras convallis bibendum tortor malesuada tincidunt. Sed urna quam, pellentesque
    eget eleifend ac, consequat bibendum urna. Sed fringilla elit hendrerit leo blandit laoreet eget quis quam!
    Morbi eu leo a dolor aliquet dictum. Suspendisse condimentum mauris non ipsum rhoncus, sit amet hendrerit augue
    gravida. Quisque facilisis pharetra felis faucibus gravida. In arcu neque, gravida ut fermentum ut, placerat eu
    quam. Nullam aliquet lectus mauris, quis dignissim est mollis sed. Ut vestibulum laoreet eros quis cursus. Proin
    commodo eros in mollis mollis. Mauris bibendum cursus nibh, sit amet eleifend mauris luctus vitae. Sed aliquet
    pretium tristique. Morbi ultricies augue a lacinia porta. Nullam mollis erat non imperdiet imperdiet. Etiam
    tincidunt fringilla ligula, in adipiscing libero viverra eu. Nunc gravida hendrerit massa, in pellentesque nunc
    dictum id.
    """

if PY3:
    split_words = lambda f: list(set(f.lower().translate(str.maketrans("", "", punctuation)).split()))
else:
    split_words = lambda f: list(set(translate(f.lower(), maketrans(punctuation, ' ' * len(punctuation))).split()))

split_sentences = lambda f: f.split('?')
change_date = lambda: bool(random.randint(0, 1))

WORDS = split_words(FACTORY)
SENTENCES = split_sentences(FACTORY)
NUM_ITEMS = 50

def fix_image(image):
    """
    Fixes the image path.

    :param string image: Image path.
    :return string: Fixed image path.
    """
    image = os.path.join(NEWS_IMAGES_STORAGE_PATH, image.replace(settings.MEDIA_ROOT, ''))
    if image.startswith('/'):
        image = image[1:]
    return image

def _build_image_factory():
    """
    Clones the https://bitbucket.org/barseghyanartur/delusionalinsanity.images repository locally to
    grab the images. Then makes a list of all the images.

    :return list: List of relative paths to images.
    """
    try:
        subprocess.call(['rm', os.path.join(settings.MEDIA_ROOT, 'delusionalinsanity.images'), '-rf'])
    except Exception as e:
        logger.debug(e)

    try:
        subprocess.call(['hg', 'clone',
            'https://barseghyanartur@bitbucket.org/barseghyanartur/delusionalinsanity.images',
            os.path.join(settings.MEDIA_ROOT, 'delusionalinsanity.images')
            ])
        source_dir = os.path.join(settings.MEDIA_ROOT, 'delusionalinsanity.images', 'images')
        images_dir = os.path.join(settings.MEDIA_ROOT, NEWS_IMAGES_STORAGE_PATH)
        subprocess.call(['mv', source_dir, images_dir])
        images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
        return [fix_image(i) for i in images]
    except Exception as e:
        logger.debug(e)
        return []

def build_image_factory():
    """
    Downloads the https://github.com/barseghyanartur/delusionalinsanity.images/archive/latest.zip locally,
    unpacks it to grab the images. Then makes a list of all the images.

    :return list: List of relative paths to images.
    """
    try:
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'delusionalinsanity.images-latest'))
    except Exception as e:
        logger.debug(e)

    try:
        download_local = os.path.join(settings.MEDIA_ROOT, 'delusionalinsanity_images_latest.zip')
        request.urlretrieve(
            'https://github.com/barseghyanartur/delusionalinsanity.images/archive/latest.zip',
            download_local
            )

        zfile = zipfile.ZipFile(download_local)
        names = zfile.namelist()

        for name in names:
            try:
                dirname, filename = os.path.split(name)

                if not filename:
                    continue

                dirname = os.path.join(settings.MEDIA_ROOT, dirname)
                if not os.path.exists(dirname):
                    os.mkdir(dirname)

                fd = open(os.path.join(settings.MEDIA_ROOT, name), "w")
                fd.write(zfile.read(name))
                fd.close()
            except Exception as e:
                logger.debug(e)

        source_dir = os.path.join(settings.MEDIA_ROOT, 'delusionalinsanity.images-latest', 'images')
        images_dir = os.path.join(settings.MEDIA_ROOT, NEWS_IMAGES_STORAGE_PATH)
        shutil.move(source_dir, images_dir)
        images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
        return [fix_image(i) for i in images]
    except Exception as e:
        logger.debug(e)
        return []

class Command(BaseCommand):
    """
    Populating dummy news items.
    """
    def handle(self, *args, **options):
        words = WORDS[:]
        images = build_image_factory()

        if not len(images):
            images = [None for i in range(NUM_ITEMS)]

        while len(images):
            i = NewsItem()
            random_name = words[random.randint(0, len(words) - 1)]
            i.title = text_type(random_name).capitalize()
            i.slug = "{0}-{1}".format(slugify(i.title), uuid.uuid4())
            i.image = images.pop()
            i.body = text_type(SENTENCES[random.randint(0, len(SENTENCES) - 1)])
            i.date_published = radar.random_datetime()

            try:
                i.save()
                words.remove(random_name)

            except Exception as e:
                images.append(i.image)
                logger.debug(e)
