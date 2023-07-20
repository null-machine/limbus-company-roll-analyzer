import yaml
from os import listdir
from sinner import Sinner
from skill import Skill
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sinners = []
skills = []


# def gen_ranking(title, list, key):
# 	list.sort(reverse=True, key=key)
# 	file = open(f'tier_lists/{title}.txt', 'w+')
# 	for x in list:
# 		file.write(f'{x.gen_summary()}\n')
# 	file.close()
	

print("Generating charts...")

files = [file for file in listdir('sinners_ut3')]

for file in files:
	stream = open(f'sinners_ut3/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	sinners.append(sinner)
	for skill in sinner.skills:
		skills.append(skill)
	sinner.calibrate()

for sinner in sinners:
	sinner.competitor_count = len(sinners)

for skill in skills:
	skill.competitor_count = len(skills)

for i in range(0, 3):
	for j in range (0, 4):
		sinners.sort(reverse=True, key=lambda x: x.elite_bias_score_matrix[i][j])
		for k in range(0, len(sinners)):
			sinners[k].elite_bias_rank_matrix[i][j] = k + 1

for i in range(0, 3):
	for j in range (0, 4):
		sinners.sort(reverse=True, key=lambda x: x.full_deck_score_matrix[i][j])
		for k in range(0, len(sinners)):
			sinners[k].full_deck_rank_matrix[i][j] = k + 1

for i in range(0, 3):
	for j in range (0, 5):
			skills.sort(reverse=True, key=lambda x: x.score_matrix[i][j])
			for k in range(0, len(skills)):
				skills[k].rank_matrix[i][j] = k + 1

for i in range(0, 3):
	for sinner in sinners:
		if (i == 0 and not sinner.has_weak) or (i == 2 and not sinner.has_prime):
			continue
		plt = sinner.gen_chart(i)
		variant_name = ''
		if i == 0:
			variant_name = 'adverse'
		elif i == 1:
			variant_name = 'expected'
		elif i == 2:
			variant_name = 'prime'
		plt.savefig(f'charts_ut3/{sinner.name}_{variant_name}.png')
		plt.close()