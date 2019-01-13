# address_search

Search addresses by postal_code (JP).　　
　　
(unuse db and external services.)　　

# Requirements

language : python 3.x　　
modules : reference to "requirements.txt"

# Input data (csv)

x-ken-allYYYYMMDD.csv　　
(http://zipcloud.ibsnet.co.jp/)　　
　　
Rename to 'x-ken-all.csv' and place it the directory where script exists.

# Usage

$ pip install　　
$ python address_search {$postal_code}　　

e.g.
```
$ python ./address_search.py 6028303
[{'postal_code': '6028303', 'pref': '京都府', 'city': '京都市上京区', 'address1': '姥ケ寺之前町'}]
(test_ken_all) HyperMacBookAirEx:address_search admin$ python ./address_search.py 9812114
[{'postal_code': '9812114', 'pref': '宮城県', 'city': '伊具郡丸森町', 'address1': '赤堀'}, {'postal_code': '9812114', 'pref': '宮城県', 'city': '伊具郡丸森町', 'address1': '泉'}, {'postal_code': '9812114', 'pref': '宮城県', 'city': '伊具郡丸森町', 'address1': '泉下'}, {'postal_code': '9812114', 'pref': '宮城県', 'city': '伊具郡丸森町', 'address1': '大目'}, {'postal_code': '9812114', 'pref': '宮城県', 'city': '伊具郡丸森町', 'address1': '北前'}, {'postal_code': '9812114', 'pref': '宮城県', 'city': '伊具郡丸森町', 'address1': '天王'}]
```
