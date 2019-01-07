import click
from bluelog import app

@app.cli.command()
def say_hello():
    click.echo("hello")
