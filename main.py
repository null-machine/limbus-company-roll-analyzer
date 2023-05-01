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

files = [file for file in listdir('sinners')]

print("Generating charts...")

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	plt = sinner.calibrate()
	plt.savefig(f'charts/{sinner.name}.png')
	plt.close()
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime') and not sinner.name.endswith('_partial'):
		sinners.append(sinner)
		s1_list.append(sinner.skills[0])
		s2_list.append(sinner.skills[1])
		s3_list.append(sinner.skills[2])
		for i in range(0, len(sinner.skills)):
			skills.append(sinner.skills[i])

print("Generating tier lists...")

tier_list = open('tier_lists/sinner_clash_ranking.txt', 'w+')
sinners.sort(reverse=True, key=lambda x: x.agg)
for x in sinners:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/skill_clash_ranking.txt', 'w+')
skills.sort(reverse=True, key=lambda x: x.max_agg)
for x in skills:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/s1_clash_ranking.txt', 'w+')
s1_list.sort(reverse=True, key=lambda x: x.max_agg)
for x in s1_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/s2_clash_ranking.txt', 'w+')
s2_list.sort(reverse=True, key=lambda x: x.max_agg)
for x in s2_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/s3_clash_ranking.txt', 'w+')
s3_list.sort(reverse=True, key=lambda x: x.max_agg)
for x in s3_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()

tier_list = open('tier_lists/sinner_damage_ranking.txt', 'w+')
sinners.sort(reverse=True, key=lambda x: x.raw)
for x in sinners:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/skill_damage_ranking.txt', 'w+')
skills.sort(reverse=True, key=lambda x: x.max_raw)
for x in skills:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/s1_damage_ranking.txt', 'w+')
s1_list.sort(reverse=True, key=lambda x: x.max_raw)
for x in s1_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/s2_damage_ranking.txt', 'w+')
s2_list.sort(reverse=True, key=lambda x: x.max_raw)
for x in s2_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/s3_damage_ranking.txt', 'w+')
s3_list.sort(reverse=True, key=lambda x: x.max_raw)
for x in s3_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	plt = sinner.calibrate()
	plt.close()
	if sinner.name.endswith('_weak') or sinner.name.endswith('_prime') or sinner.name.endswith('_partial'):
		sinners.append(sinner)
		s1_list.append(sinner.skills[0])
		s2_list.append(sinner.skills[1])
		s3_list.append(sinner.skills[2])
		for i in range(0, len(sinner.skills)):
			skills.append(sinner.skills[i])

tier_list = open('tier_lists/verbose_sinner_clash_ranking.txt', 'w+')
sinners.sort(reverse=True, key=lambda x: x.agg)
for x in sinners:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_skill_clash_ranking.txt', 'w+')
skills.sort(reverse=True, key=lambda x: x.max_agg)
for x in skills:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_s1_clash_ranking.txt', 'w+')
s1_list.sort(reverse=True, key=lambda x: x.max_agg)
for x in s1_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_s2_clash_ranking.txt', 'w+')
s2_list.sort(reverse=True, key=lambda x: x.max_agg)
for x in s2_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_s3_clash_ranking.txt', 'w+')
s3_list.sort(reverse=True, key=lambda x: x.max_agg)
for x in s3_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()

tier_list = open('tier_lists/verbose_sinner_damage_ranking.txt', 'w+')
sinners.sort(reverse=True, key=lambda x: x.raw)
for x in sinners:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_skill_damage_ranking.txt', 'w+')
skills.sort(reverse=True, key=lambda x: x.max_raw)
for x in skills:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_s1_damage_ranking.txt', 'w+')
s1_list.sort(reverse=True, key=lambda x: x.max_raw)
for x in s1_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_s2_damage_ranking.txt', 'w+')
s2_list.sort(reverse=True, key=lambda x: x.max_raw)
for x in s2_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()
tier_list = open('tier_lists/verbose_s3_damage_ranking.txt', 'w+')
s3_list.sort(reverse=True, key=lambda x: x.max_raw)
for x in s3_list:
	tier_list.write(f'{x.gen_summary()}\n')
tier_list.close()

print("Done!")