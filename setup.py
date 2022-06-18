try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

with open(".\\requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="selenium_utils",
    version=1.0,
    author="Max",
    description="Better functionality for selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],

    include_package_data=True,
    data_files=[
        ("audio", [
            "audio_processing/ffmpeg.exe",
            "audio_processing/ffplay.exe",
            "audio_processing/ffprobe.exe",
            ]),
    ],

    python_requires='>2.7, <4',
    install_requires=requirements,
)
