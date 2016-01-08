# python-deansi: Turns coloured console output into the equivalent html



## Features

- It can be used either as module or as a command line tool.
- Supports most ‘m’ codes (colors and attributes).
- The apperance can be customized using styles in a very convenient and powerful way.
	- ANSI attributes are mapped to stylable HTML classes (`ansi_yellow`, `ansi_bright`...)
	- Text sequences with the same set of ANSI attributes are enclosed in a single  `span` with those classes activated.
	- You can define styles for a class or for a certain combination of classes
	- You can define the style depending on the enclosing container so that different styles can coexist in a single document.
- It is test driven developed and back2back tested, so it is quite reliable, and in the long term features can be extended being quite sure we are not breaking existing functionality.



## Usage as module


- `deansi.styleSheet()`: returns the default stylesheet for the ANSI classes you can customize.
- `deansi.deansi(consoleText)`: returns the HTML conversion

The following example use them to build a simple console look of the output:

```python
import deansi

html_template = """\
<style>
.ansi_terminal {{ background-color: #222; color: #cfc; }}
{defaultStyle}
</style>
<div class="ansi_terminal">{ansiText}</div>
"""
ansiInput = "\033[31mHello World!!\033[m"

print html_template.format(
    defaultStyle = deansi.styleSheet(),
    ansiText = deansi.deansi(ansiInput),
    )
```

### Customizing stylesheets

The default stylesheet looks like this:

```css
.ansi_terminal { background-color: #222; color: #cfc; }
.ansi_terminal { white-space: pre; font-family: monospace; }
.ansi_black { color: black; }
.ansi_red { color: darkred; }
.ansi_green { color: darkgreen; }
.ansi_yellow { color: orange; }
.ansi_blue { color: darkblue; }
.ansi_magenta { color: purple; }
.ansi_cyan { color: darkcyan; }
.ansi_white { color: lightgray; }
.ansi_bright.ansi_black { color: gray; }
.ansi_bright.ansi_red { color: red; }
.ansi_bright.ansi_green { color: green; }
.ansi_bright.ansi_yellow { color: yellow; }
.ansi_bright.ansi_blue { color: blue; }
.ansi_bright.ansi_magenta { color: magenta; }
.ansi_bright.ansi_cyan { color: cyan; }
.ansi_bright.ansi_white { color: white; }
.ansi_bgblack { background-color: black; }
.ansi_bgred { background-color: red; }
.ansi_bggreen { background-color: green; }
.ansi_bgyellow { background-color: yellow; }
.ansi_bgblue { background-color: blue; }
.ansi_bgmagenta { background-color: magenta; }
.ansi_bgcyan { background-color: cyan; }
.ansi_bgwhite { background-color: white; }
.ansi_bright { font-weight: bold; }
.ansi_faint { opacity: .5; }
.ansi_italic { font-style: italic; }
.ansi_underscore { text-decoration: underline; }
.ansi_blink { text-decoration: blink; }
.ansi_reverse { border: 1pt solid; }
.ansi_hide { opacity: 0; }
.ansi_strike { text-decoration: line-through; }
```


Because of the cascading behaviour of CSS whichever style rules after the default ones, will override those ones.
For example if you want to change the yellow color when the ansi bright attribute apply, instead of applying bold font you can say:

```css
.ansi_yellow.ansi_bright { color: #FF7; font-weight: inherit; }
```

If you want several behaviours in the same html you can use css magic like that:

```css
.my_own_ansi_enviroment .ansi_inverse { font-style: italic; border: none; }
```


## Usage as commandline tool

`deansi` can be used as pipe based command line tool.

```bash
$ ls --color | deansi.py > ls.html
```


