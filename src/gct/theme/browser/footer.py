from plone.app.layout.viewlets.common import FooterViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from datetime import date
from plone import api
from gct.content.browser.configlet import IDict
from gct.content.browser.base_inform_configlet import IInform
import ast


class FooterViewlet(FooterViewlet):
    def update(self):
        super(FooterViewlet, self).update()
        self.year = date.today().year
        categoryDict = ast.literal_eval(api.portal.get_registry_record('dict', interface=IDict))
        abs_url = api.portal.get().absolute_url()
        catList = []
        subList = {}
        count = 0
        for category in sorted(categoryDict):
            catList.append(category)
            for subject in categoryDict[category][1]:
                subName = '{} {}'.format(subject, category)
	        if count<8:
                    count+=1
                    subList[subName] = '%s/products?p_category=%s&p_subject=%s' %(abs_url, category, subject)
        fileBrains = api.content.find(path='gct/file_container', portal_type="File", sort_limit=8)

        self.email = api.portal.get_registry_record('email', interface=IInform, default='')
	self.address = api.portal.get_registry_record('address', interface=IInform, default='')
	self.cellphone = api.portal.get_registry_record('cellphone', interface=IInform, default='')
        self.fax = api.portal.get_registry_record('fax', interface=IInform, default='')

        self.fileBrains = fileBrains
        self.catList = catList
        self.subList = subList

