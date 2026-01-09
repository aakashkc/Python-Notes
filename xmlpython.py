import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""
    #   self.content= " "

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         title = attributes["title"]
         
         print ("Title:", title)

   # Call when an elements ends
def endElement(self, tag):
    if self.CurrentData == "type":
        print ("Type:", self.type)
    elif self.CurrentData == "format":
        print ("Format:", self.format)
    elif self.CurrentData == "year":
        print ("Year:", self.year)
    elif self.CurrentData == "rating":
        print ("Rating:", self.rating)
    elif self.CurrentData == "stars":
        print ("Stars:", self.stars)

    elif self.CurrentData == "description":
        self.description = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("python.xml")
