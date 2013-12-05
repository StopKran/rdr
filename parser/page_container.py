__author__ = 'stopkran'


class page_container:

    name = ""
    site_name = ""
    url = ""
    tags = []
    content = ""

    def __init__(self):
        pass

    def __str__(self):
        return self.name + "/n" + self.content

    def generate_json(self):
        pass

    def print_content(self):
        print self.name
        print self.url
        print self.site_name
        print self.content
        print self.tags