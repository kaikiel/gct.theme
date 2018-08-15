from plone.app.layout.viewlets.common import FooterViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from datetime import date
from plone import api
from gct.content.browser.configlet import IDict
from gct.content.browser.base_inform_configlet import IInform
import ast
import urllib


class FooterViewlet(FooterViewlet):
    def update(self):
        super(FooterViewlet, self).update()
        self.year = date.today().year
        categoryDict = ast.literal_eval(api.portal.get_registry_record('dict', interface=IDict))
        abs_url = api.portal.get().absolute_url()
        catList = {}
        subList = {}
        count = 0

        productBrains = api.content.find(path="gct/products", portal_type="Product")
        data = {}
        for item in productBrains:
            category = item.p_category
            subject = item.p_subject
            if len(catList) <= 8:
                queryStr = urllib.urlencode({'p_category' : category})
                catList.update({category: '{}/products?{}'.format(abs_url, queryStr) })
            if len(subList) <= 8:
                subName = '{} {}'.format(subject, category)
                queryStr = urllib.urlencode({'p_category' : category, 'p_subject' : subject})
                subList.update({subName: '{}/products?{}'.format(abs_url, queryStr) })

        fileBrains = api.content.find(path='gct/file_container', portal_type="File", sort_limit=8)

        self.email = api.portal.get_registry_record('email', interface=IInform, default='')
	self.address = api.portal.get_registry_record('address', interface=IInform, default='').replace('\r\n', '<br>')
	self.cellphone = api.portal.get_registry_record('cellphone', interface=IInform, default='')
        self.fax = api.portal.get_registry_record('fax', interface=IInform, default='')

        self.fileBrains = fileBrains
        self.catList = catList
        self.subList = subList

