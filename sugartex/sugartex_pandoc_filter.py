import sys
import panflute as pf
from .sugartex_filter import SugarTeX

sugartex = SugarTeX(ready=False)


def kiwi_hack():
    sugartex.mjx_hack()
    # sugartex.subscripts['ᵩ'] = 'ψ'  # Consolas font specific
    # sugartex.superscripts['ᵠ'] = 'ψ'  # Consolas font specific


# noinspection PyUnusedLocal
def action(elem, doc):
    if isinstance(elem, pf.Math):
        elem.text = sugartex.replace(elem.text)


def main(doc=None):
    sugartex.ready()
    return pf.run_filter(action, doc=doc)


def cli():
    """
    Usage: sugartex [OPTIONS] [TO]

      Reads from stdin and writes to stdout. Can have single argument/option only.
      When no args or the arg is not from options then run Pandoc SugarTeX filter
      that iterates over math blocks.

    Options:
      --kiwi   Same as above but with kiwi flavor,
      --help   Show this message and exit.
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == '--kiwi':
            kiwi_hack()
        elif sys.argv[1].lower() == '--help':
            print(str(cli.__doc__).replace('\n    ', '\n'))
            return None
    main()


if __name__ == '__main__':
    cli()
