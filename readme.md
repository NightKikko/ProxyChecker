# 🕵️‍♂️ Proxy Checker

## 📜 Description
This script retrieves proxies from various APIs, tests their validity, and saves the valid ones into a text file.

## 🌟 Features
* Fetch proxies from multiple APIs
* Test the validity of each proxy
* Save valid proxies directly to `valid_proxies.txt`

## ⚙️ Installation
Make sure you have Python installed, then install the required packages:
pip install requests colorama

## 🚀 Usage

```
Run the script:
```
python proxy_checker.py
```
## ➕ Adding api
Modify `proxy_apis.txt`. Add the URLs of the proxy APIs you want to use, one per line.
Example contents of `proxy_apis.txt`:
```
https://api.proxyscrape.com/?request=displayproxies
https://www.proxy-list.download/api/v1/get?type=https
```

## 🚨 License

This project is licensed under the MIT License.

### MIT License

Copyright (c) [année] [ton nom ou celui de ton organisation]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. Credit must be given to the original authors of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
