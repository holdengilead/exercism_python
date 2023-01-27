class Markdown:
    def __init__(self, text: str) -> None:
        self.lines = text.split("\n")
        self.markdown_text = ""

    def convert(self) -> str:
        for num_line, line in enumerate(self.lines):
            self.parse_line(num_line, line)
        if self.lines[-1][0] == "*":
            self.markdown_text += "</ul>"
        return self.markdown_text

    def parse_line(self, num_line, line: str):
        if line.startswith("*"):
            if num_line == 0 or self.lines[num_line - 1][0] != "*":
                self.markdown_text += "<ul>"
            self.markdown_text += f"<li>{Markdown.get_style(Markdown.get_style(line[2:], '__', 'strong'), '_','em')}</li>"
            return
        if num_line > 0 and self.lines[num_line - 1][0] == "*":
            self.markdown_text += "</ul>"
        if line.startswith("#") and line.index(" ") < 7:
            pos = line.index(" ")
            self.markdown_text += f"<h{pos}>{line[pos+1:]}</h{pos}>"
            return
        self.markdown_text += f"<p>{Markdown.get_style(Markdown.get_style(line, '__', 'strong'), '_','em')}</p>"

    @staticmethod
    def get_style(line: str, mark: str, replace: str):
        try:
            while True:
                start = line.index(mark)
                closing = line.index(mark, start + len(mark))
                line = "{}<{}>{}</{}>{}".format(
                    line[:start],
                    replace,
                    line[start + len(mark) : closing],
                    replace,
                    line[closing + len(mark) :],
                )
        except ValueError:
            return line


def parse(markdown):
    m = Markdown(markdown)
    return m.convert()
