# address_search

Search addresses by postal_code (JP).　　
　　
S3 Select ver.

# Requirements

language : python 3.x　　
modules : boto3

# Input data (csv)

x-ken-allYYYYMMDD.csv　　
(http://zipcloud.ibsnet.co.jp/)　　
　　
Rename to 'x-ken-all.csv' and convert encoding to 'utf-8', line feed code to '\n', finally place it on the S3 bucket (bucket name = 'address-search-test').

# Usage

$ pip install awscli
$ chalice deploy
$ aws lambda invoke --function-name address_search-dev-handler --payload '{"postal_code": "{$postal_code}"}' result.txt
$ cat result.txt

{$postal_code} is any postal code. (e.g. 9812114)
