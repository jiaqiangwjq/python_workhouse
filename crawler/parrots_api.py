# 此脚本用于爬取 Parrots api 文档并统计目前 Parrots 支持的算子数量

import requests
import re
from requests.exceptions import RequestException
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--save_path", type=str, default='./')
parser.add_argument("--file_name", type=str, default='result.txt')
args = parser.parse_args()


# 伪装成 browser 并发送 get 请求，获取 parrots api 页面 
def get_one_page(url):
    
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.text
        return None
    
    except RequestException:
        return None
    

# 解析目标页面的 html 代码，并用正则表达式获取各类算子的名称
def parse_one_page(pattern, html):
    
    # 正则表达式，用于提取 torch 和 parrots 所支持的算子类别名
    result = re.findall(pattern, html)
    
    return result


def main():
    
    # Parrots api 文档主页面
    url = 'http://parrots.sensetime.com/parrots/'
    
    pattern_torch = re.compile('class="reference internal" href="(torch.*?)">(.*?)<', re.S)     # 匹配 torch 下的类
    pattern_parrots = re.compile('class="reference internal" href="(parrots.*?)">(.*?)<', re.S) # 匹配 parrots 下的类
    pattern_api = re.compile('class="sig sig-object py" id="(.*?)"', re.S)  # 匹配每一个算子名

    # 获取页面并按照正则表达式对其进行解析
    html_cat = get_one_page(url)
    result_torch = parse_one_page(pattern_torch, html_cat) 
    result_parrots = parse_one_page(pattern_parrots, html_cat)
    
    
    torch_api_num, parrots_api_num = {}, {}     # 保存每个类下算子的数量
    torch_api, parrots_api = {}, {}     # 保存每个类包含的具体算子名
    
    
    for i in range(len(result_torch)):
        url_torch = url + result_torch[i][0]
        print(url_torch)
        html_torch = get_one_page(url_torch)
        res = parse_one_page(pattern_api, html_torch)
        torch_api[result_torch[i][1]] = res
        torch_api_num[result_torch[i][1]] = len(res)
    
    for i in range(len(result_parrots)):
        url_parrots = url + result_parrots[i][0]
        print(url_parrots)
        html_parrots = get_one_page(url_parrots)
        res = parse_one_page(pattern_api,html_parrots)
        parrots_api[result_parrots[i][1]] = res
        parrots_api_num[result_parrots[i][1]] = len(res)
    
    
    # 将结果写入文件，文件路径可自行修改
    with open(args.save_path + args.file_name, 'w', encoding='utf-8') as f:
        f.write('All APIs: ' + str(sum(torch_api_num.values()) + sum(parrots_api_num.values())) + '\n')     # 总算子数
        
        # torch 下的算子数
        for i in range(len(torch_api_num)):
            f.write('=' * 60 + '\n')
            f.write(result_torch[i][1] + ': ' + str(torch_api_num[result_torch[i][1]]) + '\n')
            f.write(str(torch_api[result_torch[i][1]]) + '\n')

        # parrots 下的算子数
        for i in range(len(parrots_api_num)):
            f.write('=' * 60 + '\n')
            f.write(result_parrots[i][1] + ': ' + str(parrots_api_num[result_parrots[i][1]]) + '\n')
            f.write(str(parrots_api[result_parrots[i][1]]) + '\n')
            
    print('\n\n', 'Save File: ', args.save_path + args.file_name)

if __name__ == '__main__':
    main()