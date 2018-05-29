import re
import copy
from collections import OrderedDict
from typing import Type, Callable
from itertools import chain


# SugarTeX language extension:
# ----------------------------
# Superscripts and subscripts:
#     all are escapable
# ₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓᵦᵧᵨᵩᵪ₊₋₌₍₎
_subscripts = {
    '₀': '0',
    '₁': '1',
    '₂': '2',
    '₃': '3',
    '₄': '4',
    '₅': '5',
    '₆': '6',
    '₇': '7',
    '₈': '8',
    '₉': '9',
    'ₐ': 'a',  # no b c d
    'ₑ': 'e',  # no f g
    'ₕ': 'h',
    'ᵢ': 'i',
    'ⱼ': 'j',
    'ₖ': 'k',
    'ₗ': 'l',
    'ₘ': 'm',
    'ₙ': 'n',
    'ₒ': 'o',
    'ₚ': 'p',  # no q
    'ᵣ': 'r',
    'ₛ': 's',
    'ₜ': 't',
    'ᵤ': 'u',
    'ᵥ': 'v',  # no w
    'ₓ': 'x',  # no y z
    'ᵦ': 'β',
    'ᵧ': 'γ',
    'ᵨ': 'ρ',
    # 'ᵩ': 'ψ',  # problems in consolas font ψ<>φ, ᵠ<>ᶲ, ᵩ<>φ
    'ᵪ': 'χ',
    '₊': '+',
    '₋': '-',
    '₌': '=',
    '₍': '(',
    '₎': ')',
}
#     all are escapable
# ⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᵅᵝᵞᵟᵋᶿᶥᶲᵠᵡ⁺⁻⁼⁽⁾ᴬᴮᴰᴱᴳᴴᴵᶦᴶᴷᴸᶫᴹᴺᶰᴼᴾᴿᵀᵁᶸⱽᵂ
_superscripts = {
    '⁰': '0',
    '¹': '1',
    '²': '2',
    '³': '3',
    '⁴': '4',
    '⁵': '5',
    '⁶': '6',
    '⁷': '7',
    '⁸': '8',
    '⁹': '9',
    'ᵃ': 'a',
    'ᵇ': 'b',
    'ᶜ': 'c',
    'ᵈ': 'd',
    'ᵉ': 'e',
    'ᶠ': 'f',
    'ᵍ': 'g',
    'ʰ': 'h',
    'ⁱ': 'i',
    'ʲ': 'j',
    'ᵏ': 'k',
    'ˡ': 'l',
    'ᵐ': 'm',
    'ⁿ': 'n',
    'ᵒ': 'o',
    'ᵖ': 'p',  # no q
    'ʳ': 'r',
    'ˢ': 's',
    'ᵗ': 't',
    'ᵘ': 'u',
    'ᵛ': 'v',
    'ʷ': 'w',
    'ˣ': 'x',
    'ʸ': 'y',
    'ᶻ': 'z',
    'ᵅ': 'α',
    'ᵝ': 'β',
    'ᵞ': 'γ',
    'ᵟ': 'δ',
    'ᵋ': 'ε',
    'ᶿ': 'θ',
    'ᶥ': 'ι',
    'ᶲ': 'φ',
    # 'ᵠ': 'ψ',  # problems in consolas font ψ<>φ, ᵠ<>ᶲ, ᵩ<>φ
    'ᵡ': 'χ',
    '⁺': '+',
    '⁻': '-',
    '⁼': '=',
    '⁽': '(',
    '⁾': ')',
    'ᴬ': 'A',
    'ᴮ': 'B',  # no C
    'ᴰ': 'D',
    'ᴱ': 'E',  # no F
    'ᴳ': 'G',
    'ᴴ': 'H',
    'ᴵ': 'I',
    'ᶦ': 'I',
    'ᴶ': 'J',
    'ᴷ': 'K',
    'ᴸ': 'L',
    'ᶫ': 'L',
    'ᴹ': 'M',
    'ᴺ': 'N',
    'ᶰ': 'N',
    'ᴼ': 'O',
    'ᴾ': 'P',  # no Q
    'ᴿ': 'R',  # no S
    'ᵀ': 'T',
    'ᵁ': 'U',
    'ᶸ': 'U',
    'ⱽ': 'V',
    'ᵂ': 'W',  # no X Y Z
}

