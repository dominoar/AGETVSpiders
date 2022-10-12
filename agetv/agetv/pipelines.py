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
        arime_url_id = self.sql_urls(urls=v_urls, arime_id=arime_id)
        self.db.commit()
        print("UPDATE arime.arime SET v_urls = %s WHERE v_id = %s" % (arime_url_id, arime_id))
        self.cursor.execute("UPDATE arime.arime SET v_urls = %s WHERE v_id = %s" % (arime_id, arime_id))
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
        logging.info('开始插入urls')
        try:
            urls_len = []
            for k in range(0, len(urls)):
                urls_len.append(len(urls[k]))
                pass
            for i in range(0, len(urls[urls_len.index(min(urls_len))])):
                self.cursor.execute(
                    'INSERT INTO arime_urls(url1,arime_id) VALUES ("%s","%s")' % (
                        urls[0][i], arime_id))
                uid = self.cursor.lastrowid
                self.cursor.execute(f'UPDATE arime_urls SET url2 = "{urls[1][i]}" WHERE uid={uid}')
                self.cursor.execute(f'UPDATE arime_urls SET url3 = "{urls[2][i]}" WHERE uid={uid}')
                self.cursor.execute(f'UPDATE arime_urls SET url4 = "{urls[3][i]}" WHERE uid={uid}')
        except IndexError as e:
            logging.error(e.args)
        except Exception as e:
            self.db.rollback()
            logging.error(e.args)
