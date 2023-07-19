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
	sinner.competitor_count = len(sinners)

for i in range(0, 3):
	for j in range (0, 4):
		sinners.sort(reverse=True, key=lambda x: x.elite_bias_scores_matrix[i][j])
		for k in range(0, len(sinners)):
			sinners[k].elite_bias_ranks_matrix[i][j] = k + 1

for i in range(0, 3):
	for j in range (0, 4):
		sinners.sort(reverse=True, key=lambda x: x.full_deck_scores_matrix[i][j])
		for k in range(0, len(sinners)):
			sinners[k].full_deck_ranks_matrix[i][j] = k + 1

for sinner in sinners:
	plt = sinner.gen_chart(1)
	plt.savefig(f'charts_ut3/{sinner.name}.png')
	plt.close()