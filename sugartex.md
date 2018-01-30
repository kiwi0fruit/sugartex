# SugarTeX

SugarTeX is a more readable LaTeX language extension and a transcompiler to LaTeX.

This is a PDF version of the SugarTeX documentation. See original markdown version [here](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md) (Unicode characters will not have intended look there).

#### TODO сделать, чтобы все ссылки на этот документ были на pdf версию. Ко всем привести примеры до и после (матрицы, дроби и т.д.).


# Contents

* [Command line interfaces](#command-line-interfaces)
* [Tweaking SugarTeX](#tweaking-sugartex)
* [SugarTeX replacements and operators](#sugartex-replacements-and-operators)
    * [Brackets](#brackets)
    * [Simple pre-replacements](#simple-pre-replacements)
    * [Superscripts and Subscripts](#superscripts-and-subscripts)
    * [Regular expressions pre-replacements](#regular-expressions-pre-replacements)
    * [Nullary operators](#nullary-operators)
    * [Prefix unary operators](#prefix-unary-operators)
        * [Styles](#styles)
        * [Styles with special brackets](#styles-with-special-brackets)
        * [Greedy prefix unary operators](#greedy-prefix-unary-operators)
        * [Standard prefix unary operators](#standard-prefix-unary-operators)
    * [Postfix unary operators](#postfix-unary-operators)
    * [Center binary operators](#center-binary-operators)
        * [Matrices](#matrices)
        * [Greedy center binary operators](#greedy-center-binary-operators)
        * [Standard center binary operators](#standard-center-binary-operators)
    * [Regular expressions loop replacements](#regular-expressions-loop-replacements)
    * [Regular expressions post-replacements](#regular-expressions-post-replacements)
    * [Simple post-replacements](#simple-post-replacements)
    * [Escapable characters](#escapable-characters)
* [Examples](#examples)


# Command line interfaces

1. `sugartex`:
    * sugartex reads from stdin and writes to stdout,
    * `sugartex TO` - run Pandoc filter that iterates over math blocks,
    * `sugartex --kiwi` - same as above but with kiwi flavor,
2. `pre-sugartex`:
    * pre-sugartex reads from stdin and writes to stdout,
    * `pre-sugartex` - replace `ˎ` with `$` only,
    * `pre-sugartex --all` - replace everything with regexp,
    * `pre-sugartex --kiwi` - same as above but with kiwi flavor.

[Panflute](https://github.com/sergiocorreia/panflute) scripts are also installed so you can use it in default Panflute [automation interface in metadata](http://scorreia.com/software/panflute/guide.html#running-filters-automatically) or in it's CLI wrapper from [pandoctools](https://github.com/kiwi0fruit/pandoctools):

* `panfl sugartex_panfl --to markdown`,
* `panfl sugartex_kiwi -t markdown`.

Examples. Windows:

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


# Tweaking SugarTeX

SugarTeX is written in python and has a tweakable architecture. As you can see in [this filter](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/filters/sugartex_kiwi.py) tweaks can be made in between:
```py
sugartex = SugarTeX(delay=True)
...
sugartex.ready()
```

Attributes of instance of `SugarTeX` class can be changed. See them in defining of `SugarTeX` class and in it's `__init__` method [here](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sugartex/sugartex.py). List of attributes:

* `.brackets`
* `.brackets_types`
* `.simple_pre`
* `.superscripts`
* `.subscripts`
* `.regex_pre`
* `.null_ops` (class `NullOps`)
* `.pref_un_ops` (class `PrefUnOps`), including:
    * `.styles` (class `Styles`)
    * `.other_styles` (class `OtherStyles`)
    * `.pref_un_greedy` (class `PrefUnGreedy`)
* `.postf_un_ops` (class `PostfUnOps`)
* `.bin_centr_ops` (class `BinCentrOps`), including:
    * `.matrices` (class `Matrices`)
    * `.bin_centr_greedy` (class `BinCentrGreedy`)
* `.loop_regexps`
* `.regex_post`
* `.simple_post`
* `.escapes`



# SugarTeX replacements and operators

## Brackets

Independently replace brackets:

* `˳(` → `\left({` and `)˳` → `}\right)` (modifier letter low ring U+02F3),
* `˳˳(` → `\bigl(` and `)˳˳` → `\bigr)`,
* `˳ˌ(` → `\Bigl(` and `)˳ˌ` → `\Bigr)`,
* `ˌ˳(` → `\biggl(` and `)ˌ˳` → `\biggr)`,
* `ˌˌ(` → `\Biggl(` and `)ˌˌ` → `\Biggr)` (modifier letter low vertical line U+02CC).

Instead of `(` and `)` can be other brackets:

* `[` → `[` and `]` → `]`,
* `(` → `(` and `)` → `)`,
* `{` → `\{` and `}` → `\}`,
* `│` → `\vert` (box drawings light vertical U+2502, for math in markdown tables),
* `|` → `\vert`,
* `‖` → `\Vert` (double vertical line U+2016),
* `˱` → `.` and `˲` → `.` (modifier letter low left/right arrowhead U+02F1/U+02F2),
* `⟨` → `\langle` and `⟩` → `\rangle` (mathematical left/right angle bracket U+27E8/27E9),
* `⌊` → `\lfloor` and `⌋` → `\rfloor` (left/right floor U+230A/U+230B),
* `⌈` → `\lceil` and `⌉` → `\rceil` (left/right ceiling U+2308/U+2309.


## Simple pre-replacements

* `∛` → `3√` (cube root U+221B),
* `∜` → `4√` (fourth root U+221C),
* ` ` → `\,` (thin space U+2009).


## Superscripts and Subscripts

Groups of superscript Unicode characters like `¹²³` are replaced with `^{123}`. Unless they are escaped with `\` or followed by `√`:

* `\¹²³√` → `¹23√` (square root U+221A),
* `\¹²³` → `¹^{23}`,
* `¹²³` → `^{123}`.

Same is for groups of subscript Unicode characters:

* `\₁₂₃` → `₁_{23}`.
* `₁₂₃` → `_{123}`.

List of supported characters can be found in the beginning of the SugarTeX [source code](https://github.com/kiwi0fruit/pandoctools/blob/master/pandoctools/sugartex/sugartex.py).

**UPDATE**

Now `‹›` and `˹˺` from [Styles with special brackets](#styles-with-special-brackets) end up inside `_{}`/`^{}`, like: `A‹ₐₑ›` → `A_{‹ae›}`. Does not work if there are non-subscript/superscript characters inside `‹›`/`˹˺`, like: `A‹ᵃe›` → `A‹^{a}e›`.


## Regular expressions pre-replacements

Nothing. But can be tweaked.


## Nullary operators

Big operators replacements:

* `∑` → `\sum` (n-ary summation U+2211),
* `∑:` → `\sum\nolimits`,
* `∑⢈` → `\sum\limits` (braille pattern dots-48 U+2888).

Supported symbols for limits:

* `⢈`, `⡁` → `\limits` (braille pattern dots-48/dots-17 U+2888/U+2841),
* `:`, `⠆`, `⠰` → `\nolimits` (braille pattern dots-23/dots-56 U+2806/U+2830).

Supported big operators:

* `∑` → `\sum`,
* `∏` → `\prod`,
* `∫` → `\int`,
* `∬` → `\iint`,
* `∭` → `\iiint`,
* `⨌` → `\iiiint`,
* `∮` → `\oint`.

*Who knows what I was thinking about by adding them here instead of Regular expressions replacements...*


## Prefix unary operators

### Styles

Text inside standard brackets (`()`, `[]`, `{}`) with special prefix is replaced with style operator. For example:

`[ʳtext]` or `[^{r}text]` → `\mathrm{text}`.

First SugarTeX finds opening part like `[^{r}` then searches for the first non-escaped closing part `]` that is not inside `{}` or `˱˲` – SugarTeX counts opening and closing `{}˱˲` (`˱˲` would later be replaced with `{}` so both are counted together). For example:

`(ʳsome{te)(t})` → `\mathrm{some{te)(t}}`.

List of available styles:

* `{ʳtext}` / `{^{r}text}` → `\mathrm{text}` (**math regular**),
* `{ⁱx}` / `{^{i}x}` → `\mathit{x}` (**math italic**),
* `{ᵇx}` / `{^{b}x}` → `\mathbf{x}` (**math bold**),
* `{ᵝx}` / `{^{β}x}` → `\boldsymbol{x}` (**math bold italic**),
* `{ᵐtext}` / `{^{m}text}` → `\mathtt{text}` (**math monospace**),
* `{ᶜA}` / `{^{c}A}` → `\mathcal{A}` (**math calligraphic**,  
  no cyrillic support, see Monotype Corsiva),
* `{ᵗtext}` / `{^{t}text}` → `\text{text}` (**text**),
* `{ᵗⁱtext}` / `{^{ti}text}` → `\textit{text}` (**text italic**),
* `{ᵗᵇtext}` / `{^{tb}text}` → `\textbf{text}` (**text bold**),
* `{ᵗᵝtext}` / `{^{tβ}text}` → `\textit{\textbf{text}}` (**text bold italic**),
* `{ ⃗x}` / `{⃗x}` → `\mathbf{x}` (**vector bold notation**,  
  combining right arrow above U+20D7, first one is 'space' +\ \  ⃗ ),
* `{⠘x}` / `{⠃x}` → `\mathbf{x}` (**vector bold notation**,  
  braille pattern dots-45/dots-12 U+2818/U+2803 [right upper 2/left upper 2]),
* `{⠋A}` / `{⠛A}` → `\mathbf{A}` (**matrix bold notation**,  
  braille pattern dots-124/dots-1245 U+280B/U+281B).


### Styles with special brackets

* `‹ᵝtext›` / `‹^{β}text›` → `\textit{\textbf{text}}` (**text bold italic**),
* `‹ⁱtext›` / `‹^{i}text›` → `\textit{text}` (**text italic**),
* `‹ᵇtext›` / `‹^{b}text›` → `\textbf{text}` (**text bold**),
* `‹text›` → `\text{text}` (**text regular**,  
  single left/right-pointing angle quotation mark U+2039/U+203A),
* `˹text˺` → `\mathrm{text}` (**math regular**,  
  modifier letter begin/end high tone U+02F9/U+02FA).


### Greedy prefix unary operators

* `{⋲ smth}` / `˱⋲ smth˲` → `\begin{cases} smth\end{cases}` (**piecewise**, element of with long horizontal stroke U+22F2).

SugarTeX finds non-escaped `{⋲` or `˱⋲` first then searches for non-escaped `}` or `˲` that is not inside `{}` or `˱˲` – SugarTeX counts opening and closing `{}˱˲` (`˱˲` would later be replaced with `{}` so both are counted together).


### Standard prefix unary operators

* `⧼matrix a` → `\begin{matrix} a`  
  (left-pointing curved angle bracket U+29FC),
* `👻 A² a` → `\vphantom{A^2} a`  
  (**invisible characters that adjust height**, ghost U+1F47B),
* `→⎴ text a` → `\xrightarrow{text} a`  
  (**arrow with text above that adjusts to the text length**, rightwards arrow U+2192, top square bracket U+23B4),
* `←⎴˱long text˲ a` → `\xleftarrow{{long text}} a`  
  (leftwards arrow U+2190).

SugarTeX finds non-escaped `⧼ *` first (for example) then searches for a place before non-escaped `}`, `˲`, space, newline or end of the string that is not inside `{}` or `˱˲` – SugarTeX counts opening and closing `{}˱˲` (`˱˲` would later be replaced with `{}` so both are counted together).


## Postfix unary operators

* `a x ⃗` → `a \vec{x }` (**vector**,  
  combining right arrow above U+20D7),
* `a x ⃑` → `a \overrightarrow{x }` (**arrow above**,  
  combining right harpoon above U+20D1),
* `a x^` → `a \widehat{x}` (modifier letter up arrowhead U+02C4)
  **warning**: works only if the next character after `^` is `}`, `˲`, newline or end of the string,
* `a xˆ` → `a \hat{x}` (modifier letter circumflex accent U+02C6),
* `a x¯` → `a \bar{x}` (macron U+00AF),    
* `a x‾` → `a \overline{x}` (overline U+203E),    
* `a x˙` → `a \dot{x}` (dot above U+02D9),    
* `a x¨` → `a \ddot{x}` (diaeresis U+00A8),
* `x + y+z⏞` → `x + \overbrace{y+z}`  
  (top curly bracket U+23DE),
* `x + {y + z}⏟` → `x + \underbrace{{y + z}}`  
  (bottom curly bracket U+23DF),
* `a xˍ` → `a \underline{x}`  
  **warning**: works only if the next character after `ˍ` is `}`, `˲`, newline or end of the string (modifier letter low macron U+02CD),
* `a matrix⧽` → `a \end{matrix}`  
  (right-pointing curved angle bracket U+29FD),

SugarTeX finds non-escaped <code> \*⧽</code> first (for example) then before it searches for a place after non-escaped `{`, `˱`, space, newline or start of the string that is not inside `{}` or `˱˲` – SugarTeX counts opening and closing `{}˱˲` (`˱˲` would later be replaced with `{}` so both are counted together).

**In combination with styles:**

When combining **one-character** postfix unary operators with styles the order in which operators are applied changes:

`[ᵇx ⃗]` → `\vec{\mathbf{x }}`


## Center binary operators

### Matrices

Family of `*matrix` amsmath macros is given by `¦⠋` operator:

`˱[a b ¦⠋ c d]˲` →  
 `\begin{bmatrix}a b¦c d\end{bmatrix}`  

All brackets:

* `˱a b ¦⠋ c d˲` → `...matrix...` (**no brackets**,  
  modifier letter low left/right arrowhead U+02F1/U+02F2),
* `{a b ¦⠋ c d}` → `...Bmatrix...` (**curly brackets**),
* `˱(a b ¦⠋ c d)˲`/`{(a b ¦⠋ c d)}` → `...pmatrix...`,
* `˱[a b ¦⠋ c d]˲`/`{[a b ¦⠋ c d]}` → `...bmatrix...`,
* `˱│a b ¦⠋ c d│˲`/`{│a b ¦⠋ c d│}`/  
  `˱|a b ¦⠋ c d|˲`/`{|a b ¦⠋ c d|}` → `...vmatrix...`  
  (box drawings light vertical U+2502, for math in markdown tables),
* `˱‖a b ¦⠋ c d‖˲`/`{‖a b ¦⠋ c d‖}` → `...Vmatrix...`  
  (double vertical line U+2016).

### Matrices

#### TODO

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


### Greedy center binary operators

#### TODO
pref = r'(?<!\\)[˱{]'  # language=PythonRegExp
postf = r'(?<!\\)[˲\}]'
ops = OrderedDict([  # should have only one slot
    ('¦⠛^{t}', r'\begin{{smallmatrix}}{}¦{}\end{{smallmatrix}}'),
    ('¦⠛', r'\begin{{array}}{}¦{}\end{{array}}'),
    ('¦#', r'\begin{{aligned}}{}¦{}\end{{aligned}}'),
    ('¦˽^{l}', r'{{\begin{{subarray}}{{l}}{}¦{}\end{{subarray}}}}'),
    ('¦˽^{c}', r'{{\begin{{subarray}}{{c}}{}¦{}\end{{subarray}}}}'),
    ('¦˽^{r}', r'{{\begin{{subarray}}{{r}}{}¦{}\end{{subarray}}}}'),
    ('¦˽', r'{{\substack{{{}¦{}}}}}'),
])


### Standard center binary operators

#### TODO
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
    ('¦^{c}', {'pat': r'\binom{{{}}}{{{}}}', 'pref': _choose_pref, 'postf': _choose_postf}),
    ('¦^{ct}', {'pat': r'\tbinom{{{}}}{{{}}}', 'pref': _choose_pref, 'postf': _choose_postf}),  # (n¦ᶜᵗm)
    ('¦^{cd}', {'pat': r'\dbinom{{{}}}{{{}}}', 'pref': _choose_pref, 'postf': _choose_postf}),
])_


## Regular expressions loop replacements

Nothing. But can be tweaked.


## Regular expressions post-replacements

Nothing. But can be tweaked.


## Simple post-replacements

* `¦` → `\\` (broken bar U+00A6, this should be after other `¦` replacements),
* `˳` → `&` (modifier letter low ring U+02F3, this should be after brackets and other `˳` replacements),
* `˱` → `{` and `˲` → `}` (modifier letter low left/right arrowhead U+02F1/U+02F2),
* `ˍ` → `_` (modifier letter low macron U+02CD),
* `↕^{d}` → `\displaystyle` (up down arrow U+2195),
* `↕^{t}` → `\textstyle`,
* `↕^{s}` → `\scriptstyle`,
* `↕^{xs}` → `\scriptscriptstyle`,
* Superscripts and Subscripts replacements give:
* `↕ᵈ` → `\displaystyle`,
* `↕ᵗ` → `\textstyle`,
* `↕ˢ` → `\scriptstyle`,
* `↕ˣˢ` → `\scriptscriptstyle`,


## Escapable characters

All one-character replacements from:

* Prefix unary operators,
* Postfix unary operators,
* Center binary operators,
* Nullary operators,
* Simple pre-replacements,
* Simple post-replacements,

and `⋲`, `›`, `˺`, `↕`, `ˌ`

(element of with long horizontal stroke U+22F2, single right-pointing angle quotation mark U+203A, modifier letter end high tone U+02FA, up down arrow U+2195, modifier letter low vertical line U+02CC)

are escapable with `\`.


# Examples

```md
ˎˎ
˱∇ × [ ⃗B] - 1∕c ∂[ ⃗E]∕∂t ˳= 4π∕c [ ⃗j] ¦#
               ∇ ⋅ [ ⃗E]\ ˳= 4πρ       ¦
 ∇ × [ ⃗E] + 1∕c ∂[ ⃗B]∕∂t ˳= [ ⃗0]      ¦
               ∇ ⋅ [ ⃗B]\ ˳= 0         ˲
,ˎˎ{#eq:max}

where ˎ[ ⃗B], [ ⃗E], [ ⃗j]: ℝ⁴ → ℝ³ˎ – vector functions of the form
ˎ(t,x,y,z) ↦ [ ⃗f](t,x,y,z), [ ⃗f] = (f_˹x˺, f_˹y˺, f_˹z˺)ˎ.
```
renders to:

$$
\begin{aligned}∇ × {\mathbf{B}} - \frac{1}{c} \frac{∂{\mathbf{E}}}{∂t} &= \frac{4π}{c} {\mathbf{j}}\\
               ∇ ⋅ {\mathbf{E}}\  &= 4πρ       \\
 ∇ × {\mathbf{E}} + \frac{1}{c} \frac{∂{\mathbf{B}}}{∂t} &= {\mathbf{0}}      \\
               ∇ ⋅ {\mathbf{B}}\  &= 0         \end{aligned}
,$${\#eq:max}

where ${\mathbf{B}},\,{\mathbf{E}},\,{\mathbf{j}}:\,ℝ^{4} → ℝ^{3}$ --
vector functions of the form
$(t,x,y,z) ↦ {\mathbf{f}}(t,x,y,z),\,{\mathbf{f}} = (f_{\mathrm{x}}, f_{\mathrm{y}}, f_{\mathrm{z}})$.


#### TODO more examples

‹› = \<  \> = single left/right-pointing angle quotation mark
˱˲ = \_<  \_> = modifier letter low left/right arrowhead
 ⃗ = \^-> = combining right arrow above
 ⃑ = \^--> = combining right harpoon above
ˍ = \_ = modifier letter low macron
⣤ = \_:: = braille pattern dots-3678
⠛ = \^:: = braille pattern dots-1245
⠘ = braille pattern dots-45 (right upper 2)
⠃ = braille pattern dots-12 (left upper 2)
⢈ = \:b = braille pattern dots-48
⡁ = braille pattern dots-17
⠆ = braille pattern dots-23
⠰ = \:s = braille pattern dots-56
 ⃔ = \^^ = combining anticlockwise arrow above
ˎ = \_` = modifier letter low grave accent
ˌ = \_'s = modifier letter low vertical line
⋲ = -E = element of with long horizontal stroke
˄ = \^bb = modifier letter up arrowhead
ˆ = \^ss = modifier letter circumflex accent
˽ = \__ = modifier letter shelf
‖ = \|| = double vertical line
│ = \| = box drawings light vertical
ˊˋ = \`m (modif letter) \` (modif letter) = modifier letter acute/grave accent
\]em/3[ = three-per-em space
👻 = \ghost
˚ = \^os = ring above
ˈ = \'s = modifier letter vertical line
¦ = \\ = \|/2 = broken bar
┆ = \|/3 = box drawings light triple dash vertical
˹˺ = \^rs = modifier letter begin/end high tone
\__- = combining macron below
\^ + symbol = modifier letter small / superscript
\_ + symbol = subscript

↕ = v|^ = up down arrow

√ = \sqrt
