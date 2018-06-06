from plone.app.layout.viewlets.common import FooterViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from datetime import date
from plone import api

class FooterViewlet(FooterViewlet):
    def update(self):
        super(FooterViewlet, self).update()
        self.year = date.today().year
        catList = []
        subList = []
        abs_url = api.portal.get().absolute_url()
        productBrains = api.content.find(path='gct/products', portal_type='Product')
        for item in productBrains:
            obj = item.getObject()
            category = obj.category
            subject = obj.subject
            name = '%s %s' %(subject, category)
            if category and category not in catList:
                catUrl = '%s?p_category=%s' %(abs_url, category)
                catList.append( [category, catUrl])
            if subject and subject not in subList:
                subUrl = '%s?p_category=%s&p_subject=%s' %(abs_url, category, subject)
                subList.append([name, subUrl])
 
        fileBrains = api.content.find(path='gct/file_container', portal_type="File", sort_limit=8)

        self.fileBrains = fileBrains
        self.catList = catList
        self.subList = subList

