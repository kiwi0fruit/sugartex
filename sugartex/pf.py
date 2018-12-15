#!/usr/bin/env python
import sys
import panflute as pf
from sugartex import SugarTeX

sugartex = SugarTeX()


def action(elem, doc):
    if isinstance(elem, pf.Math):
        elem.text = sugartex.replace(elem.text)


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
