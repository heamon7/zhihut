# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import leancloud
from leancloud import Object
from leancloud import LeanCloudError

class FirstPipline(object):

    def __init__(self):
        leancloud.init('jlxrio7ls1fdx9oyapnsw7djov681i6jf1omoxiyqcdqm65t', master_key='xxmihbxc73mw06smcjnrqhvcdenam1ahg4hbxsjdqhsdqkty')
        #self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        Question= Object.extend('Question')
        question = Question()
        question.set('answerCount',item['answerCount'])
        question.set('isTopQuestion',item['isTopQuestion'])
        question.set('subTopicName',item['subTopicName'])
        question.set('subTopicHref',item['subTopicHref'])
        question.set('questionTimestamp',item['questionTimestamp'])
        question.set('questionLinkHref',item['questionLinkHref'])
        question.set('questionName',item['questionName'])

        # question.set('',item[''])

        try:
            question.save()
        except LeanCloudError,e:
            print e
        finally:
            return item





        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # return item

class SecondPipline(object):
    def process_item(self, item, spider):
        return item
