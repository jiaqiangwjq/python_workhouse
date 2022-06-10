import requests
import re
import json
from requests.exceptions import RequestException

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
    

def parse_one_page(html):
    pattern = re.compile('class="sig sig-object py" id="(.*?)"', re.S)
    items = re.findall(pattern, html)
    return items


def main():
    cat_torch_api = ['torch', 'torch_tensor', 'torch_nn', 'torch_nn_init', 'torch_nn_module', 'torch_nn_parallel', 'torch_nn_utils',
                 'torch_nn_functional', 'torch_autograd', 'torch_optim', 'torch_distributed', 'torch_distributions', 'torch_cuda',
                 'torch_random']
    torch_api_num = {}
    torch_api = {}
    
    cat_parrots_api = ['parrots_info', 'parrots_ir', 'parrots_comm', 'parrots_logging', 'parrots_runtimeconfig', 'parrots_autograd',
                   'parrots_utils_track', 'parrots_utils_tester', 'parrots_quantizer']
    parrots_api_num = {}
    parrots_api = {}
    
    url_torch = 'http://parrots.sensetime.com/parrots/torch_api/'
    url_parrots = 'http://parrots.sensetime.com/parrots/parrots_api/'
    
    for category in cat_torch_api:
        url = url_torch + category + '.html'
        print(url)
        html = get_one_page(url)
        res = parse_one_page(html)
        torch_api_num[category] = len(res)
        torch_api[category] = res
    
    for category in cat_parrots_api:
        url = url_parrots + category + '.html'
        print(url)
        html = get_one_page(url)
        res = parse_one_page(html)
        parrots_api_num[category] = len(res)
        parrots_api[category] = res
    
    print('\n')
    
    print(torch_api_num)
    print('Total of torch_api: ', sum(torch_api_num.values()), '\n')
    
    print(parrots_api_num)
    print('Total of parrots_api: ', sum(parrots_api_num.values()), '\n')
    
    print('All APIs: ', sum(torch_api_num.values()) + sum(parrots_api_num.values()))
    
if __name__ == '__main__':
    main()