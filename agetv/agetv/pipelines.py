# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import pymysql as pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AgetvPipeline:
    db = None
    cursor = None

    def open_spider(self, spider):
        self.db = pymysql.connect(host='localhost', database='arime', user='root', password='root')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        logging.info('正在执行sql')
        v_title = item.get('v_title')
        v_address = item.get('v_address')
        v_arime_type = item.get('v_arime_type')
        v_original_name = item.get('v_original_name')
        v_other_name = item.get('v_other_name')
        v_author = item.get('v_author')
        v_production = item.get('v_production')
        v_first_time = item.get('v_first_time')
        v_play_status = item.get('v_play_status')
        v_plot_type = item.get('v_plot_type')
        v_label = item.get('v_label')
        v_original_web = item.get('v_original_web')
        v_home = item.get('v_home')
        v_urls = item.get('v_urls')

        self.cursor.execute('ALTER TABLE arime AUTO_INCREMENT = 0')
        self.cursor.execute('ALTER TABLE arime_urls AUTO_INCREMENT = 0')
        arime_id = self.sql_content(v_title, v_address, v_arime_type, v_original_name, v_other_name, v_author,
                                    v_production,
                                    v_first_time, v_play_status, v_plot_type, v_label, v_original_web, v_home)
        self.db.commit()
        self.sql_urls(urls=v_urls, arime_id=arime_id)
        self.db.commit()
        self.cursor.execute(f"UPDATE arime SET v_urls = {arime_id} WHERE v_id = {arime_id}")
        self.db.commit()
        return item

    def sql_content(self, v_title, v_address, v_arime_type, v_original_name, v_other_name, v_author, v_production,
                    v_first_time, v_play_status, v_polt_type, v_label, v_original_web, v_home):
        try:
            sql = 'INSERT INTO arime(v_title, v_address ,v_arime_type, v_original_name, v_other_name, v_author, \
                v_production, v_first_time,v_play_status,v_polt_type,v_label,v_original_web,v_home) \
                VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                v_title, v_address, v_arime_type, v_original_name, v_other_name, v_author, v_production, v_first_time,
                v_play_status, v_polt_type, v_label, v_original_web, v_home)
            self.cursor.execute(sql)
            logging.info('数据插入正常')
            return self.cursor.lastrowid
        except Exception as e:
            self.db.rollback()
            logging.error(e.args)

    def sql_urls(self, urls: list, arime_id):
        try:
            a = 0
            last_index = -1
            for url in urls:
                b = len(url)
                if last_index == -1:
                    a = b
                    last_index = last_index + 1
                else:
                    if b > a:
                        for i in range(b - a):
                            urls[last_index].append('')
                        last_index = last_index + 1
                        a = b
                    elif b < a:
                        for i in range(a - b):
                            url.append('')
                        last_index = last_index + 1
            print(len(urls[0]), len(urls[1]), len(urls[2]), len(urls[3]))
            for i in range(0, a):
                self.cursor.execute(
                    'INSERT INTO arime_urls(url1, url2, url3, url4,arime_id) VALUES ("%s","%s","%s","%s","%s")' % (
                        urls[0][i], urls[1][i], urls[2][i], urls[3][i], arime_id))
        except IndexError as e:
            logging.error(e.args)
        except Exception as e:
            self.db.rollback()
            logging.error(e.args)
