"""Console script for lorem_text."""
import sys
import lorem_text
import click
from lorem_text import sentence

@click.command()
@click.option('--words', type=int, help="Returns lorem ipsum words")
@click.option('--s', is_flag=True, help="Returns lorem ipsum sentence")
def main(words,  s):
    """Console script for lorem_text."""
    if words:
        words = int(words)
        click.echo(lorem_text.words(words))

    # Returns a lorem ipsum sentence
    elif s:
        click.echo(lorem_text.sentence())

    # Returns a lorem ipsum paragraph by default
    else:
        click.echo(lorem_text.paragraph())


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
