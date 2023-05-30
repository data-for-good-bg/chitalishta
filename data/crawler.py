import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import html_to_json
import os
import re

def get_latest_file(PATH,type_, contains):
    list_of_files = [os.path.join(PATH, file)
                     for file in os.listdir(os.path.join(PATH))
                     if type_ in file
                     and contains in file
                     and os.path.getsize(os.path.join(PATH, file)) != 0
                     ]
    latest_file=None
    if len(list_of_files) != 0:
        latest_file = max(list_of_files, key=os.path.getctime)

    return latest_file

class Chitalishta(object):
    
    def __init__(self,crawl_all,export_info_cards):
        self.crawl_all = crawl_all
        self.export_info_cards = export_info_cards
        self.page_url = 'https://chitalishta.com/index.php?act=community&do=list&special=1&&sql_which={}'
        
        
    def get_all_item_links(self,sql_which):
        _dict = {}

        print('Getting data from page: ',self.page_url.format(sql_which))
        response = requests.get(self.page_url.format(sql_which))
        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.find_all('tr',{'class':"odd"})

        for row in rows:
            cells = row.find_all("td")

            if cells:
                reg_num = cells[0].text.strip()
                name = cells[1].text.strip().replace('"','')
                urls = [f"https://chitalishta.com/index.php{a['href']}" for a in cells[1].find_all('a',href=True) if len(a['href'])>0]
                id_ = urls[0].split('&')[-2]
                reg_num  = urls[0].split('&')[-1]
                _dict[f'{id_}&{reg_num}'] = urls[0]

        assert len(rows) == len(_dict), 'Not all chitalishta links downloaded!!!'

        return _dict

    def crawl_one_item(self, idx):
        _dict = {}
        sub_url = f'https://chitalishta.com/index.php?act=community&do=detail&{idx}'
        _dict['idx'] = idx 
        _dict['base_url'] = sub_url 

        sub_response = requests.get(sub_url)
        sub_soup = BeautifulSoup(sub_response.text, "html.parser")
        sub_rows = sub_soup.find_all('tr', {'class': None}, recursive=True)
        for sub_row in sub_rows:
            sub_cells = sub_row.find_all('td',{'class': 'bold'}, recursive=False)
            if len(sub_cells) > 0:
                key = sub_row.find_all('td',{'class': 'bold'})[0].text.strip()
                try:
                    value = sub_row.find_all('td',{'colspan': '3'})[0].text.strip().replace('\xa0',' ').replace('\r\n',' ').replace('"','')
                    if value == 'ВИЖ':
                        value = sub_row.find_all('td',{'colspan': '3'})[0].find_all('a',href=True)[0]['href']
                except IndexError:
                    key = sub_row.find_all('td',{'colspan': '4'})[0].text.strip()
                    link = sub_row.find_all('td',{'colspan': '4'})[0].find_all('a',href=True)[0]['href']
                    value = f'https://chitalishta.com/{link}'

                _dict[key] = value

        return _dict
    
    def export_info_cards(self,meta_all_chitalishta):
        _dict_count = {}

        for item in meta_all_chitalishta:
            info_cards = [i for i in item if 'Информационна карта' in i]
            idx = item['idx']
            _dict_count[idx] = len(info_cards)

            if len(info_cards)!=0:
                for card in info_cards:
                    year = re.findall(r'\d{4}',card)
                    year = year[0] if len(year)==1 else 9999

                    # export each information card to a json format
                    url = item[card]
                    html_response = requests.get(url=url)
                    output_json = html_to_json.convert(html_response.text)

                    with open(f"data/info_cards/{idx}_{year}.json", "w") as file:
                        json.dump(output_json,ensure_ascii=False, indent=2,fp=file)

        assert len([i for i in os.listdir(os.path.join(os.getcwd(),'data/info_cards')) if f'.json' in i]) == np.sum([v for k,v in _dict_count.items()])

        return _dict_count

    
    def crawl_all_meta(self):
        meta_all_chitalishta = []
        _dict_links = {}
        
        sql_which = 0
        
        while True:
            #first check if there are any rows within the base url which contain chitalishta
            response = requests.get(self.page_url.format(sql_which))
            soup = BeautifulSoup(response.text, "html.parser")
            rows = soup.find_all('tr',{'class':"odd"})

            if not rows:
                break
                
            _dict = self.get_all_item_links(sql_which = sql_which)
            _dict_links = {**_dict_links, **_dict}
            
            sql_which += 40

        # crawl meta for all chitalishta once we have the list
        for idx ,url in _dict_links.items():
            meta_all_chitalishta.append(self.crawl_one_item(idx =idx))

        #download meta file
        with open(f'chitalishta_meta_{datetime.now().date()}.json', 'w') as json_file:
            json.dump(meta_all_chitalishta, json_file)
            
        self.meta_all_chitalishta = meta_all_chitalishta
        
    def run(self):
        if self.crawl_all == True:
            self.crawl_all_meta()
        else:
            filename=get_latest_file(PATH = os.getcwd(),type_='json',contains = 'chitalishta')
            with open(filename, 'r') as f:
                data = json.load(f)
            self.meta_all_chitalishta = data
            
        if self.export_info_cards == True:
            _dict_count = self.export_info_cards(meta_all_chitalishta = self.meta_all_chitalishta)
            self._dict_exported_cards = _dict_count

crawl_all=False
export_info_cards=False
       
chit = Chitalishta(crawl_all = crawl_all,export_info_cards=export_info_cards)
chit.run()
