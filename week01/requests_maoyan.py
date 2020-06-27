#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


if __name__ == "__main__":
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

    header = {
        "user-agent": user_agent
        }

    url = 'https://maoyan.com/films?showType=3'

    response = requests.get(url, headers=header)
    
    if response.url != url:
        print("Please open '%s' in browser ！" % response.url)
        return

    bs_obj = bs(response.text, 'html.parser')

    movies_list = []

    count = 0
    # 获取电影列表
    for tags in bs_obj.find_all('div', attrs={'class': 'movie-hover-info'}):
        
        # 只取前10个电影
        if count >= 10:
            break

        # 获取电影所有属性
        movie_info = tags.find_all('div', attrs={'class': 'movie-hover-title'})
        print(movie_info, type(movie_info), len(movie_info))
        print("*******************************************")

        movie_title = movie_info[0].find('span', attrs={'class': 'name'}).text
        print(movie_title)
        print("*******************************************")

        # 获取电影所有属性
        # hover_tags = tags.find_all('span', attrs={'class': 'hover-tag'})
        # print(hover_tags)

        # 获取电影类型
        movie_type = list(movie_info[1].stripped_strings)
        print(movie_type)
        print("*******************************************")

        # 获取电影上映时间
        movie_time = list(movie_info[3].stripped_strings)
        print(movie_time)
        print("*******************************************")

        movie = {}
        movie["Title"] = movie_title
        movie["Type"] = movie_type[1]
        movie["Time"] = movie_time[1]
        movies_list.append(movie)

        count += 1

    df = pd.DataFrame(movies_list).to_csv("requests_maoyan.csv")