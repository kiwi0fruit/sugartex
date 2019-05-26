The SugarTeX [**examples PDF**](examples.pdf?raw=true).

Was created via this [Markdown source](examples.md?raw=true). You can find output LaTeX source in [this document](examples.md.md).

### Using in Jupyter

```py
import IPython.display as ds
import math
import sugartex as st

ds.Markdown(st.stex(f'''

Some **dynamic** Markdown text with SugarTeX formula: ˎα^˱{math.pi:1.4f}˲ˎ.

ˎˎ
˱∇ × [ ⃗B] - 1∕c ∂[ ⃗E]∕∂t ˳= 4π∕c [ ⃗j] ¦#
               ∇ ⋅ [ ⃗E]\ ˳= 4πρ       ¦
 ∇ × [ ⃗E] + 1∕c ∂[ ⃗B]∕∂t ˳= [ ⃗0]      ¦
               ∇ ⋅ [ ⃗B]\ ˳= 0         ˲
ˎˎ


where ˎ[ ⃗B], [ ⃗E], [ ⃗j]: ℝ⁴ → ℝ³ˎ – vector functions of the form
ˎ(t,x,y,z) ↦ [ ⃗f](t,x,y,z), [ ⃗f] = (f_˹x˺, f_˹y˺, f_˹z˺)ˎ.
'''))
```
