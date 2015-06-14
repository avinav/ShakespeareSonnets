'''
Created on Apr 27, 2015

@author: avinav
'''



class Document:
    '''
    classdocs
    '''
    counter = -1
    def __init__(self, name, term_list):
        '''
        Constructor
        '''
        Document.counter += 1
        self.id = Document.counter
        self.name = name
        self.term_list = term_list