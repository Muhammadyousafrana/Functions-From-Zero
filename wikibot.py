import click
from my_lib.bot import scrape


@click.command()
@click.option("--name", default="Microsoft", help="web page we want to scape")
@click.option("--length", default=1, type=int, help="Number of sentences in summary")
def cli(name, length):
    result = scrape(name=name, length=length)
    click.echo(click.style(f"{result}", fg="green"))


if __name__ == "__main__":
    cli()
