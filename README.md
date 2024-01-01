# SRG-jutsu

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## Tools

- [Sphinx](https://www.sphinx-doc.org)
- [doc2dash](https://github.com/hynek/doc2dash)
- [Zeal](https://zealdocs.org)
- [svg2png](https://github.com/v0lt/svg2png)

Quick install:

```
scoop install python39
pip install doc2dash
scoop install make
scoop install zeal
```

Download `svg2png.exe` from https://github.com/v0lt/svg2png/releases.

## Start

```
mkdir YourDocument
cd YourDocument
python39 -m venv venv
venv\Scripts\activate.bat
pip install sphinx==4.4.0 sphinx_rtd_theme==1.1.1 sphinx_rtd_dark_mode future
sphinx-quickstart
```

After creating your document:

```
make html
doc2dash --name AbbreviationOfDocument -f ./build/html
move AbbreviationOfDocument.docset YourDocument.docset
```

If you have some `icon.svg` and you want show icon:

```
svg2png icon.svg -w 16 icon.png
svg2png icon.svg -w 32 icon@2x.png
```

Then put `.png` into `YourDocument.docset`.

Move `YourDocument.docset` to docset storage of Zeal. The path is on: Zeal > Edit > Preferences > Docset storage → Browse ... Or use `mklink`:

```sh
mklink /J ...\DocsetPathOfZeal\YourDocument.docset ...\YourDocument.docset
```

## Use it in Keypirinha

1. Install [Keypirinha](https://keypirinha.com)
2. Install [Keypirinha-Zealous](https://github.com/bantya/Keypirinha-Zealous)
3. Keypirinha → Configure Package → Zealous

```
[main]
path = "%SCOOP%\scoop\apps\zeal\current"
docset_path = "...\DocsetPathOfZeal"
results = 50
wildcard = no

[docs]
ShorterAbbreviation = AbbreviationOfDocument

# Optional

[types]
a = Attribute
c = Class
e = Exception
f = Function
g = Guide
m = Method
s = Section
v = Variable
o = Option
```

![](https://raw.githubusercontent.com/scillidan/repo_cos/main/screenshot/keypirinha-zealous_srg-jutsu.png)