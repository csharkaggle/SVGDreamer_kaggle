from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='svgdreamer',
    version="0.1.0",
    packages=[p for p in find_packages() if p.startswith('svgdreamer') or p.startswith('ImageReward') ],
    package_data={'svgdreamer': ['py.typed']},
    install_requires=[
    ],
    python_requires=">=3.7",
    author='Ximing Xing, Juncheng Hu et al.',
    author_email='ximingxing@gmail.com',
    description='SVG Differentiable Rendering: Generating vector graphics using neural networks.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        'Artificial Intelligence',
        'AIGC',
        'Generative Models',
        'SVG Generation',
    ],
    url='https://github.com/ximinng/SVGDreamer',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)