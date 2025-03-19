from setuptools import setup, find_packages

setup(
    name="elan",  # PyPI'de görünecek paket adı
    version="0.3.8",  # Büyük özellik eklendiği için versiyon numarasını artırıyoruz
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "opencv-python",  # Görüntü işleme için OpenCV
        "requests",       # İnternet üzerinden kelime havuzu indirebilmek için
    ],
    author="Efekan Nefesoğlu",
    author_email="efekan8190nefesogeu@gmail.com",
    description="ElanLibs ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/efekannn5/ElanLibs",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Turkish",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)
