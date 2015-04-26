from tsl_news.models import Section, Author, Article, WaitingArticle, User


def article_has_properties():

    # get each article
    for article in Article.objects.all():
        # get the article
        article = Article.objects.get(id=article.id)
        # get headline
        headline = article.headline
        # make sure it isn't empty
        if headline == '':
            print "(%d) %s does not have a valid title" % (article.id, article.headline[:15])
        # get the authors
        authors = list(article.authors.all())
        if len(authors) == 0:
            print "(%d) %s does not have a valid author" % (article.id, article.headline[:15])
        # get the section
        section = article.section.name
        section_list = []
        for sect in Section.objects.all():
            section_temp = Section.objects.get(id=sect.id)
            section_list.append(section_temp.name)
        if section not in section_list:
            print "(%d) %s does not have a valid section" % (article.id, article.headline[:15])
        # get the date
        date = article.pub_date.strftime("%B %d, %Y")
        if date == '':
            print "(%d) %s is missing a date" % (article.id, article.headline[:15])
        # check body for proper spacing
        article_body = article.article_body
        if "\r" in article_body:
            print "(%d) %s has a carraige return" % (article.id, article.headline[:15])
        if "\n\n\n" in article_body:
            print "(%d) %s has a triple space" % (article.id, article.headline[:15])
        if " \n " in article_body:
            print "(%d) %s has a single space" % (article.id, article.headline[:15])

