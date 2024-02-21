# import ipdb

class Article:
    all = []  # List to store all articles

    def __init__(self, author, magazine, title):
        """
        Initialize an article with an author, magazine, and title.
        
        Args:
            author (str): The author of the article.
            magazine (str): The magazine where the article is published.
            title (str): The title of the article.
        """
        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    def get_author(self):
        return self._author
    
    def get_magazine(self):
        return self._magazine
    
    def get_title(self):
        return self._title

    author = property(get_author)
    magazine = property(get_magazine)
    title = property(get_title)

if __name__ == "__main__":
    
    first_article = Article(author="Obama", magazine="Embraced", title="Leadership")
    second_article = Article(author="Fiodor", magazine="Fema", title="Energy")
    third_article = Article(author="Sheldon", magazine="Defacto", title="Lies")
    fourth_article = Article(author="Obama", magazine="Physics", title="Poles")

    # Article.get_article_by()

    # ipdb.set_trace()
