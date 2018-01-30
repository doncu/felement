import glob
import pathlib
import collections

import setuptools
from pip import req


def get_recursive_files(src, dst):
    data_files = collections.defaultdict(list)
    for path in glob.glob('{}/**/*'.format(src), recursive=True):
        path_obj = pathlib.Path(path)
        if path_obj.is_file():
            new_path = (dst, ) + path_obj.parent.parts[1:]
            dirname = pathlib.Path(*new_path)
            data_files[str(dirname)].append(path)

    return tuple(data_files.items())


setuptools.setup(
    name='felement',
    version='1.0.4',
    author="Semen Dontsu, Ivan Krivosheev",
    author_email="doncusemen@gmail.com, py.krivosheev@gmail.com",
    description="Site for f-element",
    url='http://felement.ru/',
    zip_safe=False,
    python_requires='>=3.5',
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=get_recursive_files('etc', 'etc') + get_recursive_files('static', 'static'),
    install_requires=[str(ir.req) for ir in req.parse_requirements('requirements.txt', session='hack')]
)
