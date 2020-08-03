import click
import requests
from bs4 import BeautifulSoup


@click.command()
@click.option("--user_entry", help="Enter your name", type=str)
def user_input(user_entry):
    html = requests.get("http://en.wikipedia.org/wiki/" + user_entry)

    soup = BeautifulSoup(html.text, "html.parser")
    image_links = soup.findAll("a", {"class": "image"})
    for image in image_links:
        print(image.img['src'])


if __name__ == "__main__":
    user_input()

