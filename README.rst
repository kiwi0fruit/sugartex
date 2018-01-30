SugarTeX
========

SugarTeX is a more readable LaTeX language extension and transcompiler
to LaTeX.

See `SugarTeX
documentation <https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md>`__.

Install
-------

.. code:: sh

    pip install sugartex

If you use conda package manager (Anaconda/Miniconda) then you can
install dependencies first:

.. code:: sh

    conda install -c defaults -c conda-forge "pandoc>=2.0,<2.1" pyyaml future shutilwhich

Also can install from GitHub:

.. code:: sh

    pip install git+https://github.com/kiwi0fruit/sugartex.git

In this case you need to have installed
`Git <https://git-scm.com/downloads>`__ available from command prompt.

Atom editor with full Unicode support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Highly recommended to install `Atom editor <https://atom.io/>`__ as it’s
the best for markdown.

Atom is perfect for Unicode rich texts. But you need to install some
fonts first. Recommended font fallback chains:

-  **Open Mono** (that is a Roboto Mono remix for SugarTeX):
   ``'Open Mono', 'Noto Sans CJK TC Thin', monospace``,

`Open Mono <https://github.com/kiwi0fruit/open-mono>`__ can be installed
from `this 7z
archive <https://github.com/kiwi0fruit/open-mono/blob/master/open_mono.7z>`__.
`Noto fonts <https://www.google.com/get/noto/>`__ can also be freely
downloaded (if you need ``'Noto Sans CJK TC Thin'``).

I used monospacified fonts with the help of
`monospacifier.py <https://github.com/cpitclaudel/monospacifier>`__. If
you do not like Roboto Mono you can pick there monospacified versions
for other monospace fonts.

SugarTeX Completions for Atom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Atom package <https://github.com/kiwi0fruit/sugartex-completions>`__
for easy typing SugarTeX. At the moment it can be installed via:

.. code:: sh

    apm install kiwi0fruit/sugartex-completions

(it’s incompatible with
`latex-completions <https://atom.io/packages/latex-completions>`__
package).

In the future it would have a proper documentation and will be published
as a normal Atom package.

TODO ↑
^^^^^^

Usage examples
--------------

Windows:

.. code:: bat

    chcp 65001 > NUL
    set PYTHONIOENCODING=utf-8

    type doc.md | ^
    pre-sugartex | ^
    pandoc -f markdown --filter sugartex -o doc.md.md

Unix:

.. code:: sh

    export PYTHONIOENCODING=utf-8

    cat doc.md | \
    pre-sugartex | \
    pandoc -f markdown --filter sugartex -o doc.md.md

Or splitting Pandoc reader-writer:

.. code:: bat

    chcp 65001 > NUL
    set PYTHONIOENCODING=utf-8

    type doc.md | ^
    pre-sugartex | ^
    pandoc -f markdown -t json | ^
    sugartex --kiwi | ^
    pandoc -f json -o doc.md.md

`Panflute <https://github.com/sergiocorreia/panflute>`__ scripts are
also installed so you can use it in default Panflute `automation
interface in
metadata <http://scorreia.com/software/panflute/guide.html#running-filters-automatically>`__
or in it’s CLI wrapper from
`pandoctools <https://github.com/kiwi0fruit/pandoctools>`__:

-  ``panfl sugartex_panfl --to markdown``,
-  ``panfl sugartex_kiwi -t markdown``.