_brackets = [
    (('[', r'['), (']', r']')),
    (('(', r'('), (')', r')')),
    (('{', r'\{'), ('}', r'\}')),
    (('│', r'\vert'), ('│', r'\vert')),  # for math in markdown tables
    (('|', r'\vert'), ('|', r'\vert')),
    (('‖', r'\Vert'), ('‖', r'\Vert')),
    (('˱', r'.'), ('˲', r'.')),
    (('⟨', r'\langle'), ('⟩', r'\rangle')),
    (('⌊', r'\lfloor'), ('⌋', r'\rfloor')),
    (('⌈', r'\lceil'), ('⌉', r'\rceil')),
]
_brackets_types = [
    (('˳˳{}', r'\bigl{} '), ('{}˳˳', r'\bigr{}')),
    (('˳ˌ{}', r'\Bigl{} '), ('{}˳ˌ', r'\Bigr{}')),
    (('ˌ˳{}', r'\biggl{} '), ('{}ˌ˳', r'\biggr{}')),
    (('ˌˌ{}', r'\Biggl{} '), ('{}ˌˌ', r'\Biggr{}')),
    (('˳{}', r'\left{}{{'), ('{}˳', r'}}\right{}'))
]  # ˳ alt+L + mlori, ˌ alt+L + molo vline

# language=PythonRegExp
_default_pref = r'^|(?<=\n)|(?<=^[ ˱{])|(?<=[^\\][ ˱{])'   # language=PythonRegExp
_default_postf = r'$|(?=\n)|(?<!\\)(?=[ ˲\}])'


def _ops_regex(ops_) -> str:
    """ops is a iterable of str"""
    ops = list(ops_)
    singles = re.escape(''.join(op for op in ops if len(op) == 1))  # language=PythonRegExp
    singles = [r'[{}]'.format(singles)] if (singles != '') else []
    longs = [op for op in ops if len(op) > 1]
    longs.sort(key=lambda s: -len(s))
    longs = [re.escape(op) for op in longs]  # language=PythonRegExp
    return '|'.join(longs + singles)


def _search_regex(ops: dict, regex_pat: str):
    """
    Search order:
      * specified regexps
      * operators sorted from longer to shorter
    """
    custom_regexps = list(filter(None, [dic['regex'] for op, dic in ops.items() if 'regex' in dic]))
    op_names = [op for op, dic in ops.items() if 'regex' not in dic]
    regex = [regex_pat.format(_ops_regex(op_names))] if len(op_names) > 0 else []  # language=PythonRegExp
    return re.compile('|'.join(custom_regexps + regex))


class Styles:
    """Math styles with brackets (prefix unary operators)"""
    # language=PythonRegExp
    regex_pat = r'(?<!\\)({}(?:{}))'  # should have only one slot inside it's own group
    # language=PythonRegExp
    postf_pat = r'(?:(?<![\\{1}]){0}|(?<!\\)([{1}]){0})|(?<=\\[{1}]){0}'

    def postf(self, close_br: str, postf_un_ops: str) -> str:
        return self.postf_pat.format(re.escape(close_br), postf_un_ops)

    @staticmethod
    def pat(pat: str):  # has 2 slots: text, postf_un_op
        return lambda t: ('{{' + pat + '{}}}').format(t[0], t[1] if (t[1] is not None) else '')

    brackets = [('{', '}'), ('[', ']'), ('(', ')')]

    styles = OrderedDict([  # should have only one slot
        ('^{r}', r'\mathrm{{{}}}'),  # regular
        ('^{i}', r'\mathit{{{}}}'),  # italic
        ('^{b}', r'\mathbf{{{}}}'),  # bold
        (' ⃗', r'\mathbf{{{}}}'),  # vector bold notation
        ('⃗', r'\mathbf{{{}}}'),  # vector bold notation
        ('⠃', r'\mathbf{{{}}}'),  # vector bold notation
        ('⠘', r'\mathbf{{{}}}'),  # vector bold notation
        ('⠛', r'\mathbf{{{}}}'),  # matrix bold notation
        ('⠋', r'\mathbf{{{}}}'),  # matrix bold notation
        ('^{β}', r'\boldsymbol{{{}}}'),  # bold italic
        ('^{m}', r'\mathtt{{{}}}'),  # monospace
        ('^{c}', r'\mathcal{{{}}}'),  # calligraphic # no cyrillic support (see Monotype Corsiva)
        ('^{t}', r'\text{{{}}}'),
        ('^{ti}', r'\textit{{{}}}'),
        ('^{tb}', r'\textbf{{{}}}'),
        ('^{tβ}', r'\textit{{\textbf{{{}}}}}'),
    ])
    mjx_bi = r'\class{{MJX-BoldItalic}}{{\mathbf{{{}}}}}'  # mathjax hack
    mjx_m = r'\class{{MJX-Monospace}}{{\mathtt{{{}}}}}'  # mathjax hack
    mpl_bi = r'\mathsf{{{}}}'  # matplotlib hack
    styles_bak = copy.deepcopy(styles)

    def spec(self, postf_un_ops: str) -> list:
        """Return prefix unary operators list"""
        spec = [(l + op, {'pat': self.pat(pat),
                          'postf': self.postf(r, postf_un_ops),
                          'regex': None})
                for op, pat in self.styles.items()
                for l, r in self.brackets]
        spec[0][1]['regex'] = self.regex_pat.format(
            _ops_regex(l for l, r in self.brackets),
            _ops_regex(self.styles.keys())
        )
        return spec


