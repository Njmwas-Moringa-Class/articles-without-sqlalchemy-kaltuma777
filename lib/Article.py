
class Article:
    _all_articles = []  # List to store all articles
    
    def __init__(self, author, magazine, title):
        """
        Initialize an article with an author, magazine, and title.
        
        Args:
            author (Author): The author of the article.
            magazine (str): The magazine where the article is published.
            title (str): The title of the article.
        """
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all_articles.append(self)  # Add the article to the list of all articles
    
    def title(self):
        """
        Get the title of the article.
        
        Returns:
            str: The title of the article.
        """
        return self._title
    
    def author(self):
        """
        Get the author of the article.
        
        Returns:
            Author: The author of the article.
        """
        return self._author
    
    def magazine(self):
        """
        Get the magazine where the article is published.
        
        Returns:
            str: The magazine where the article is published.
        """
        return self._magazine
    
    @classmethod
    def all(cls):
        """
        Get all articles.
        
        Returns:
            list: List of all articles.
        """
        return cls._all_articles
