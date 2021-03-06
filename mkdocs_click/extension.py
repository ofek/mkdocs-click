import re
from typing import List

from markdown import Markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

from mkdocs_click.parser import generate_command_docs


class ClickProcessor(Preprocessor):

    PATTERN = re.compile(r"^:::click module=([:a-zA-Z0-9_.]+):([:a-zA-Z0-9_.]+)::: *$")

    def run(self, lines: List[str]) -> List[str]:
        new_lines = []
        for line in lines:
            m = self.PATTERN.search(line)
            if m:
                path, command = m.groups()
                new_lines.extend(generate_command_docs(path, command))
            else:
                new_lines.append(line)

        return new_lines


class MKClickExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        md.registerExtension(self)
        processor = ClickProcessor(md.parser)
        md.preprocessors.register(processor, "mk_click", 141)


def makeExtension() -> Extension:
    return MKClickExtension()