class PrefUnGreedy:
    """
    Greedy prefix unary operators like `{⋲` or `˱⋲`:
    ˎ\sign(x) = {⋲  1 if x>0 ¦ 0 if x=0 ¦ -1 if x<0}ˎ
    """
    # language=PythonRegExp
    postf = r'(?<!\\)[˲\}]'  # language=PythonRegExp1
    regex_pat = r'(?<!\\)([˱{{](?:{}))'  # should have only one slot inside it's own group
    ops = OrderedDict([  # should have only one slot
        ('⋲', r'\begin{{cases}}{}\end{{cases}}'),
    ])

    def spec(self) -> list:
        """Returns prefix unary operators list.
        Sets only one regex for all items in the dict."""
        spec = [item
                for op, pat in self.ops.items()
                for item in [('{' + op, {'pat': pat, 'postf': self.postf, 'regex': None}),
                             ('˱' + op, {'pat': pat, 'postf': self.postf, 'regex': None})]
                ]
        spec[0][1]['regex'] = self.regex_pat.format(_ops_regex(self.ops.keys()))
        return spec


class OtherStyles:
    """
    Other styles (prefix unary operators)
    ops = {
        captured regex group: {
            'pat': .format() pattern OR func -> str,
            'postf': postfix regex string
            'regex': str or None  # optional
                # if not provided - it will be made from operator key
                # if None - it will be ignored completely (useful when you specify only one regex)
        }
    }
    'pat' should have only one slot
    """
    postf_pat = Styles.postf_pat
    postf = Styles.postf
    pat = staticmethod(Styles.pat)  # language=PythonRegExp
    regex_pat = r'(?<!\\)({})'  # should have only one slot inside it's own group
    styles = OrderedDict([
        ('‹^{β}', {'pat': r'\textit{{\textbf{{{}}}}}', 'postf': '›'}),  # text bold-italic
        ('‹^{i}', {'pat': r'\textit{{{}}}', 'postf': '›'}),  # text italic
        ('‹^{b}', {'pat': r'\textbf{{{}}}', 'postf': '›'}),  # text bold
        ('‹',  {'pat': r'\text{{{}}}', 'postf': '›'}),  # text regular
        ('˹', {'pat': r'\mathrm{{{}}}', 'postf': '˺'}),  # math regular
    ])
    mjx_tbi = r'\class{{MJX-TextBoldItalic}}{{\textbf{{{}}}}}'  # mathjax hack
    styles_bak = copy.deepcopy(styles)

    def spec(self, postf_un_ops: str) -> list:
        spec = [(op, {'pat': self.pat(dic['pat']),
                      'postf': self.postf(dic['postf'], postf_un_ops),
                      'regex': None})
                for op, dic in self.styles.items()]
        spec[0][1]['regex'] = self.regex_pat.format(_ops_regex(self.styles.keys()))
        return spec


class PrefUnOps:
    """
    Prefix unary operators.
    ops = {
        captured regex group: {
            'pat': .format() pattern OR func -> str,
            'postf': postfix regex string  # optional
            'regex': str or None  # optional
                # if not provided - it will be made from operator key
                # if None - it will be ignored completely (useful when you specify only one regex)
        }
    }
    'pat' should have only one slot
    """
    postf = _default_postf  # language=PythonRegExp
    regex_pat = r'(?<!\\)({}) *'  # should have only one slot inside it's own group
    ops = OrderedDict([
        # math styles will be inserted here,
        # other styles will be inserted here,
        # greedy unary prefix operators will be inserted here,
        ('⧼', {'pat': r'\begin{{{}}}'}),
        ('👻', {'pat': r'\vphantom{{{}}}'}),
        ('→⎴', {'pat': r'\xrightarrow{{{}}}'}),
        ('←⎴', {'pat': r'\xleftarrow{{{}}}'}),
        # ('ˏ', {'pat': r'\mathrm{{{}}}',  # language=PythonRegExp
        #        'postf': r'ˏ|$|(?=\n)|(?<!\\)(?=[\\ ˲\}])'})  # regular math style
    ])
    regex = None

    def __init__(self):
        self.styles = Styles()
        self.other_styles = OtherStyles()
        self.pref_un_greedy = PrefUnGreedy()  # Unary prefix operators without brackets

    def fill(self, postf_un_ops: str):
        """
        Insert:
          * math styles
          * other styles
          * unary prefix operators without brackets
          * defaults
        """
        for op, dic in self.ops.items():
            if 'postf' not in dic:
                dic['postf'] = self.postf
        self.ops = OrderedDict(
            self.styles.spec(postf_un_ops) +
            self.other_styles.spec(postf_un_ops) +
            self.pref_un_greedy.spec() +
            list(self.ops.items())
        )
        for op, dic in self.ops.items():
            dic['postf'] = re.compile(dic['postf'])
        self.regex = _search_regex(self.ops, self.regex_pat)


