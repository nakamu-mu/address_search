#!/usr/bin/env python

import sys
import pandas as pd
import math

INDEX_POSTAL_CODE = 2
INDEX_PREF = 6
INDEX_CITY = 7
INDEX_ADDRESS1 = 8

class AddressBook:

  address_df = None

  keys = (
    'local_gov_code',
    'postal_code_old',
    'postal_code',
    'pref_kana',
    'city_kana',
    'address1_kana',
    'pref',
    'city',
    'address1',
    'flg1',
    'flg2',
    'flg3',
    'flg4',
    'flg5',
    'flg6',
  )

  def __init__(self, src_csv_path):
    self.address_df = pd.read_csv(
      src_csv_path,
      encoding="shift-jis",
      names=self.keys,
      dtype="object"
    )

  def get_addresses(self, postal_code):
    addresses = self.address_df.query("postal_code==@postal_code").fillna('').values.tolist()
    results = []
    for address in addresses:
      results.append({
        'postal_code': address[INDEX_POSTAL_CODE],
        'pref': address[INDEX_PREF],
        'city': address[INDEX_CITY],
        'address1': address[INDEX_ADDRESS1]
      })
    return results

if __name__ == '__main__':
  if len(sys.argv) <= 1:
    print('Invalid arguments...')
    sys.exit(-1)
  
  postal_code = sys.argv[1]
  ab = AddressBook('./x-ken-all.csv')
  print(ab.get_addresses(postal_code))