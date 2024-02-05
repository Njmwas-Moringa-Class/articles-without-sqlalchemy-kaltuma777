#!/usr/bin/env python3
import os
import sys
import ipdb

sys.path.append('../lib') 

print(os.getcwd())
print(sys.path)
print(os.listdir())

from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
    # WRITE YOUR TEST CODE HERE

    author1 = Author("Oprah Winfrey")
    author2 = Author("Tyler Perry")

    ipdb.set_trace()

    magazine1 = Magazine("Vogue", "Gucci")
    magazine2 = Magazine("Christina Herera", "Giovani")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "Dress Fashionbly")
    article2 = author2.add_article(magazine1, "How to be Great")
    article3 = author1.add_article(magazine2, "The Most Expensive Gift")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")

    # DO NOT REMOVE THIS
    ipdb.set_trace()

    # DO NOT REMOVE THIS
    ipdb.set_trace()
