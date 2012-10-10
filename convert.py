# coding: utf-8
import sqlite3
import pymongo

con = sqlite3.connect('lurkingideas.db')
con.row_factory = sqlite3.Row
cursor = con.cursor()

cursor.execute('select * from blog_post')

mocon = pymongo.Connection()
for post in cursor:
    mocon.lurkingideas.posts.insert({
        'slug': post['slug'],
        'title': post['title'],
        'summary': post['about'],
        'content': post['content'],
        'created_date': post['created'],
    })
