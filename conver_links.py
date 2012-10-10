# coding: utf-8
import sqlite3
import pymongo

con = sqlite3.connect('lurkingideas.db')
con.row_factory = sqlite3.Row
cursor = con.cursor()
mocon = pymongo.Connection()

for category_id, category in enumerate(['The porn of now', 'Sick and tired'], 1):
    cursor.execute('select * from links_link where category_id = %d order by ordering' % category_id)
    links = []
    for link in cursor:
        links.append({
            'name': link['name'],
            'description': link['description'],
            'url': link['url'],
        })
    mocon.lurkingideas.links.insert({
        'category': category,
        'links': links,
    })
