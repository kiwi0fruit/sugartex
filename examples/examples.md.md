---
autoEqnLabels: False
autoSectionLabels: False
ccsDelim: ','
ccsLabelSep: '---'
ccsTemplate: $$i$$$$ccsLabelSep$$$$t$$
chapDelim: '.'
chapters: False
chaptersDepth: 1
codeBlockCaptions: False
comments-map:
  js:
  - '//'
  - '/\*'
  - '\*/'
  py:
  - '\#'
  - ''''''''
  - ''''''''
  - '\"\"\"'
  - '\"\"\"'
  r:
  - '\#'
  - ''''
  - ''''
  - '\"'
  - '\"'
  ts:
  - '//'
  - '/\*'
  - '\*/'
cref: False
crossrefYaml: 'pandoc-crossref.yaml'
eqnLabels: arabic
eqnPrefix:
- 'eq.'
- 'eqns.'
eqnPrefixTemplate: $$p$$ $$i$$
eval: False
figLabels: arabic
figPrefix:
- 'fig.'
- 'figs.'
figPrefixTemplate: $$p$$ $$i$$
figureTemplate: $$figureTitle$$ $$i$$$$titleDelim$$ $$t$$
figureTitle: Figure
kernels-map:
  py: python3
  r: ir
lastDelim: ','
linkReferences: False
listingTemplate: $$listingTitle$$ $$i$$$$titleDelim$$ $$t$$
listingTitle: Listing
listings: False
lofTitle: |
    List of Figures
    ===============
lolTitle: |
    List of Listings
    ================
lotTitle: |
    List of Tables
    ==============
lstLabels: arabic
lstPrefix:
- 'lst.'
- 'lsts.'
lstPrefixTemplate: $$p$$ $$i$$
nameInLink: False
numberSections: False
pairDelim: ','
pandoctools:
  out: '*.*.md'
  profile: Kiwi
rangeDelim: '\-'
refDelim: ','
refIndexTemplate: $$i$$$$suf$$
secHeaderTemplate: $$i$$$$secHeaderDelim$$$$t$$
secLabels: arabic
secPrefix:
- 'sec.'
- 'secs.'
secPrefixTemplate: $$p$$ $$i$$
sectionsDepth: 0
styles-map:
  py: python
