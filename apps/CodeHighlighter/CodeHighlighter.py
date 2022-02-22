from pygments import highlight
from pygments import lexers
from pygments.formatters.html import HtmlFormatter
from pygments.styles import get_style_by_name, get_all_styles


class Highlighter():
    """
    A Class to Highlight Source Code
    see https://pygments.org/docs/quickstart/#example
    """
    def __init__(self):
        pass

    def showAllLexer(self):  
        """ will show all available lexers """
        for lexer in lexers.get_all_lexers():
            print(lexer)

    def showAllStyles(self):  
        """ will show all available styles """
        for s in get_all_styles():
            print(s)

    def simpleTest(self):
        code = "INSERT INTO gaestebuch (datum,name,titel,eintrag) VALUES('20010719153145','Christian Felken','Mein Gästebucheintrag','HalloWelt!');"
        lexer = lexers.get_lexer_by_name('SQL')

        selected_style = get_style_by_name('one-dark')
        # see https://pygments.org/docs/formatters/?highlight=inline
        formatter = HtmlFormatter(
            linenos=True, 
            full=False,            # no full html document, just the code 
            style=selected_style,
            noclasses=True,        # use inline CSS
            
            )
        # Highlight
        filename = 'test.html'
        with open(filename, 'w') as f: 
            highlight(code, lexer, formatter, outfile=f)
        
        print("\nOutput: %s" % filename)


if __name__ == "__main__":
    tool = Highlighter()
    print("Lexers ====================================================================")
    tool.showAllLexer()
    print("\n\nStyles ====================================================================")
    tool.showAllStyles()
    tool.simpleTest()
