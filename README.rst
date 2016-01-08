python-deansi: Turns coloured console output into the equivalent html
=====================================================================

Features
--------

-  You can use it as module or as a command line tool.
-  Supports most ‘m’ codes (colors and attributes).
-  The apperance can be customized using styles in a very convenient and
   powerful way.

   -  ANSI attributes are mapped to stylable HTML classes
      (``ansi_yellow``, ``ansi_bright``...)
   -  Text sequences with the same set of ANSI attributes are enclosed
      in a single ``span`` with those classes activated.
   -  You can define styles for a class or for a certain combination of
      classes
   -  You can define the style depending on the enclosing container so
      that different styles can coexist in a single document.

-  It is test driven developed and back2back tested, so it is quite
   reliable, and in the long term features can be extended being quite
   sure we are not breaking existing functionality.

Usage as module
---------------

-  ``deansi.styleSheet()``: returns the default stylesheet for the ANSI
   classes you can customize.
-  ``deansi.deansi(consoleText)``: returns the HTML conversion

The following example use them to build a simple console look of the
output:

.. code:: python

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

Customizing stylesheets
~~~~~~~~~~~~~~~~~~~~~~~

You can change the colors displayed adding style rules after the default
ones, for example if you want to change the yellow color when the ansi
bright attribute apply, and not to apply bold font (the default) you can
say:

.. code:: css

    .ansi_yellow.ansi_bright { color: #FF7; font-weight: inherit; }

If you want several behaviours in the same html you can use css magic
like that:

.. code:: css

    .my_own_ansi_enviroment .ansi_inverse { font-style: italic; border: none; }

I look forward applying it to TestFarm soon so all the miss-conversions
are fixed.

Usage as commandline tool
-------------------------

``deansi`` can be used as pipe based command line tool.

.. code:: bash

    $ ls --color | deansi.py > ls.html

