import click
import requests
from bs4 import BeautifulSoup

# Using the click module for interacting with the CLI

@click.command()
@click.option("--user_entry", help="Enter your name", type=str)
# This will prompt the user for an entry in string format 

def user_input(user_entry):
    html = requests.get("http://en.wikipedia.org/wiki/" + user_entry)
    # This will then concatenate the user entry with the url 
    
    soup = BeautifulSoup(html.text, "html.parser")
    image_links = soup.findAll("a", {"class": "image"})
    for image in image_links:
        print(image.img['src'])
        # This will now print out all the image taged urls 

if __name__ == "__main__":
    user_input()

