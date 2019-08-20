#!/usr/bin/python
import sys
import json
import argparse

def hive_lld():
  new_data =[]
  with open('/run/hive/gpu-detect.json') as json_file:
    data = json.load(json_file)
    i = 0
    for p in data:
      new_data.append({'{#GPUNUMBER}':'gpu_' + str(i)})
      i = i + 1
  print json.dumps({"data": new_data})

def hive_gpu_stats(item, gpu):
  new_data =[]
  gpu_id = gpu.split('_')
  second_item_list = ['temp', 'power', 'fan']
  if any(x in item for x in second_item_list):
    Filename='/var/run/hive/gpu-stats.json'
  else:
    Filename='/run/hive/gpu-detect.json'
  with open(Filename) as json_file:
    data = json.load(json_file)
  i = 0
  if any(x in item for x in second_item_list):
    for p in data[item]:
      if i == int(gpu_id[1]):
        print p
      i = i + 1
  else:
    for p in data:
      if i == int(gpu_id[1]):
        print p[item]
      i = i + 1
def main():
  if sys.argv[1] == 'lld':
    hive_lld()
  else:
    hive_gpu_stats(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
