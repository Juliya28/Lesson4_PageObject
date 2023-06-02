import requests
import logging


def gett_my(token):
    logging.debug('Open posts page')
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})#, 'page': 17, params={'owner': 'notMe'
    if g:
        listcont = [i['content'] for i in g.json()['data']] 
        return listcont
    else:
        logging.error('Страница с постами не открылась')
        
 
def gett_notmy_posts(token):
    logging.debug('Open posts page')
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    if g:
        listcont = [i['content'] for i in g.json()['data']] 
        return listcont
    else:
        logging.error('Страница с постами не открылась')   
    
    
def newpost(token):
    logging.debug('Create new post')
    a = requests.post('https://test-stand.gb.ru/getway/posts', headers={'X-Auth-Token': token}, 
                      data={ 'title':'test title',
            'description':'test description',
            'content': 'test content'} )
    if a:
        return a.json()
    else:
        logging.error('Пост не создан')



def findpost(token):
    logging.debug('Find created post')
    b = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    if b: 
        listmy = [i['description'] for i in b.json()['data']]
        return listmy
    else:
        logging.error('Пост не найден')


def test_2(login, text1):
    assert text1 in gett_notmy_posts(login)
    
    
def test_3(login, text2):
    assert text2 in gett_my(login)
    
    
    
