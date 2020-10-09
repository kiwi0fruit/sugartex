# SugarTeX

SugarTeX is a more readable LaTeX language extension and transcompiler to LaTeX. Designed to be used instead of `$formula$` insertions to markdown. 

See [SugarTeX documentation](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md). Examples of input to output conversion see in [this PDF](https://github.com/kiwi0fruit/sugartex/blob/master/examples/examples.pdf?raw=true).

I use Markdown with Python code blocks for document programming via [Pandoctools](https://github.com/kiwi0fruit/pandoctools) (like R-Markdown).

Both Python and Markdown are very readable languages. Unfortunately LaTeX is not like this. So I wrote SugaTeX extension+transpiler that is highly readable. In order to achieve this it heavily uses Unicode so that SugarTeX install instructions even have recommended monospace font fallback chains. And more: [SugarTeX Completions](#sugartex-completions-for-atom) Atom package helps write all that Unicode in a moment.

I am trying to incorporate LaTeX into .md using the Markdown Philosophy of “you should write something that's readable as plain text, without compilation, also”.


## Install

Install as part of [Pandoctools](https://github.com/kiwi0fruit/pandoctools) - convenient interface and works out of the box.

Via conda:

```bash
conda install -c defaults -c conda-forge sugartex
```

Via pip:

```bash
pip install sugartex
```


### Atom editor with full Unicode support

Highly recommended to install [Atom editor](https://atom.io/) as it's the best for markdown.

Atom is perfect for Unicode rich texts. But you need to install some fonts first. See [**this instruction**](https://github.com/kiwi0fruit/open-fonts/blob/master/README.md#best-monospace) how to install recommended font fallback chains for Unicode support.


### SugarTeX Completions for Atom

Install [SugarTeX Completions](https://atom.io/packages/sugartex-completions) package for easy typing SugarTeX and lots of other Unicode characters. (it's incompatible with [latex-completions](https://atom.io/packages/latex-completions) package).

In the [SugarTeX documentation](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md) appropriate shortcuts for SugarTeX Completions for Atom are given.


### SugarTeX to docx conversion with free software only

[Math support in pandoc](https://github.com/kiwi0fruit/open-fonts/blob/master/language_variants_and_math_support.md#pandoc).


## Usage examples

Example of input to output conversion is at the end of [this PDF].

Windows:

```bat
@echo off
chcp 65001 > NUL
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

type doc.md | ^
pre-sugartex | ^
pandoc -f markdown --filter sugartex -o doc.md.md
```

Unix (`convert` bash script to use like `./convert doc.md`):

```bash
#!/bin/bash
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1

cat "$@" | \
pre-sugartex | \
pandoc -f markdown --filter sugartex -o "$@.md"
```
(or `pandoc -f markdown --filter sugartex --to docx+styles -o "$@.docx"`)

Or splitting Pandoc reader-writer:

```sh
export PYTHONIOENCODING=utf-8

cat doc.md | \
pre-sugartex | \
pandoc -f markdown -t json | \
sugartex --kiwi | \
pandoc -f json -o doc.md.md
```

[Panflute](https://github.com/sergiocorreia/panflute) scripts are also installed so you can use it in default Panflute [automation interface in metadata](http://scorreia.com/software/panflute/guide.html#running-filters-automatically) or in recommend [panfl](https://github.com/kiwi0fruit/pandoctools/blob/master/docs/panfl.md) CLI:

* `panfl sugartex --to markdown`,
* `panfl sugartex.kiwi -t markdown`.
