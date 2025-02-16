from setuptools import find_packages, setup

setup(
    name="hand_control",
    version="1.2.0",
    packages=find_packages(),
    install_requires=["numpy", "opencv-python", "mediapipe"],
    entry_points={
        "console_scripts": [
            "hand_control=main:main",
        ],
    },
    author="Eric dos Santos",
    author_email="ericshantos13@gmail.com",
    description="Computer vision-based remote control",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ericshantos/hand_control",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
