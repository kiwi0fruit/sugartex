---
eval: False
pandoctools:
  profile: Kiwi
  # out: "*.*.md"
  out: "*.pdf"
---

```
See @eq:max.
\ˎ\ˎ
˱∇ × [ ⃗B] - 1∕c ∂[ ⃗E]∕∂t ˳= 4π∕c [ ⃗j] ¦#
               ∇ ⋅ [ ⃗E]\ ˳= 4πρ       ¦
 ∇ × [ ⃗E] + 1∕c ∂[ ⃗B]∕∂t ˳= [ ⃗0]      ¦
               ∇ ⋅ [ ⃗B]\ ˳= 0         ˲
,\ˎ\ˎ{#eq:max}

where \ˎ[ ⃗B], [ ⃗E], [ ⃗j]: ℝ⁴ → ℝ³\ˎ – vector functions of the form
\ˎ(t,x,y,z) ↦ [ ⃗f](t,x,y,z), [ ⃗f] = (f_˹x˺, f_˹y˺, f_˹z˺)\ˎ.
```
See @eq:max.
ˎˎ
˱∇ × [ ⃗B] - 1∕c ∂[ ⃗E]∕∂t ˳= 4π∕c [ ⃗j] ¦#
               ∇ ⋅ [ ⃗E]\ ˳= 4πρ       ¦
 ∇ × [ ⃗E] + 1∕c ∂[ ⃗B]∕∂t ˳= [ ⃗0]      ¦
               ∇ ⋅ [ ⃗B]\ ˳= 0         ˲
