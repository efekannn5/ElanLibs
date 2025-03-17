from setuptools import setup, find_packages

setup(
    name="elan",  # PyPI'de görünecek paket adı
    version="0.2.9",  # Önemli yeni özellikler eklendiği için versiyon numarasını artırıyoruz
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "opencv-python>=4.5.3",  # Görüntü işleme için OpenCV
        "requests>=2.27.1",      # İnternet üzerinden kelime havuzu indirebilmek için
        "face_recognition>=1.3.0",  # DLIB tabanlı yüz tanıma için
        "mediapipe>=0.8.9",        # Google'ın modern yüz algılama ve yüz hatları tespiti için
        "numpy>=1.20.0",          # Sayısal işlemler için
    ],
    author="Efekan Nefesoğlu",
    author_email="efekan8190nefesogeu@gmail.com",
    description="ElanLibs - Çok Yönlü Python Yardımcı Kütüphanesi",
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
