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

# @click.command()
# @click.argument("number1", type=int)
# @click.argument("number2", type=int)
# @click.argument("number3", type=int)
# @click.argument("method", default="add")
# def operators(number1, number2, number3, method):
#     if method == "add":
#         result = number1 + number2 + number3
#         if result < 255:
#             click.echo(result)
#             click.echo("The result is lower than 255")
#         else:
#             click.echo("The result is more than 255")
#




