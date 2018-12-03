from setuptools import setup

setup(
    name="App",
    options={
        'build_apps': {
            'gui_apps': {
                'App': 'main.py',
            },
            'platforms': [
                'manylinux1_x86_64',
                'macosx_10_6_x86_64',
                'win32',
                'win_amd64',
            ],
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ]
        }
    })
