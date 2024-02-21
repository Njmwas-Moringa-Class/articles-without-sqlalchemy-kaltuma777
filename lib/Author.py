# import ipdb

from Magazine import Magazine
from Article import Article

class Author:
    all = []  # Class variable to keep track of all instances

    def __init__(self, name):
        """
        Initialize an author with a name.
        
        Args:
            name (str): The name of the author.
        """
        self._name = name
        self.articles = []
        self.magazines = []

        Author.all.append(self)  # Append the new instance to the 'all' class variable

        for article in Article.all:
            if article.author == self.name:
                self.articles.append(article)
        for magazine in Magazine.all:
            for article in self.articles:
                if magazine.name == article.magazine and magazine not in self.magazines:
                    self.magazines.append(magazine)

    def get_name(self):
        """
        Get the name of the author.
        
        Returns:
            str: The name of the author.
        """
        return self._name
    
    def articles(self):
        """
        Get the articles written by the author.
        
        Returns:
            list: List of articles written by the author.
        """
        return self.articles

    def magazines(self):
        """
        Get the magazines the author has contributed to.
        
        Returns:
            list: List of magazines the author has contributed to.
        """
        return self.magazines
    
    def add_article(self,magazine, title):
        """
        Add an article written by the author to a magazine.
        
        Args:
            magazine (Magazine): The magazine where the article is published.
            title (str): The title of the article.
        """
        new_article = Article(self._name, magazine.name, title)
        self.articles.append(new_article)

        if magazine not in self.magazines:
            self.magazines.append(magazine)

    def topic_areas(self):
        """
        Get the topic areas the author has contributed to.
        
        Returns:
            list: List of topic areas the author has contributed to.
        """
        return list(set([magazine.category for magazine in self.magazines]))
    
    name = property(get_name)


if __name__ == "__main__":

    #instatiating Article

    first_article = Article(author="Obama", magazine="Embraced", title="Leadership")
    second_article = Article(author="Fiodor", magazine="Fema", title="Energy")
    third_article = Article(author="Sheldon", magazine="Defacto", title="Lies")
    fourth_article = Article(author="Obama", magazine="Physics", title="Poles")
    #instatiating Magazine

    first_magazine = Magazine(name="Embraced", category="Politics")
    second_magazine = Magazine(name="Fema", category="news")
    third_magazine = Magazine(name="Defacto", category="all")
    fourth_magazine = Magazine(name="Physics", category="sport")
    
    first_author = Author("Obama")

    # Returns an list of Articles instances the author has written
    first_author.articles # should return 2 Articles instances of Kapinga

    # Returns a unique list of Magazine instances for which the author has contributed to
    first_author.magazines # should return 2 Magazine instances for Kapinga

    # Given a  magazine(as Magazine instance) and a title (as a string), creates a new Article instance and associates it with that author and that magazine
    author = Author("Obama")
    magazine = Magazine(name="Living", category="lifestyle")
        
    author.add_article(magazine, "Vogue")   
        # Check if the new article was added
    print("Here is the new added article instance to the author\n")
    print(author.articles)   # This should print a list of instances containing the new article
    print("Here all articles within the Article class including the lastly added\n")
    for articles in Article.all: print(articles.title)   
        # Check if the magazine was added to the author's magazines
    print("Here is the new added magazine instance\n")
    print(author.magazines)  # This should print a list of instances containing the magazine
    print("Here all magazine within the Magazine class inclding the lastly added\n")
    for magazine in Magazine.all: print(magazine.name)

    # Returns a unique list of strings with the categories of the magazines the author has contributed to
    print("Here is the unique list of magazine categories the author has contributed to\n")
    print(first_author.topic_areas())
    


    
    # ipdb.set_trace()