class PostfUnOps:
    """
    Postfix unary operators.
    ops = {
        captured regex group: {
            'pat': .format() pattern OR func -> str,
            'pref': prefix regex string,  # optional
            'regex': str or None  # optional
                # if not provided - it will be made from operator key
                # if None - it will be ignored completely (useful when you specify only one regex)
        }
    }
    'pat' should have only one slot
    """
    pref = _default_pref  # language=PythonRegExp
    regex_pat = r'(?<!\\) *({})'  # should have only one slot inside it's own group
    ops = OrderedDict([
        ('⃗', {'pat': r'\vec{{{}}}'}),
        ('⃑', {'pat': r'\overrightarrow{{{}}}'}),  # \^-->
        ('^', {'pat': r'\widehat{{{}}}',  # language=PythonRegExp
               'regex': r'(?<!\\) *(\^)(?=[˲\}]|\r?\n|$)'}),
        ('ˆ', {'pat': r'\hat{{{}}}'}),
        ('¯', {'pat': r'\bar{{{}}}'}),
        ('‾', {'pat': r'\overline{{{}}}'}),
        ('˙', {'pat': r'\dot{{{}}}'}),
        ('¨', {'pat': r'\ddot{{{}}}'}),
        ('⏞', {'pat': r'\overbrace{{{}}}'}),
        ('⏟', {'pat': r'\underbrace{{{}}}'}),
        ('ˍ', {'pat': r'\underline{{{}}}',  # language=PythonRegExp
               'regex': r'(?<!\\) *(ˍ)(?=[˲\}]|\r?\n|$)'}),
        ('⧽', {'pat': r'\end{{{}}}'}),
    ])
    regex = None

    def fill(self):
        for op, dic in self.ops.items():
            if 'pref' not in dic:
                dic['pref'] = self.pref
        for op, dic in self.ops.items():
            dic['pref'] = re.compile(dic['pref'])
        self.regex = _search_regex(self.ops, self.regex_pat)

    def one_symbol_ops_str(self) -> str:
        """Regex-escaped string with all one-symbol operators"""
        return re.escape(''.join((key for key in self.ops.keys() if len(key) == 1)))


class Matrices:
    """Matrix operators (and fractions without bar) (center binary operators)"""
    # language=PythonRegExp
    pref = r'(?<!\\)([{˱])([(\[│|‖]?)'  # language=PythonRegExp
    postf = r'(?<!\\)([)\]│|‖]?)([˲\}])'
    mat_dic = {
        '(': 'p', ')': 'p',
        '[': 'b', ']': 'b',
        '{': 'B', '}': 'B',
        '│': 'v', '|': 'v',  # for math in markdown tables
        '‖': 'V',
        '˱': '', '˲': '',
    }
    mat_ops = ['¦⠋']
    mat_pat = r'\begin{{{}matrix}}{}¦{}\end{{{}matrix}}'

    frac_dic = {
        '(': '(', ')': ')',
        '[': '[', ']': ']',
        '{': r'\{', '}': r'\}',
        '│': '|', '|': '|',
        '‖': r'\Vert',
        '˱': '', '˲': '',
    }
    frac_ops = ['¦⠘', '¦⠃']  # ⠘ br45 (right upper 2), ⠃ br12 (left upper 2)
    frac_styles = OrderedDict([('^{d}', '0'), ('^{t}', '1'), ('^{xs}', '3'), ('^{s}', '2'), ('', '')])
    frac_pat = r'\genfrac{{{0}}}{{{3}}}{{0pt}}{{<>}}{{{1}}}{{{2}}}'

    @staticmethod
    def pat(pat: str, dic: dict):  # has 4 slots: left bracket id, term1, term2, right bracket id
        return lambda t: pat.format(dic[t[1] if t[1] != '' else t[0]], t[2], t[3], dic[t[4] if t[4] != '' else t[5]])

    def spec(self) -> list:
        frac_spec = [(op + style, {'pat': self.pat(self.frac_pat.replace('<>', self.frac_styles[style]),
                                                   self.frac_dic),
                                   'pref': self.pref, 'postf': self.postf})
                     for op in self.frac_ops
                     for style in self.frac_styles.keys()]
        mat_spec = [(op, {'pat': self.pat(self.mat_pat, self.mat_dic),
                          'pref': self.pref, 'postf': self.postf})
                    for op in self.mat_ops]
        return mat_spec + frac_spec


