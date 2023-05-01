import yaml
from os import listdir
from sinner import Sinner
from skill import Skill
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

files = [file for file in listdir('sinners')]

# for file in files:
# 	stream = open(f'new_sinners/{file}', 'r')
# 	sinner = yaml.load(stream, yaml.Loader)
# 	plt = sinner.gen_chart()
	# sinner.calibrate()
	# write_stream = open(f'new_sinners/{file}', 'w+')
	# yaml.dump(sinner, write_stream)
	

sinners = []
verbose_sinners = []
skills = []
s1_list = []
s2_list = []
s3_list = []

print("Generating charts...")

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	plt = sinner.calibrate()
	plt.savefig(f'charts/{sinner.name}.png')
	plt.close()
	verbose_sinners.append(sinner)
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime') and not sinner.name.endswith('_partial'):
		sinners.append(sinner)

print("Generating tier lists...")

sinners.sort(reverse=True, key=lambda x: x.aggregate)
tier_list = open('tier_lists/verbose_sinner_clash_tier_list.txt', 'w+')
for sinner in sinners:
	tier_list.write(f'{sinner.gen_summary()}\n')
tier_list.close()

tier_list = open('tier_lists/sinner_clash_tier_list.txt', 'w+')
for sinner in sinners:
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime') and not sinner.name.endswith('_partial'):
		tier_list.write(f'{sinner.gen_summary()}\n')
tier_list.close()



# sinners.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/verbose_sinner_damage_tier_list.txt', 'w+')
# for sinner in sinners:
# 	tier_list.write(f'{sinner.gen_summary()}\n')
# tier_list.close()

# tier_list = open('tier_lists/sinner_damage_tier_list.txt', 'w+')
# for sinner in sinners:
# 	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime') and not sinner.name.endswith('_partial'):
# 		tier_list.write(f'{sinner.gen_summary()}\n')
# tier_list.close()



# skills.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/skill_clash_tier_list.txt', 'w+')
# for skill in skills:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s1_list.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/s1_clash_tier_list.txt', 'w+')
# for skill in s1_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s2_list.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/s2_clash_tier_list.txt', 'w+')
# for skill in s2_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s3_list.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/s3_clash_tier_list.txt', 'w+')
# for skill in s3_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()



# skills.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/skill_damage_tier_list.txt', 'w+')
# for skill in skills:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s1_list.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/s1_damage_tier_list.txt', 'w+')
# for skill in s1_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s2_list.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/s2_damage_tier_list.txt', 'w+')
# for skill in s2_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s3_list.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/s3_damage_tier_list.txt', 'w+')
# for skill in s3_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()



# for sinner in sinners:
# 	if sinner.name.endswith('_weak') or sinner.name.endswith('_prime'):
# 		skills.append(sinner.s1)
# 		skills.append(sinner.s2)
# 		skills.append(sinner.s3)
# 		s1_list.append(sinner.s1)
# 		s2_list.append(sinner.s2)
# 		s3_list.append(sinner.s3)



# skills.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/verbose_skill_clash_tier_list.txt', 'w+')
# for skill in skills:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s1_list.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/verbose_s1_clash_tier_list.txt', 'w+')
# for skill in s1_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s2_list.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/verbose_s2_clash_tier_list.txt', 'w+')
# for skill in s2_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s3_list.sort(reverse=True, key=lambda x: x.aggregate)
# tier_list = open('tier_lists/verbose_s3_clash_tier_list.txt', 'w+')
# for skill in s3_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()



# skills.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/verbose_skill_damage_tier_list.txt', 'w+')
# for skill in skills:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s1_list.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/verbose_s1_damage_tier_list.txt', 'w+')
# for skill in s1_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s2_list.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/verbose_s2_damage_tier_list.txt', 'w+')
# for skill in s2_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# s3_list.sort(reverse=True, key=lambda x: x.damage)
# tier_list = open('tier_lists/verbose_s3_damage_tier_list.txt', 'w+')
# for skill in s3_list:
# 	tier_list.write(f'{skill.gen_summary()}\n')
# tier_list.close()

# print("Done!")