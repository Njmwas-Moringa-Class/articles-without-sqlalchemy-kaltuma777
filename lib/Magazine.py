
from Article import Article

class Magazine:
    _all_magazines = []  # List to store all magazines

    def _init_(self, name, category):
        """
        Initialize a magazine with a name and category.
        
        Args:
            name (str): The name of the magazine.
            category (str): The category of the magazine.
        """
        self._name = name
        self._category = category
        self._articles = []  # List to store articles of the magazine
        Magazine._all_magazines.append(self)  # Add the magazine to the list of all magazines

    def name(self):
        """
        Get the name of the magazine.
        
        Returns:
            str: The name of the magazine.
        """
        return self._name

    def category(self):
        """
        Get the category of the magazine.
        
        Returns:
            str: The category of the magazine.
        """
        return self._category

    @classmethod
    def all(cls):
        """
        Get all magazines.
        
        Returns:
            list: List of all magazines.
        """
        return Magazine._all_magazines

    def contributors(self):
        """
        Get the contributors (authors) of the magazine.
        
        Returns:
            list: List of contributors (authors) of the magazine.
        """
        return list(set(article.author() for article in self._articles))

    def add_article(self, author, title):
        """
        Add an article to the magazine.
        
        Args:
            author (Author): The author of the article.
            title (str): The title of the article.
        
        Returns:
            Article: The added article.
        """
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def find_by_name(cls, name):
        """
        Find a magazine by its name.
        
        Args:
            name (str): The name of the magazine to find.
        
        Returns:
            Magazine or None: The found magazine or None if not found.
        """
        return next((magazine for magazine in cls._all_magazines if magazine.name() == name), None)

    @classmethod
    def article_titles(cls):
        """
        Get all article titles from all magazines.
        
        Returns:
            list: List of all article titles.
        """
        return [article.title() for magazine in cls._all_magazines for article in magazine._articles]

    @classmethod
    def contributing_authors(cls):
        """
        Get authors who contributed to more than 2 articles across all magazines.
        
        Returns:
            list: List of contributing authors.
        """
        return [author for magazine in cls._all_magazines for author in magazine.contributors() if len(author.articles()) > 2]
