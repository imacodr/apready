import os
import click

from colored import Fore, Back, Style

from apready.files import readlines, writelines, downloads_path
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


    data = readlines(input)
    new = scrap(data, ["#"])
    print(new)

    for line in new:
        print(line)

    file_name = os.path.basename(input)

    copy_title_split = file_name.split(".")

    writelines(downloads_path + "/" + copy_title_split[0] + "-copy." + copy_title_split[1], new)
    
    click.echo("")
    click.echo(Fore.GREEN + "☑")
    