class BinCentrGreedy:
    """
    Greedy center binary operators like `¦#`:
    ˎsign(x) = ˳{˱1 if x>0 ¦# 0 if x=0 ¦ -1 if x<0˲˲˳ˎ
    """
    # language=PythonRegExp
    pref = r'(?<!\\)[˱{]'  # language=PythonRegExp
    postf = r'(?<!\\)[˲\}]'
    ops = OrderedDict([  # should have only one slot
        ('¦⠛^{t}', r'\begin{{smallmatrix}}{}¦{}\end{{smallmatrix}}'),
        ('¦⠛', r'\begin{{array}}{}¦{}\end{{array}}'),
        ('¦#', r'\begin{{aligned}}{}¦{}\end{{aligned}}'),
        ('¦˽^{l}', r'{{\begin{{subarray}}{{l}}{}¦{}\end{{subarray}}}}'),
        ('¦⎵^{l}', r'{{\begin{{subarray}}{{l}}{}¦{}\end{{subarray}}}}'),
        ('¦˽^{c}', r'{{\begin{{subarray}}{{c}}{}¦{}\end{{subarray}}}}'),
        ('¦⎵^{c}', r'{{\begin{{subarray}}{{c}}{}¦{}\end{{subarray}}}}'),
        ('¦˽^{r}', r'{{\begin{{subarray}}{{r}}{}¦{}\end{{subarray}}}}'),
        ('¦⎵^{r}', r'{{\begin{{subarray}}{{r}}{}¦{}\end{{subarray}}}}'),
        ('¦˽', r'{{\substack{{{}¦{}}}}}'),
        ('¦⎵', r'{{\substack{{{}¦{}}}}}'),
    ])

    def spec(self) -> list:
        spec = [(op, {'pat': pat, 'pref': self.pref, 'postf': self.postf})
                for op, pat in self.ops.items()]
        return spec


class BinCentrOps:
    """
    Center binary operators.
    ops = {
        captured center group: {
            'pat': .format() pattern OR lambda func -> str,
            'pre': prefix regex string,  # optional
            'post': postfix regex string  # optional
            'regex': str or None  # optional
                # if not provided - it will be made from operator key
                # if None - it will be ignored completely (useful when you specify only one regex)
        }
    }
    """
    pref = _default_pref
    postf = _default_postf  # language=PythonRegExp
    regex_pat = r'(?<!\\) *({}) *'  # language=PythonRegExp

    _choose_pref = r'(?<!\\)\('  # language=PythonRegExp
    _choose_postf = r'(?<!\\)\)'  # language=PythonRegExp
    _sfrac_pref = r'(?:^|(?<=\n)|(?<=^[ ˱{])|(?<=[^\\][ ˱{]))(?:[˱{]([^˱˲{\}]*[^\\˱˲{\}])[˲\}])?'
    ops = OrderedDict([
        ('∕^{d}', {'pat': r'\dfrac{{{}}}{{{}}}'}),  # a∕ᵈb
        ('∕^{t}', {'pat': r'\tfrac{{{}}}{{{}}}'}),
        ('∕^{c}', {'pat': r'\cfrac{{{}}}{{{}}}'}),
        ('∕^{xs}', {'pat': lambda t: r'\genfrac{{}}{{}}{{{}}}{{3}}{{{}}}{{{}}}'.format(
                           t[0] if (t[0] is not None) else '', t[1], t[2]), 'pref': _sfrac_pref}),
        ('∕^{s}', {'pat': lambda t: r'\genfrac{{}}{{}}{{{}}}{{2}}{{{}}}{{{}}}'.format(
                          t[0] if (t[0] is not None) else '', t[1], t[2]), 'pref': _sfrac_pref}),
        ('∕', {'pat': r'\frac{{{}}}{{{}}}'}),
        ('√', {'pat': r'\sqrt[{}]{{{}}}',  # language=PythonRegExp
               'regex': r'(?<!\\)(√) *'}),  # can have superscript arguments (no `\` escapes!)
        ('⎴', {'pat': r'\overset{{{1}}}{{{0}}}'}),
        ('˽', {'pat': r'\underset{{{1}}}{{{0}}}'}),
        ('⎵', {'pat': r'\underset{{{1}}}{{{0}}}'}),
        ('¦^{c}', {'pat': r'\binom{{{}}}{{{}}}', 'pref': _choose_pref, 'postf': _choose_postf}),
        ('¦^{ct}', {'pat': r'\tbinom{{{}}}{{{}}}', 'pref': _choose_pref, 'postf': _choose_postf}),  # (n¦ᶜᵗm)
        ('¦^{cd}', {'pat': r'\dbinom{{{}}}{{{}}}', 'pref': _choose_pref, 'postf': _choose_postf}),
    ])
    regex = None

    def __init__(self):
        self.matrices = Matrices()
        self.bin_centr_greedy = BinCentrGreedy()

    def fill(self):
        for op, dic in self.ops.items():
            if 'pref' not in dic:
                dic['pref'] = self.pref
            if 'postf' not in dic:
                dic['postf'] = self.postf
        self.ops = OrderedDict(
            self.matrices.spec() +
            self.bin_centr_greedy.spec() +
            list(self.ops.items())
        )
        for op, dic in self.ops.items():
            dic['pref'] = re.compile(dic['pref'])
            dic['postf'] = re.compile(dic['postf'])
        self.regex = _search_regex(self.ops, self.regex_pat)


