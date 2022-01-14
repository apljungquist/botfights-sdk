#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="botfights_sdk",
    version="0.0",
    install_requires=["fire", "requests"],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        "console_scripts": ["wordle = wordle.wordle:fire_main"],
        "botfights_sdk.wordle": [
            "sample = wordle.sample_bot:play",
        ],
    },
)
