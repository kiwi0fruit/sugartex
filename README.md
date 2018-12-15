# SugarTeX

SugarTeX is a more readable LaTeX language extension and transcompiler to LaTeX. Designed to be used instead of `$formula$` insertions to markdown. 

See [SugarTeX documentation](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md). Examples of input to output conversion see in [this PDF](https://github.com/kiwi0fruit/sugartex/blob/master/examples/examples.pdf?raw=true).

I use Markdown with Python code blocks for document programming via [Pandoctools](https://github.com/kiwi0fruit/pandoctools) (like R-Markdown).

Both Python and Markdown are very readable languages. Unfortunately LaTeX is not like this. So I wrote SugaTeX extension+transpiler that is highly readable. In order to achieve this it heavily uses Unicode so that SugarTeX install instructions even have recommended monospace font fallback chains. And more: [SugarTeX Completions](#sugartex-completions-for-atom) Atom package helps write all that Unicode in a moment.

I am trying to incorporate LaTeX into .md using the Markdown Philosophy of “you should write something that's readable as plain text, without compilation, also”.


## Install

Install as part of [Pandoctools](https://github.com/kiwi0fruit/pandoctools) - convenient interface and works out of the box.

Or install:

```bash
pip install sugartex
```

If you use conda package manager (Anaconda/Miniconda) then you can install dependencies first:

```bash
conda install -c defaults -c conda-forge "pip>=10.0.1" "pandoc>=2.2.1" pyyaml future shutilwhich
pip install sugartex
```

if pip install fails try to change codepage: `chcp 1252`

Also can install from GitHub:

```bash
pip install git+https://github.com/kiwi0fruit/sugartex.git
```
In this case you need to have installed [Git](https://git-scm.com/downloads) available from command prompt.


### Atom editor with full Unicode support

Highly recommended to install [Atom editor](https://atom.io/) as it's the best for markdown.

Atom is perfect for Unicode rich texts. But you need to install some fonts first. Recommended font fallback chains:

* For **Consolas**: `Consolas, 'STI0 Two Mat0 monospacified for Consola0', 'DejaVu Sans Mono monospacified for Consolas', 'Symbola monospacified for Consolas', 'Noto Sans CJK TC', monospace`. Download:
    * Consolas can be installed together with [Microsoft PowerPoint Viewer](https://www.microsoft.com/en-us/download/details.aspx?id=13) till April, 2018. SHA256: 249473568EBA7A1E4F95498ACBA594E0F42E6581ADD4DEAD70C1DFB908A09423. But note that it's license says that "You may use the software only to view and print files created with Microsoft Office software. You may not use the software for any other purpose." so you might not be even allowed to print Consolas font text via Chrome browser,
    * [STI0 Two Mat0 monospacified for Consola0](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/STI0TwoMat0_monospacified_for_Consola0.ttf?raw=true) (STIX Two Math for Consolas),
    * [DejaVu Sans Mono monospacified for Consolas](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/DejaVuSansMono_monospacified_for_Consolas.ttf?raw=true)
    * [Symbola monospacified for Consolas](https://github.com/kiwi0fruit/monospacifier/blob/d8beda67289bab66244ab0bd64f69bd4933e992c/fonts/Symbola_monospacified_for_Consolas.ttf?raw=true),
* For **Roboto Mono**: `'Open Mono', 'Noto Sans Mono', 'IBM Plex Mono', 'STI0 Two Mat0 monospacified for Robot0 Mono', 'DejaVu Sans Mono', 'Symbola monospacified for DejaVu Sans Mono', 'Noto Sans CJK TC', monospace`. Download:
    * [Open Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/OpenMono.7z?raw=true) that is simply a renamed monospacified version of Roboto Mono (italic in Roboto Mono has different width than regular),
    * [Noto Sans Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSansMono-hinted.7z?raw=true),
    * [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono). [Download](https://fonts.google.com/specimen/IBM+Plex+Mono), [Download](https://github.com/google/fonts/tree/master/ofl/ibmplexmono),
    * [STI0 Two Mat0 monospacified for Robot0 Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/STI0TwoMat0_monospacified_for_Robot0Mono.ttf?raw=true) (STIX Two Math for Roboto Mono),
    * [DejaVu Sans Mono](https://dejavu-fonts.github.io/Download.html),
    * [Symbola monospacified for DejaVu Sans Mono](https://github.com/cpitclaudel/monospacifier/blob/master/fonts/Symbola_monospacified_for_DejaVuSansMono.ttf?raw=true),

[Noto fonts](https://www.google.com/get/noto/) can also be freely downloaded (if you need CJK support). TC is Traditional Chinese but it can also be SC, JP, KR. I used monospacified fonts with the help of [monospacifier.py](https://github.com/cpitclaudel/monospacifier). If you do not like Consolas/Roboto Mono you can pick there monospacified versions for other monospace fonts.


### SugarTeX Completions for Atom

Install [SugarTeX Completions](https://atom.io/packages/sugartex-completions) package for easy typing SugarTeX and lots of other Unicode characters. (it's incompatible with [latex-completions](https://atom.io/packages/latex-completions) package).

In the [SugarTeX documentation](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md) appropriate shortcuts for SugarTeX Completions for Atom are given.


## Usage examples

Example of input to output conversion is at the end of [this PDF].

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

```sh
export PYTHONIOENCODING=utf-8

cat doc.md | \
pre-sugartex | \
pandoc -f markdown -t json | \
sugartex --kiwi | \
pandoc -f json -o doc.md.md
```

[Panflute](https://github.com/sergiocorreia/panflute) scripts are also installed so you can use it in default Panflute [automation interface in metadata](http://scorreia.com/software/panflute/guide.html#running-filters-automatically) or in it's CLI wrapper from [pandoctools](https://github.com/kiwi0fruit/pandoctools):

* `panfl sugartex/pf --to markdown`,
* `panfl sugartex/pf_kiwi -t markdown`.