class NullOps:
    """Nullary operators"""
    big_ops = OrderedDict([
        ('∑', r'\sum'),
        ('∏', r'\prod'),
        ('∫', r'\int'),
        ('∬', r'\iint'),
        ('∭', r'\iiint'),
        ('⨌', r'\iiiint'),
        ('∮', r'\oint'),
    ])
    big_limits = OrderedDict([
        ('⢈', r'\limits'),  # ⢈ br pat 48
        ('⡁', r'\limits'),  # ⡁ br pat 17
        (':', r'\nolimits'),
        ('⠆', r'\nolimits'),  # ⠆ br pat 23
        ('⠰', r'\nolimits'),  # ⠰ br pat 56
        ('', ''),
    ])  # language=PythonRegExp
    big_regex_pat = r'(?<!\\)({})((?:{})?)'

    @staticmethod
    def big_pat(pat: str, dic):  # has 2 slots: big op id, optional limits display mode
        return lambda t: '{}{}'.format(pat, dic[t[0]])  # language=PythonRegExp

    regex_pat = r'(?<!\\)({})'

    ops = OrderedDict([
        # (':^{d}', {'pat': r'\displaystyle',  # language=PythonRegExp
        #            'regex': r'(?:(?<=^[˱{])|(?<=[^\\][˱{]))(:\^{[dt]\})'}),
        # (':^{t}', {'pat': r'\textstyle', 'regex': None}),  # examples
    ])
    regex = None

    def fill(self):
        big_spec = [(op, {'pat': self.big_pat(self.big_ops[op], self.big_limits), 'regex': None})
                    for op in self.big_ops.keys()]
        big_spec[0][1]['regex'] = self.big_regex_pat.format(_ops_regex(self.big_ops.keys()),
                                                            _ops_regex(self.big_limits.keys()))
        self.ops = OrderedDict(
            big_spec +
            list(self.ops.items())
        )
        self.regex = _search_regex(self.ops, self.regex_pat)


