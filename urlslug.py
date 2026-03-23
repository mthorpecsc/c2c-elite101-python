import string
no_punct = str.maketrans('','', string.punctuation)
container = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #container to check if the title contains at least one letter or number

def url_slug(title):
    url_slug = title.replace(" ", "-") #replaces spaces with hyphens
    if "--" in url_slug: #if there are double hyphens, replace with a single hyphen
        new_url_slug = url_slug.replace("--", "-")
        print(new_url_slug)
    else:
        print(url_slug) #if not past the url slug as normal

def main():
    while True:
        title = input("Enter a phrase or title: ").lower().translate(no_punct) #takes away punctuation and lowercases title
        if len(title) == 0: #empty inputs edgecase
            print("Your phrase or title must contain at least one letter or number. Please try again. ")
            continue #skips the loop and prompts user again
        for char in title: #checks if each character in title is in the container
            if char in container:
                url_slug(title) #if so the urlslug function is called,
                break
            else: #if not the user is prompted to try again
                print("Your phrase or title must contain at least one letter or number. Please try again. ")
                break
        break


main()
