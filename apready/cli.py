import os
import click

from apready.files import readlines
from apready.scraper import scrap

@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """✅ AP Ready - Check if your AP test is ready for submission, scrape comments and help document."""

@cli.command()
@click.option("-i", "--input", prompt="Input a path to the script", help="Script to scrape", type=str)
@click.option("-t", "--type", prompt="What type of file?", help="Type of file", type=click.Choice(["python", "javascript", "java"]))
@click.pass_context
def scrape(ctx: click.Context, input: str, type: click.Choice):
    """scrape comments off your file and generate a copy without it"""
    
    

    print(input)
    data = readlines(input)
    print(data)
    scrap(data, ["#"])