class SugarTeX:
    """
    Define LaTeX syntax extension.

    IMPORTANT: groups in operators regexps should be unnamed and their order in the:
    1) center binary operators:
       pref.match.groups() + [term1] + (regex.match.groups()≠None)[1:] +
       [term2] + postf.match.groups()
    2) prefix unary operators:
       (regex.match.groups()≠None)[1:] + [term] + postf.match.groups()
    3) postfix unary operators:
       pref.match.groups() + [term] + (regex.match.groups()≠None)[1:]

    is the same as the order in the .format() pattern. Otherwise specify
    function (-> str) instead of .format() pattern (it's argument would
    be the tuple mentioned).
    """
    max_iter = 10
    max_while = 1000
    # all brackets and simple replacements are applied via one big regex (OR `|` joined)
    # so they cannot be stacked
    brackets = _brackets
    brackets_types = _brackets_types
    simple_pre = OrderedDict([  # Order should not matter!
        ('∛', ' 3√'),
        ('∜', ' 4√'),
        (' ', r'\,'),  # thin space
    ])
    superscripts = _superscripts
    subscripts = _subscripts
    regex_pre = []

    # language=PythonRegExp
    loop_regexps = []  # = [[regex string, replace],]

    regex_post = []
    simple_post = OrderedDict([  # Order should not matter!
        ('¦', '\\\\'),  # IMPORTANT: this should be after other `¦` replacements
        ('˳', '&'),  # IMPORTANT: this should be after brackets and other `˳` replacements
        ('˱', '{'),
        ('˲', '}'),
        ('ˍ', '_'),
        ('`', '\\'),
        ('ˋ', '\\'),  # modifier letter grave accent
        ('↕^{d}', r'\displaystyle'),
        ('↕^{t}', r'\textstyle'),
        ('↕^{s}', r'\scriptstyle'),
        ('↕^{xs}', r'\scriptscriptstyle'),
    ])

    # Escapes:
    # ------------------------------
    escapes = ['⋲', '›', '˺', '↕', 'ˌ']
    escapes_regex = None  # it's assigned later

    def __init__(self, delay: bool=False):
        self.pref_un_ops = PrefUnOps()
        self.postf_un_ops = PostfUnOps()
        self.bin_centr_ops = BinCentrOps()
        self.null_ops = NullOps()
        if not delay:
            self.ready()

    def ready(self):
        self.bin_centr_ops.fill()
        self.postf_un_ops.fill()
        styles_postf = self.postf_un_ops.one_symbol_ops_str()
        self.pref_un_ops.fill(styles_postf)
        self.null_ops.fill()
        # Brackets + simple pre replacements:
        self.simple_pre = OrderedDict(self._brackets_to_list() + list(self.simple_pre.items()))
        # Superscripts and subscripts + pre regexps:
        self.regex_pre = [self._su_scripts_regex()] + self.regex_pre
        # Escape characters:
        self.escapes += [s for s in chain(self.pref_un_ops.ops.keys(),
                                          self.postf_un_ops.ops.keys(),
                                          self.bin_centr_ops.ops.keys(),
                                          self.null_ops.ops.keys(),
                                          self.simple_pre.keys(),
                                          self.simple_post.keys()) if len(s) == 1]
        self.escapes = OrderedDict((s, None) for s in self.escapes).keys()
        self.escapes_regex = re.compile(r'\\({})'.format(_ops_regex(self.escapes)))

    @staticmethod
    def _dict_replace(dic: dict or Type[OrderedDict], source: str) -> str:
        if len(dic) > 0 and source != '':
            rep = {re.escape(key): val for key, val in dic.items()}  # language=PythonRegExp
            regex = re.compile(r'(?<!\\)(?:{})'.format("|".join(rep.keys())))
            return regex.sub(lambda m: rep[re.escape(m.group(0))], source)
        else:
            return source

    def _su_scripts_regex(self):
        """
        :return:
            [compiled regex, function]
        """
        sups = re.escape(''.join([k for k in self.superscripts.keys()]))
        subs = re.escape(''.join([k for k in self.subscripts.keys()]))  # language=PythonRegExp
        su_regex = (r'\\([{su_}])|([{sub}]+|‹[{sub}]+›|˹[{sub}]+˺)' +
                    r'|([{sup}]+)(?=√)|([{sup}]+(?!√)|‹[{sup}]+›|˹[{sup}]+˺)').format(
            su_=subs + sups, sub=subs, sup=sups)
        su_regex = re.compile(su_regex)

        def su_replace(m):
            esc, sub, root_sup, sup = m.groups()
            if esc is not None:
                return esc
            elif sub is not None:
                return '_{' + ''.join([c if (c in ['‹', '›', '˹', '˺']) else self.subscripts[c] for c in sub]) + '}'
            elif root_sup is not None:
                return ''.join([self.superscripts[c] for c in root_sup])
            elif sup is not None:
                return '^{' + ''.join([c if (c in ['‹', '›', '˹', '˺']) else self.superscripts[c] for c in sup]) + '}'
            else:
                raise TypeError("Regex bug: this should never be reached")

        return [su_regex, su_replace]

    def _brackets_to_list(self) -> list:
        return [
            (key, val)
            for lpat, rpat in self.brackets_types
            for l, r in self.brackets
            for key, val in ((lpat[0].format(l[0]), lpat[1].format(l[1])),
                             (rpat[0].format(r[0]), rpat[1].format(r[1])))
        ]

    @staticmethod
    def _local_map(match, loc: str = 'lr') -> list:
        """
        :param match:
        :param loc: str
            "l" or "r" or "lr"
            turns on/off left/right local area calculation
        :return: list
            list of the same size as the string + 2
            it's the local map that counted { and }
            list can contain: None or int>=0
            from the left of the operator match:
                in `b}a` if a:0 then }:0 and b:1
                in `b{a` if a:0 then {:0 and b:-1(None)
            from the right of the operator match:
                in `a{b` if a:0 then {:0 and b:1
                in `a}b` if a:0 then }:0 and b:-1(None)
            Map for +1 (needed for r'$') and -1 (needed for r'^')
            characters is also stored: +1 -> +1, -1 -> +2
        """
        s = match.string
        map_ = [None] * (len(s) + 2)
        if loc == 'l' or loc == 'lr':
            balance = 0
            for i in reversed(range(0, match.start())):
                map_[i] = balance
                c, prev = s[i], (s[i - 1] if i > 0 else '')
                if (c == '}' or c == '˲') and prev != '\\':
                    balance += 1
                elif (c == '{' or c == '˱') and prev != '\\':
                    balance -= 1
                if balance < 0:
                    break
            map_[-1] = balance
        if loc == 'r' or loc == 'lr':
            balance = 0
            for i in range(match.end(), len(s)):
                map_[i] = balance
                c, prev = s[i], s[i - 1]
                if (c == '{' or c == '˱') and prev != '\\':
                    balance += 1
                elif (c == '}' or c == '˲') and prev != '\\':
                    balance -= 1
                if balance < 0:
                    break
            map_[len(s)] = balance
        return map_

    def _operators_replace(self, string: str) -> str:
        """
        Searches for first unary or binary operator (via self.op_regex
        that has only one group that contain operator)
        then replaces it (or escapes it if brackets do not match).
        Everything until:
          * space ' '
          * begin/end of the string
          * bracket from outer scope (like '{a/b}': term1=a term2=b)
        is considered a term (contents of matching brackets '{}' are
        ignored).

        Attributes
        ----------
        string: str
            string to replace
        """
        # noinspection PyShadowingNames
        def replace(string: str, start: int, end: int, substring: str) -> str:
            return string[0:start] + substring + string[end:len(string)]

        # noinspection PyShadowingNames
        def sub_pat(pat: Callable[[list], str] or str, terms: list) -> str:
            if isinstance(pat, str):
                return pat.format(*terms)
            else:
                return pat(terms)

        count = 0

        def check():
            nonlocal count
            count += 1
            if count > self.max_while:
                raise RuntimeError('Presumably while loop is stuck')

        # noinspection PyShadowingNames
        def null_replace(match) -> str:
            regex_terms = [gr for gr in match.groups() if gr is not None]
            op = regex_terms[0]
            terms = regex_terms[1:]
            return sub_pat(self.null_ops.ops[op]['pat'], terms)

        string = self.null_ops.regex.sub(null_replace, string)

        for ops, loc in [(self.pref_un_ops, 'r'), (self.postf_un_ops, 'l'),
                         (self.bin_centr_ops, 'lr')]:
            count = 0
            match = ops.regex.search(string)
            while match:
                check()
                regex_terms = [gr for gr in match.groups() if gr is not None]
                op = regex_terms[0]
                loc_map = self._local_map(match, loc)
                lmatch, rmatch = None, None
                if loc == 'l' or loc == 'lr':
                    for m in ops.ops[op]['pref'].finditer(string):
                        if m.end() <= match.start() and loc_map[m.end() - 1] == 0:
                            lmatch = m
                    if lmatch is None:
                        string = replace(string, match.start(), match.end(), match.group(0).replace(op, '\\' + op))
                        match = ops.regex.search(string)
                        continue
                    else:
                        term1 = string[lmatch.end():match.start()]
                if loc == 'r' or loc == 'lr':
                    for m in ops.ops[op]['postf'].finditer(string):
                        if m.start() >= match.end() and loc_map[m.start()] == 0:
                            rmatch = m
                            break
                    if rmatch is None:
                        string = replace(string, match.start(), match.end(), match.group(0).replace(op, '\\' + op))
                        match = ops.regex.search(string)
                        continue
                    else:
                        term2 = string[match.end():rmatch.start()]
                if loc == 'l':
                    terms = list(lmatch.groups()) + [term1] + regex_terms[1:]
                    start, end = lmatch.start(), match.end()
                elif loc == 'r':
                    terms = regex_terms[1:] + [term2] + list(rmatch.groups())
                    start, end = match.start(), rmatch.end()
                elif loc == 'lr':
                    terms = list(lmatch.groups()) + [term1] + regex_terms[1:] + [term2] + list(rmatch.groups())
                    start, end = lmatch.start(), rmatch.end()
                else:  # this never happen
                    terms = regex_terms[1:]
                    start, end = match.start(), match.end()

                string = replace(string, start, end, sub_pat(ops.ops[op]['pat'], terms))
                match = ops.regex.search(string)

        return string

    def mjx_hack(self):
        s = self.pref_un_ops.styles
        s2 = self.pref_un_ops.other_styles
        s.styles['^{β}'] = s.mjx_bi
        s.styles['^{m}'] = s.mjx_m
        s.styles['^{tβ}'] = s2.mjx_tbi
        s2.styles['‹^{β}']['pat'] = s2.mjx_tbi

    def mpl_hack(self):
        s = self.pref_un_ops.styles
        s.styles['^{β}'] = s.mpl_bi

    def replace(self, src: str) -> str:
        """
        Extends LaTeX syntax via regex preprocess
        :param src: str
            LaTeX string
        :return: str
            New LaTeX string
        """
        # Brackets + simple pre replacements:
        src = self._dict_replace(self.simple_pre, src)

        # Superscripts and subscripts + pre regexps:
        for regex, replace in self.regex_pre:
            src = regex.sub(replace, src)

        # Unary and binary operators:
        src = self._operators_replace(src)

        # Loop regexps:
        src_prev = src
        for i in range(self.max_iter):
            for regex, replace in self.loop_regexps:
                src = regex.sub(replace, src)
            if src_prev == src:
                break
            else:
                src_prev = src

        # Post regexps:
        for regex, replace in self.regex_post:
            src = regex.sub(replace, src)

        # Simple post replacements:
        src = self._dict_replace(self.simple_post, src)

        # Escape characters:
        src = self.escapes_regex.sub(r'\1', src)

        return src
