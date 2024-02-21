# import ipdb
from Article import Article
# from Author import Author


class Magazine:

    all = []

    def __init__(self, name, category):
        """
        Initialize a magazine with a name and category.
        
        Args:
            name (str): The name of the magazine.
            category (str): The category of the magazine.
        """
        self.name = name
        self.category = category
        self.contributors = []
    
        Magazine.all.append(self)

        # self.contributing_authors()

        # for article in Article.all:
        #     if article.magazine == self.name and article.author not in self.contributors:
        #         self.contributors.append(article)

        for article in Article.all:
            if article.magazine == self.name:
                from Author import Author
                #Find the author instance with the name matching the article's author
                author_instance = next((author for author in Author.all if author.name == article.author), None)
                if author_instance and author_instance not in self.contributors:
                    self.contributors.append(author_instance)
            
    
    @classmethod
    def find_by_name(cls, name):
        """
        Find a magazine by its name.
        
        Args:
            name (str): The name of the magazine to find.
        
        Returns:
            Magazine or None: The found magazine or None if not found.
        """
        return next((magazine for magazine in cls.all if magazine.name == name), None)

    @classmethod
    def article_titles(cls,magazine_name):
        """
        Get all article titles from a specific magazine.
        
        Args:
            magazine_name (str): The name of the magazine.
        
        Returns:
            list: List of all article titles in the specified magazine.
        """
        return [article.title for article in Article.all if article.magazine == magazine_name]

    def contributing_authors(self):
        """
        Get authors who contributed to the magazine.
        
        Returns:
            list: List of authors who contributed to the magazine.
        """
        return [author for author in self.contributors if len([article for article in author.articles if article.magazine == self.name]) > 2]
    
        
if __name__ == "__main__":

    # Create instances of Author
    from Author import Author
    author1 = Author("Obama")
    author2 = Author("Fiodor")
    author3 = Author("Sheldon")

    

    #instatiating Article
    article1 = Article(author="Obama", magazine="Embraced", title="Leadership")
    article2 = Article(author="Fiodor", magazine="Fema", title="Energy")
    article3 = Article(author="Sheldon", magazine="Defacto", title="Lies")
    article4 = Article(author="Obama", magazine="Embraced", title="Poles")
    article5 = Article(author="Shakespiere", magazine="Fema", title="Lost")
    article5 = Article(author="Thiongo", magazine="Kumiira", title="Nigute")

    #instatiating Magazine
    magazine1 =  Magazine(name="Embraced", category="Politics")
    magazine2 = Magazine(name="Fema", category="news")
    magazine3 = Magazine(name="Defacto", category="all")
    magazine4 = Magazine(name="Kumiira", category="sport")
    


    # Test the contributors method
    print("Contributors for", magazine1.name, ":", [author.name for author in magazine1.contributors])
    print("Contributors for", magazine2.name, ":", [author.name for author in magazine2.contributors])
    print("Contributors for", magazine3.name, ":", [author.name for author in magazine3.contributors])

    # Test the contributing_authors method
    print("Contributing authors for", magazine1.name, ":", [author.name for author in magazine1.contributing_authors()])
    print("Contributing authors for", magazine2.name, ":", [author.name for author in magazine2.contributing_authors()])
    print("Contributing authors for", magazine3.name, ":", [author.name for author in magazine3.contributing_authors()])



    #Returns an list strings of the titles of all articles written for that magazine
    print(Magazine.article_titles("Embraced"))

    # Test the find_by_name method
    print(Magazine.find_by_name("Embraced"))


    
    # ipdb.set_trace()
