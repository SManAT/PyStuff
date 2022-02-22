https://clay-atlas.com/us/blog/2020/03/05/python-english-tutorial-package-pygments-highlight-code/


from pygments import highlight
from pygments import lexers
from pygments.formatters.html import HtmlFormatter
from pygments.styles import get_style_by_name


class Highlighter():
  """ A Class to Highlight Source Code """
  # Settings
  code = "print('Hello World!')"
  lexer = lexers.get_lexer_by_name('python')
  style = get_style_by_name('native')
  formatter = HtmlFormatter(full=True, style=style)

  for lexer in lexers.get_all_lexers():
      print(lexer)

  # Style
  for s in get_all_styles():
      print(s)

  # Highlight
  with open('test.html', 'w') as f:
      highlight(code, lexer, formatter, outfile=f)

if __name__ == "__main__":
    tool = IMage2Base64Converter()