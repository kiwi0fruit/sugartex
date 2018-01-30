import sys
import panflute as pf
from .sugartex_filter import SugarTeX

sugartex = SugarTeX(delay=True)


def kiwi_hack():
    sugartex.mjx_hack()
    sugartex.subscripts['ᵩ'] = 'ψ'  # Consolas font specific
    sugartex.superscripts['ᵠ'] = 'ψ'  # Consolas font specific


def action(elem, doc):
    if isinstance(elem, pf.Math):
        elem.text = sugartex.replace(elem.text)


_help = '''sugartex reads from stdin and writes to stdout. Usage:
`sugartex TO` - run Pandoc filter that iterates over math blocks,
`sugartex kiwi` - same as above but with kiwi flavor,
`sugartex --help` or `sugartex -h` - show this message and exit.
'''


def main(doc=None):
    if len(sys.argv) > 1:
        if sys.argv[1] == '--kiwi':
            kiwi_hack()
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print(_help)
            return None
    sugartex.ready()
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
