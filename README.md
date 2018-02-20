# SugarTeX

SugarTeX is a more readable LaTeX language extension and transcompiler to LaTeX.

See [SugarTeX documentation](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md).


## Install

```sh
pip install sugartex
```

If you use conda package manager (Anaconda/Miniconda) then you can install dependencies first:

```sh
conda install -c defaults -c conda-forge "pandoc>=2.0,<2.1" pyyaml future shutilwhich
```

Also can install from GitHub:

```sh
pip install git+https://github.com/kiwi0fruit/sugartex.git
```
In this case you need to have installed [Git](https://git-scm.com/downloads) available from command prompt.


### Atom editor with full Unicode support

Highly recommended to install [Atom editor](https://atom.io/) as it's the best for markdown.

Atom is perfect for Unicode rich texts. But you need to install some fonts first. Recommended font fallback chains:

* For **Consolas**: `Consolas, 'TeX Gyre Schola Math monospacified for Consolas', 'Symbola monospacified for Consolas', 'Noto Sans CJK TC', monospace`. Download:
    * Consolas can be installed together with [Microsoft PowerPoint Viewer](https://www.microsoft.com/en-us/download/details.aspx?id=13) till April, 2018. SHA256: 249473568EBA7A1E4F95498ACBA594E0F42E6581ADD4DEAD70C1DFB908A09423,
    * [TeX Gyre Schola Math monospacified for Consolas](https://github.com/cpitclaudel/monospacifier/blob/master/fonts/TeXGyreScholaMath_monospacified_for_Consolas.ttf?raw=true),
    * [Symbola monospacified for Consolas](https://github.com/cpitclaudel/monospacifier/blob/master/fonts/Symbola_monospacified_for_Consolas.ttf?raw=true),
* For **Roboto Mono**: `"Roboto Mono", 'DejaVu Sans Mono', 'TeX Gyre Schola Math monospacified for DejaVu Sans Mono', 'Symbola monospacified for DejaVu Sans Mono', 'Noto Sans CJK TC', monospace`. Download:
    * [Roboto Mono](https://github.com/google/fonts/tree/master/apache/robotomono),
    * [DejaVu Sans Mono](https://dejavu-fonts.github.io/Download.html),
    * [TeX Gyre Schola Math monospacified for DejaVu Sans Mono](https://github.com/cpitclaudel/monospacifier/blob/master/fonts/TeXGyreScholaMath_monospacified_for_DejaVuSansMono.ttf?raw=true),
    * [Symbola monospacified for DejaVu Sans Mono](https://github.com/cpitclaudel/monospacifier/blob/master/fonts/Symbola_monospacified_for_DejaVuSansMono.ttf?raw=true),

[Noto fonts](https://www.google.com/get/noto/) can also be freely downloaded (if you need CJK support). TC is Traditional Chinese but it can also be SC, JP, KR. I used monospacified fonts with the help of [monospacifier.py](https://github.com/cpitclaudel/monospacifier). If you do not like Consolas/Inconsolata you can pick there monospacified versions for other monospace fonts.


### SugarTeX Completions for Atom

[Atom package](https://github.com/kiwi0fruit/sugartex-completions) for easy typing SugarTeX. At the moment it can be installed via:

```sh
apm install kiwi0fruit/sugartex-completions
```
(it's incompatible with [latex-completions](https://atom.io/packages/latex-completions) package).

In the future it would have a proper documentation and will be published as a normal Atom package.

#### TODO ↑


## Usage examples

Windows:

```bat
chcp 65001 > NUL
set PYTHONIOENCODING=utf-8

type doc.md | ^
pre-sugartex | ^
pandoc -f markdown --filter sugartex -o doc.md.md
```

Unix:

```sh
export PYTHONIOENCODING=utf-8

cat doc.md | \
pre-sugartex | \
pandoc -f markdown --filter sugartex -o doc.md.md
```

Or splitting Pandoc reader-writer:

```bat
chcp 65001 > NUL
set PYTHONIOENCODING=utf-8

type doc.md | ^
pre-sugartex | ^
pandoc -f markdown -t json | ^
sugartex --kiwi | ^
pandoc -f json -o doc.md.md
```

[Panflute](https://github.com/sergiocorreia/panflute) scripts are also installed so you can use it in default Panflute [automation interface in metadata](http://scorreia.com/software/panflute/guide.html#running-filters-automatically) or in it's CLI wrapper from [pandoctools](https://github.com/kiwi0fruit/pandoctools):

* `panfl sugartex_panfl --to markdown`,
* `panfl sugartex_kiwi -t markdown`.
