from setuptools import setup, find_packages

setup(
    name="elan",  # PyPI'de görünecek paket adı
    version="0.3.1",  # Versiyon numarasını artırıyoruz
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "numpy>=1.20.0",      # Temel sayısal işlemler için 
        "requests>=2.27.1",   # İnternet üzerinden kelime havuzu indirebilmek için
    ],
    extras_require={
        # Görüntü işleme özellikleri
        'image': [
            "opencv-python>=4.5.3",    # Görüntü işleme için OpenCV
        ],
        # Yüz algılama özellikleri
        'face': [
            "opencv-python>=4.5.3",    # Görüntü işleme için OpenCV
            "dlib>=19.22.0",           # Yüz algılama için temel kütüphane
            "face_recognition>=1.3.0", # DLIB tabanlı yüz tanıma için
            "mediapipe>=0.8.9",        # Google'ın modern yüz algılama için
        ],
        # Tüm özellikler
        'all': [
            "opencv-python>=4.5.3",
            "dlib>=19.22.0", 
            "face_recognition>=1.3.0",
            "mediapipe>=0.8.9",
        ],
    },
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
