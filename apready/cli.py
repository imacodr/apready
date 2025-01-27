import os
import click

from colorama import Fore, Back, Style

from apready.files import readlines, writelines, downloads_path
from apready.scraper import scrap

@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """🐿️ Good to Go - Check if your AP test is ready for submission, scrape comments and help document."""

@cli.command()
@click.option("-i", "--input", prompt="Input a path to the script", help="Script to scrape", type=str)
@click.option("-t", "--type", prompt="What type of file?", help="Type of file", type=click.Choice(["python", "javascript", "java"]))
@click.pass_context
def scrape(ctx: click.Context, input: str, type: click.Choice):
    """scrape comments off your file and generate a copy without it"""


    data = readlines(input)
    new = scrap(data, ["#"], ['"""'])

    for line in new:
        print(line)

    file_name = os.path.basename(input)

    copy_title_split = file_name.split(".")

    file_name = downloads_path + "/" + copy_title_split[0] + "-good." + copy_title_split[1]

    writelines(file_name, new)
    
    click.echo("")
    click.echo(Fore.GREEN + "☑ Successfully scraped file!")
    click.echo(Fore.RESET + "It can be found in " + Fore.BLUE + file_name)
    click.echo(Fore.RESET + "")
    
