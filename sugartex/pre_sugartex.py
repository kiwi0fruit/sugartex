"""
CLI wrapper for sugartex_preprosess function:
(source: str) -> str
"""
import sys
import re
from .sugartex_filter import SugarTeX
import time

SESSION_ID = '§' + str(int(round(time.time() * 1000)))[-4:] + '§'


def sugartex_preprocess(source: str) -> str:
    """
    Preprocess text for SugarTeX Pandoc filter.
    Replaces 'ˎ' with `$` (except `\ˎ`), replaces `\ˎ` with `ˎ`
    """
    rep = {r'\ˎ': 'ˎ', 'ˎ': '$'}
    return re.sub(r'\\ˎ|ˎ', lambda m: rep[m.group(0)], source)


sugartex = SugarTeX(ready=False)


def sugartex_replace_all(string):
    """
    Replace all with SugarTeX.
    Runs ``sugartex_preprocess`` then iterates via regex and
    replaces each math between '$...$'.
    """
    string = sugartex_preprocess(string).replace(r'\$', SESSION_ID)
    return re.sub(
        r'(?<=\$)[^\$]*(?=\$)',
        lambda m: sugartex.replace(m.group(0)),
        string
    ).replace(SESSION_ID, r'\$')


_help = '''pre-sugartex reads from stdin and writes to stdout. Usage:
`pre-sugartex` - replace `ˎ` with `$` only,
`pre-sugartex --all` - replace everything with regexp,
`pre-sugartex --kiwi` - same as above but with kiwi flavor,
`pre-sugartex --help` or `pre-sugartex -h` - show this message.
'''


def main():
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
        if arg1 == '--all' or arg1 == '--kiwi':
            if arg1 == '--kiwi':
                sugartex.mjx_hack()
                # sugartex.subscripts['ᵩ'] = 'ψ'  # Consolas font specific
                # sugartex.superscripts['ᵠ'] = 'ψ'  # Consolas font specific
            sugartex.ready()
            sys.stdout.write(sugartex_replace_all(sys.stdin.read()))
        elif arg1 == '--help' or arg1 == '-h':
            print(_help)
        else:
            raise Exception("Invalid first argument: " + arg1)
    else:
        sys.stdout.write(sugartex_preprocess(sys.stdin.read()))


if __name__ == '__main__':
    main()
