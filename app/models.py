class News:
    
    def __init__(self,source,title, content, description, urlToImage, publishedAt,url,author):
        self.source = source
        self.title = title
        self.content = content
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url
        self.author = author
        
        
class Source:
    
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country =country
        