,ˎˎ{#eq:max}

where ˎ[ ⃗B], [ ⃗E], [ ⃗j]: ℝ⁴ → ℝ³ˎ – vector functions of the form
ˎ(t,x,y,z) ↦ [ ⃗f](t,x,y,z), [ ⃗f] = (f_˹x˺, f_˹y˺, f_˹z˺)ˎ.

----


```
See @eq:max2.
\ˎ\ˎ
˱∇ × 𝐁 - 1∕c ∂𝐄∕∂t ˳= 4π∕c 𝐣 ¦#
            ∇ ⋅ 𝐄\ ˳= 4πρ    ¦
 ∇ × 𝐄 + 1∕c ∂𝐁∕∂t ˳= 𝟎      ¦
            ∇ ⋅ 𝐁\ ˳= 0      ˲
,\ˎ\ˎ{#eq:max2}

where \ˎ𝐁, 𝐄, 𝐣: ℝ⁴ → ℝ³\ˎ – vector functions of the form
\ˎ(t,x,y,z) ↦ 𝐟(t,x,y,z), 𝐟 = (f_˹x˺, f_˹y˺, f_˹z˺)\ˎ.
```
See @eq:max2.
ˎˎ
˱∇ × 𝐁 - 1∕c ∂𝐄∕∂t ˳= 4π∕c 𝐣 ¦#
            ∇ ⋅ 𝐄\ ˳= 4πρ    ¦
 ∇ × 𝐄 + 1∕c ∂𝐁∕∂t ˳= 𝟎      ¦
            ∇ ⋅ 𝐁\ ˳= 0      ˲
,ˎˎ{#eq:max2}

where ˎ𝐁, 𝐄, 𝐣: ℝ⁴ → ℝ³ˎ – vector functions of the form
ˎ(t,x,y,z) ↦ 𝐟(t,x,y,z), 𝐟 = (f_˹x˺, f_˹y˺, f_˹z˺)ˎ.

----

```
\ˎ\ˎ [⠋A] = [⠋B]˹ᵀ˺ [⠋C] [⠋B] \ˎ\ˎ

\ˎ\ˎ 𝐀 = 𝐁˹ᵀ˺𝐂 𝐁 \ˎ\ˎ
```
ˎˎ [⠋A] = [⠋B]˹ᵀ˺ [⠋C] [⠋B] ˎˎ

ˎˎ 𝐀 = 𝐁˹ᵀ˺𝐂 𝐁 ˎˎ

```
\ˎ\ˎ
˱[ x₁₁ ˳x₁₂ ˳x₁₃ ˳… ˳x₁ₙ ¦⠋
   x₂₁ ˳x₂₂ ˳x₂₃ ˳… ˳x₂ₙ ¦
    ⋮  ˳ ⋮  ˳ ⋮  ˳⋱ ˳ ⋮  ¦
   xₚ₁ ˳xₚ₂ ˳xₚ₃ ˳… ˳xₚₙ ]˲ \ˎ\ˎ
```
ˎˎ
˱[ x₁₁ ˳x₁₂ ˳x₁₃ ˳… ˳x₁ₙ ¦⠋
   x₂₁ ˳x₂₂ ˳x₂₃ ˳… ˳x₂ₙ ¦
    ⋮  ˳ ⋮  ˳ ⋮  ˳⋱ ˳ ⋮  ¦
   xₚ₁ ˳xₚ₂ ˳xₚ₃ ˳… ˳xₚₙ ]˲ ˎˎ

----

```
\ˎ\ˎ ˋdefˋB{
˱[ ax₀ + by₁ ¦⠋
   ax₁ + by₂ ¦
       ⋮     ¦
   ax_{N-1} + by_{N-1} ]˲
}¦
ˋB = a[ ⃗x] + b[ ⃗y] \ˎ\ˎ
```
ˎˎ ˋdefˋB{
˱[ ax₀ + by₁ ¦⠋
   ax₁ + by₂ ¦
       ⋮     ¦
   ax_{N-1} + by_{N-1} ]˲
}¦
ˋB = a[ ⃗x] + b[ ⃗y] ˎˎ

----

```
\ˎ\ˎ ˳|x|˳ = {⋲  x˳ ‹if› x≥0 ¦
              -x˳ ‹if› x<0 } \ˎ\ˎ

\ˎ\ˎ ˹boole˺(x) = {⋲ 1˳ ‹if \ˎx\ˎ is › [ᵐTrue]  ¦
                   0˳ ‹if \ˎx\ˎ is › [ᵐFalse] } \ˎ\ˎ
```
ˎˎ ˳|x|˳ = {⋲  x˳ ‹if› x≥0 ¦
              -x˳ ‹if› x<0 } ˎˎ

ˎˎ ˹boole˺(x) = {⋲ 1˳ ‹if ˎxˎ is › [ᵐTrue]  ¦
                   0˳ ‹if ˎxˎ is › [ᵐFalse] } ˎˎ

----

```
\ˎ\ˎ ˹lim˺˽x→0 ˱˹sin˺ x˲∕x = 1\ˎ\ˎ
\ˎ\ˎ U_{δ₁ρ₂}^{β₁α₂} \ˎ\ˎ
\ˎ\ˎ √x = 1 + ˱x-1˲∕ᶜ{2 + ˱x-1˲∕ᶜ{2 + ˱x-1˲∕ᶜ{2 + ⋱}}} \ˎ\ˎ
\ˎ\ˎ ˹sin˺² x¨ + ˹cos˺² x¨ = 1 \ˎ\ˎ
```
ˎˎ ˹lim˺˽x→0 ˱˹sin˺ x˲∕x = 1ˎˎ
ˎˎ U_{δ₁ρ₂}^{β₁α₂} ˎˎ
ˎˎ √x = 1 + ˱x-1˲∕ᶜ{2 + ˱x-1˲∕ᶜ{2 + ˱x-1˲∕ᶜ{2 + ⋱}}} ˎˎ
ˎˎ ˹sin˺² x¨ + ˹cos˺² x¨ = 1 ˎˎ

----

```
\ˎ\ˎ α₂³∕³√{β₂² + γ₂²} \ˎ\ˎ
\ˎ\ˎ (x + y)² = ∑ₖ₌₀^∞ (n¦ᶜk)xⁿ⁻ᵏyᵏ \ˎ\ˎ
\ˎ\ˎ (n¦ᶜk) = ˱(n¦⠘k)˲, ˱[n¦⠘k]˲ \ˎ\ˎ
```
ˎˎ α₂³∕³√{β₂² + γ₂²} ˎˎ
ˎˎ (x + y)² = ∑ₖ₌₀^∞ (n¦ᶜk)xⁿ⁻ᵏyᵏ ˎˎ
ˎˎ (n¦ᶜk) = ˱(n¦⠘k)˲, ˱[n¦⠘k]˲ˎˎ

----

```
\ˎ\ˎ {x + … + x}⏞⎴{k ‹times›} \ˎ\ˎ
\ˎ\ˎ πd²∕4 1∕˳(A+B)˳² =
   πd²∕4👻{˳(A)˳²} 1∕˳(A+B)˳² \ˎ\ˎ
\ˎ\ˎ ∑ⁿˍ{0≤i≤N ¦˽ 0≤j≤M} (ij)² +
   ∑ⁿˍ{i∈A ¦˽ˡ 0≤j≤M} (ij)²  \ˎ\ˎ
```
ˎˎ{x + … + x}⏞⎴{k ‹times›}ˎˎ
ˎˎ πd²∕4 1∕˳(A+B)˳² =
   πd²∕4👻{˳(A)˳²} 1∕˳(A+B)˳² ˎˎ
ˎˎ ∑ⁿˍ{0≤i≤N ¦˽ 0≤j≤M} (ij)² +
   ∑ⁿˍ{i∈A ¦˽ˡ 0≤j≤M} (ij)²  ˎˎ

----

```
\ˎ\ˎ ˹erf˺(x) = 1∕√π ∫₋ₓˣ e^{-t²} dt \ˎ\ˎ
\ˎ\ˎ f⁽²⁾(0) = f''(0) = ˳˱d²f∕dx²|˳ₓ₌₀ \ˎ\ˎ
Text \ˎ˳˳(˱a ˳b ¦⠛ᵗ c ˳d˲)˳˳\ˎ and some more text.
```
ˎˎ ˹erf˺(x) = 1∕√π ∫₋ₓˣ e^{-t²} dt ˎˎ
ˎˎ f⁽²⁾(0) = f''(0) = ˳˱d²f∕dx²|˳ₓ₌₀ ˎˎ
Text ˎ˳˳(˱a ˳b ¦⠛ᵗ c ˳d˲)˳˳ˎ and some more text.

----

prefix unary operator `→⎴`:
```
\ˎ\ˎ f: x →⎴{‹arrow map›} ˽i x² \ˎ\ˎ
```
ˎˎ f: x →⎴{‹arrow map›} ˽i x² ˎˎ
center binary operator `⎴`:
```
\ˎ\ˎ f: x → ⎴‹arrow map› ˽i x² \ˎ\ˎ
```
ˎˎ f: x → ⎴‹arrow map› ˽i x² ˎˎ
bug because styles also implemented as prefix unary operators (but by design styles should have priority!):
```
\ˎ\ˎ f: x →⎴‹arrow map› ˽i x² \ˎ\ˎ
```
ˎˎ f: x →⎴‹arrow map› ˽i x² ˎˎ
