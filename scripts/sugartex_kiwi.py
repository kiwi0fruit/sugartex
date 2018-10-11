#!/usr/bin/env python
import panflute as pf
from sugartex import SugarTeX

sugartex = SugarTeX(ready=False)
# Tuning SugarTeX options:
sugartex.mjx_hack()
# sugartex.subscripts['ᵩ'] = 'ψ'  # Consolas font specific
# sugartex.superscripts['ᵠ'] = 'ψ'  # Consolas font specific
# Applying SugarTeX options:
sugartex.ready()


def action(elem, doc):
    if isinstance(elem, pf.Math):
        elem.text = sugartex.replace(elem.text)

def main(doc=None):
    return pf.run_filter(action, doc=doc)

if __name__ == '__main__':
    main()
