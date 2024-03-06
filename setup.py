from setuptools import setup

setup(
    name="gomind_screen_methods",
    python_requires=">=3.6",
    version="0.0.2",
    description="GoMind screen methods functions",
    url="https://github.com/GrupoDomini/gomind_screen_methods.git",
    author="JeffersonCarvalhoGD",
    author_email="jefferson.carvalho@grupodomini.com",
    license="unlicense",
    packages=["gomind_screen_methods"],
    zip_safe=False,
    install_requires=[
        "customtkinter==5.2.2",
        "darkdetect==0.8.0",
        "keyboard==0.13.5",
        "packaging==23.2",
        "pillow==10.2.0",
        "pynput==1.7.6",
        "six==1.16.0",
        "requests==2.31.0",
    ],
)