subfigGrid: False
subfigLabels: alpha a
subfigureChildTemplate: $$i$$
subfigureRefIndexTemplate: '$$i$$$$suf$$ ($$s$$)'
subfigureTemplate: '$$figureTitle$$ $$i$$$$titleDelim$$ $$t$$. $$ccs$$'
tableEqns: False
tableTemplate: $$tableTitle$$ $$i$$$$titleDelim$$ $$t$$
tableTitle: Table
tblLabels: arabic
tblPrefix:
- 'tbl.'
- 'tbls.'
tblPrefixTemplate: $$p$$ $$i$$
titleDelim: ':'
---

    See @eq:max.
    ˎˎ
    ˱∇ × [ ⃗B] - 1∕c ∂[ ⃗E]∕∂t ˳= 4π∕c [ ⃗j] ¦#
                   ∇ ⋅ [ ⃗E]\ ˳= 4πρ       ¦
     ∇ × [ ⃗E] + 1∕c ∂[ ⃗B]∕∂t ˳= [ ⃗0]      ¦
                   ∇ ⋅ [ ⃗B]\ ˳= 0         ˲
    ,ˎˎ{#eq:max}

    where ˎ[ ⃗B], [ ⃗E], [ ⃗j]: ℝ⁴ → ℝ³ˎ – vector functions of the form
    ˎ(t,x,y,z) ↦ [ ⃗f](t,x,y,z), [ ⃗f] = (f_˹x˺, f_˹y˺, f_˹z˺)ˎ.

See eq. 1. [$$
\begin{aligned}∇ × {\mathbf{B}} - \frac{1}{c} \frac{∂{\mathbf{E}}}{∂t} &= \frac{4π}{c} {\mathbf{j}}\\
               ∇ ⋅ {\mathbf{E}}\ &= 4πρ       \\
 ∇ × {\mathbf{E}} + \frac{1}{c} \frac{∂{\mathbf{B}}}{∂t} &= {\mathbf{0}}      \\
               ∇ ⋅ {\mathbf{B}}\ &= 0         \end{aligned}
,\qquad(1)$$]{#eq:max}

where ${\mathbf{B}},\,{\mathbf{E}},\,{\mathbf{j}}:\,ℝ^{4} → ℝ^{3}$ --
vector functions of the form
$(t,x,y,z) ↦ {\mathbf{f}}(t,x,y,z),\,{\mathbf{f}} = (f_{\mathrm{x}}, f_{\mathrm{y}}, f_{\mathrm{z}})$.

------------------------------------------------------------------------

    See @eq:max2.
    ˎˎ
    ˱∇ × 𝐁 - 1∕c ∂𝐄∕∂t ˳= 4π∕c 𝐣 ¦#
                ∇ ⋅ 𝐄\ ˳= 4πρ    ¦
     ∇ × 𝐄 + 1∕c ∂𝐁∕∂t ˳= 𝟎      ¦
                ∇ ⋅ 𝐁\ ˳= 0      ˲
    ,ˎˎ{#eq:max2}

    where ˎ𝐁, 𝐄, 𝐣: ℝ⁴ → ℝ³ˎ – vector functions of the form
    ˎ(t,x,y,z) ↦ 𝐟(t,x,y,z), 𝐟 = (f_˹x˺, f_˹y˺, f_˹z˺)ˎ.

See eq. 2. [$$
\begin{aligned}∇ × 𝐁 - \frac{1}{c} \frac{∂𝐄}{∂t} &= \frac{4π}{c} 𝐣\\
            ∇ ⋅ 𝐄\ &= 4πρ    \\
 ∇ × 𝐄 + \frac{1}{c} \frac{∂𝐁}{∂t} &= 𝟎      \\
            ∇ ⋅ 𝐁\ &= 0      \end{aligned}
,\qquad(2)$$]{#eq:max2}

where $𝐁,\,𝐄,\,𝐣:\,ℝ^{4} → ℝ^{3}$ -- vector functions of the form
$(t,x,y,z) ↦ 𝐟(t,x,y,z),\,𝐟 = (f_{\mathrm{x}}, f_{\mathrm{y}}, f_{\mathrm{z}})$.

------------------------------------------------------------------------

    ˎˎ [⠋A] = [⠋B]˹ᵀ˺ [⠋C] [⠋B] ˎˎ

    ˎˎ 𝐀 = 𝐁˹ᵀ˺𝐂 𝐁 ˎˎ

$$ {\mathbf{A}} = {\mathbf{B}}^{{\mathrm{T}}} {\mathbf{C}}\,{\mathbf{B}} $$

$$ 𝐀 = 𝐁^{{\mathrm{T}}}𝐂\,𝐁 $$

    ˎˎ
    ˱[ x₁₁ ˳x₁₂ ˳x₁₃ ˳… ˳x₁ₙ ¦⠋
       x₂₁ ˳x₂₂ ˳x₂₃ ˳… ˳x₂ₙ ¦
        ⋮  ˳ ⋮  ˳ ⋮  ˳⋱ ˳ ⋮  ¦
       xₚ₁ ˳xₚ₂ ˳xₚ₃ ˳… ˳xₚₙ ]˲ ˎˎ

$$
\begin{bmatrix} x_{11} &x_{12} &x_{13} &… &x_{1n}\\
   x_{21} &x_{22} &x_{23} &… &x_{2n} \\
    ⋮  & ⋮  & ⋮  &⋱ & ⋮  \\
   x_{p1} &x_{p2} &x_{p3} &… &x_{pn} \end{bmatrix} $$

------------------------------------------------------------------------

    ˎˎ ˋdefˋB{
    ˱[ ax₀ + by₁ ¦⠋
       ax₁ + by₂ ¦
           ⋮     ¦
       ax_{N-1} + by_{N-1} ]˲
    }¦
    ˋB = a[ ⃗x] + b[ ⃗y] ˎˎ

$$ \def\B{
\begin{bmatrix} ax_{0} + by_{1}\\
   ax_{1} + by_{2} \\
       ⋮     \\
   ax_{N-1} + by_{N-1} \end{bmatrix}
}\\
\B = a{\mathbf{x}} + b{\mathbf{y}} $$

------------------------------------------------------------------------

    ˎˎ ˳|x|˳ = {⋲  x˳ ‹if› x≥0 ¦
                  -x˳ ‹if› x<0 } ˎˎ

    ˎˎ ˹boole˺(x) = {⋲ 1˳ ‹if ˎxˎ is › [ᵐTrue]  ¦
                       0˳ ‹if ˎxˎ is › [ᵐFalse] } ˎˎ

$$ \left\vert{x}\right\vert = \begin{cases}  x& {\text{if}} x≥0 \\
              -x& {\text{if}} x<0 \end{cases} $$

$$ {\mathrm{boole}}(x) = \begin{cases} 1& {\text{if $x$ is }} {\class{MJX-Monospace}{\mathtt{True}}}  \\
                   0& {\text{if $x$ is }} {\class{MJX-Monospace}{\mathtt{False}}} \end{cases} $$

------------------------------------------------------------------------

    ˎˎ ˹lim˺˽x→0 ˱˹sin˺ x˲∕x = 1ˎˎ
    ˎˎ U_{δ₁ρ₂}^{β₁α₂} ˎˎ
    ˎˎ √x = 1 + ˱x-1˲∕ᶜ{2 + ˱x-1˲∕ᶜ{2 + ˱x-1˲∕ᶜ{2 + ⋱}}} ˎˎ
    ˎˎ ˹sin˺² x¨ + ˹cos˺² x¨ = 1 ˎˎ

$$ \underset{x→0}{{\mathrm{lim}}} \frac{{{\mathrm{sin}}\,x}}{x} = 1$$
$$ U_{δ_{1}ρ_{2}}^{β_{1}α_{2}} $$
$$ \sqrt[]{x} = 1 + \cfrac{{x-1}}{{2 + \cfrac{{x-1}}{{2 + \cfrac{{x-1}}{{2 + ⋱}}}}}} $$
$$ {\mathrm{sin}}^{2} \ddot{x} + {\mathrm{cos}}^{2} \ddot{x} = 1 $$

------------------------------------------------------------------------

    ˎˎ α₂³∕³√{β₂² + γ₂²} ˎˎ
    ˎˎ (x + y)² = ∑ₖ₌₀^∞ (n¦ᶜk)xⁿ⁻ᵏyᵏ ˎˎ
    ˎˎ (n¦ᶜk) = ˱(n¦⠘k)˲, ˱[n¦⠘k]˲ ˎˎ

$$ \frac{α_{2}^{3}}{\sqrt[3]{{β_{2}^{2} + γ_{2}^{2}}}} $$
$$ (x + y)^{2} = \sum_{k=0}^∞ \binom{n}{k}x^{n-k}y^{k} $$
$$ \binom{n}{k} = \genfrac{(}{)}{0pt}{}{n}{k}, \genfrac{[}{]}{0pt}{}{n}{k}$$

------------------------------------------------------------------------

    ˎˎ {x + … + x}⏞⎴{k ‹times›} ˎˎ
    ˎˎ πd²∕4 1∕˳(A+B)˳² =
       πd²∕4👻{˳(A)˳²} 1∕˳(A+B)˳² ˎˎ
    ˎˎ ∑ⁿˍ{0≤i≤N ¦˽ 0≤j≤M} (ij)² +
       ∑ⁿˍ{i∈A ¦˽ˡ 0≤j≤M} (ij)²  ˎˎ

$$\overset{{k {\text{times}}}}{\overbrace{{x + … + x}}}$$
$$ \frac{πd^{2}}{4} \frac{1}{\left({A+B}\right)^{2}} =
   \frac{πd^{2}}{4\vphantom{{\left({A}\right)^{2}}}} \frac{1}{\left({A+B}\right)^{2}} $$
$$ \sum^{n}_{\substack{0≤i≤N\\0≤j≤M}} (ij)^{2} +
   \sum^{n}_{\begin{subarray}{l}i∈A\\0≤j≤M\end{subarray}} (ij)^{2}  $$

------------------------------------------------------------------------

    ˎˎ ˹erf˺(x) = 1∕√π ∫₋ₓˣ e^{-t²} dt ˎˎ
    ˎˎ f⁽²⁾(0) = f''(0) = ˳˱d²f∕dx²|˳ₓ₌₀ ˎˎ
    Text ˎ˳˳(˱a ˳b ¦⠛ᵗ c ˳d˲)˳˳ˎ and some more text.

$$ {\mathrm{erf}}(x) = \frac{1}{\sqrt[]{π}} \int_{-x}^{x} e^{-t^{2}} dt $$
$$ f^{(2)}(0) = f''(0) = \left.{\frac{d^{2}f}{dx^{2}}}\right\vert_{x=0} $$
Text $\bigl( \begin{smallmatrix}a &b\\c &d\end{smallmatrix}\bigr)$ and
some more text.

------------------------------------------------------------------------

prefix unary operator `→⎴`:

    ˎˎ f: x →⎴{‹arrow map›} ˽i x² ˎˎ

$$ f: x \underset{i}{\xrightarrow{{{\text{arrow map}}}}} x^{2} $$ center
binary operator `⎴`:

    ˎˎ f: x → ⎴‹arrow map› ˽i x² ˎˎ

$$ f: x \underset{i}{\overset{{\text{arrow map}}}{→}} x^{2} $$ bug
because styles also implemented as prefix unary operators (but by design
styles should have priority!):

    ˎˎ f: x →⎴‹arrow map› ˽i x² ˎˎ

$$ f: x \xrightarrow{‹arrow} \underset{i}{map›} x^{2} $$
