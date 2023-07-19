import yaml
from os import listdir
from sinner import Sinner
from skill import Skill
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sinners = []
skills = []
s1_list = []
s2_list = []
s3_list = []

files = [file for file in listdir('sinners_ut3')]

# def gen_ranking(title, list, key):
# 	list.sort(reverse=True, key=key)
# 	file = open(f'tier_lists/{title}.txt', 'w+')
# 	for x in list:
# 		file.write(f'{x.gen_summary()}\n')
# 	file.close()
	

print("Generating charts...")

for file in files:
	stream = open(f'sinners_ut3/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	sinners.append(sinner)
	sinner.calibrate()

for sinner in sinners:
	plt = sinner.gen_chart(1)
	plt.savefig(f'charts_ut3/{sinner.name}.png')
	plt.close()