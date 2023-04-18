import yaml
from os import listdir
from sinner import Sinner
from skill import Skill
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def compare_agg(self, other):
	return self.aggregate < other.aggregate

def compare_raw(self, other):
	return self.damage < other.damage

def compare_both(self, other):
	return 2 * self.aggregate + self.damage < 2 * other.aggregate + other.damage

files = [file for file in listdir('sinners')]

sinners = []
skills = []
s1_list = []
s2_list = []
s3_list = []

print("Generating charts...")

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	plt = sinner.gen_chart()
	plt.savefig(f'charts/{sinner.name}.png')
	plt.close()
	sinners.append(sinner)
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime'):
		skills.append(sinner.s1)
		skills.append(sinner.s2)
		skills.append(sinner.s3)
		s1_list.append(sinner.s1)
		s2_list.append(sinner.s2)
		s3_list.append(sinner.s3)

print("Generating tier lists...")

# plt.style.use('dark_background')
# matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
# fig, ax = plt.subplots()
# y = []

for sinner in sinners:
	sinner.__lt__ = compare_agg

sinners.sort(reverse=True)
tier_list = open('tier_lists/verbose_sinner_clash_tier_list.txt', 'w+')
for sinner in sinners:
	tier_list.write(f'{sinner.gen_display_str()}\n')
tier_list.close()

tier_list = open('tier_lists/sinner_clash_tier_list.txt', 'w+')
for sinner in sinners:
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime'):
		tier_list.write(f'{sinner.gen_display_str()}\n')
tier_list.close()



for sinner in sinners:
	sinner.__lt__ = compare_raw

sinners.sort(reverse=True)
tier_list = open('tier_lists/verbose_sinner_damage_tier_list.txt', 'w+')
for sinner in sinners:
	tier_list.write(f'{sinner.gen_display_str()}\n')
tier_list.close()

tier_list = open('tier_lists/sinner_damage_tier_list.txt', 'w+')
for sinner in sinners:
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime'):
		tier_list.write(f'{sinner.gen_display_str()}\n')
tier_list.close()



# for sinner in sinners:
# 	sinner.__lt__ = compare_both

# sinners.sort(reverse=True)
# tier_list = open('tier_lists/verbose_sinner_general_tier_list.txt', 'w+')
# for sinner in sinners:
# 	tier_list.write(f'{sinner.gen_display_str()}\n')
# tier_list.close()

# tier_list = open('tier_lists/sinner_general_tier_list.txt', 'w+')
# for sinner in sinners:
# 	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime'):
# 		tier_list.write(f'{sinner.gen_display_str()}\n')
# tier_list.close()



for skill in skills:
	skill.__lt__ = compare_agg

skills.sort(reverse=True)
tier_list = open('tier_lists/skill_clash_tier_list.txt', 'w+')
for skill in skills:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s1_list.sort(reverse=True)
tier_list = open('tier_lists/s1_clash_tier_list.txt', 'w+')
for skill in s1_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s2_list.sort(reverse=True)
tier_list = open('tier_lists/s2_clash_tier_list.txt', 'w+')
for skill in s2_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s3_list.sort(reverse=True)
tier_list = open('tier_lists/s3_clash_tier_list.txt', 'w+')
for skill in s3_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()



for skill in skills:
	skill.__lt__ = compare_raw

skills.sort(reverse=True)
tier_list = open('tier_lists/skill_damage_tier_list.txt', 'w+')
for skill in skills:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s1_list.sort(reverse=True)
tier_list = open('tier_lists/s1_damage_tier_list.txt', 'w+')
for skill in s1_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s2_list.sort(reverse=True)
tier_list = open('tier_lists/s2_damage_tier_list.txt', 'w+')
for skill in s2_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s3_list.sort(reverse=True)
tier_list = open('tier_lists/s3_damage_tier_list.txt', 'w+')
for skill in s3_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()



for sinner in sinners:
	if sinner.name.endswith('_weak') or sinner.name.endswith('_prime'):
		skills.append(sinner.s1)
		skills.append(sinner.s2)
		skills.append(sinner.s3)
		s1_list.append(sinner.s1)
		s2_list.append(sinner.s2)
		s3_list.append(sinner.s3)



for skill in skills:
	skill.__lt__ = compare_agg

skills.sort(reverse=True)
tier_list = open('tier_lists/verbose_skill_clash_tier_list.txt', 'w+')
for skill in skills:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s1_list.sort(reverse=True)
tier_list = open('tier_lists/verbose_s1_clash_tier_list.txt', 'w+')
for skill in s1_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s2_list.sort(reverse=True)
tier_list = open('tier_lists/verbose_s2_clash_tier_list.txt', 'w+')
for skill in s2_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s3_list.sort(reverse=True)
tier_list = open('tier_lists/verbose_s3_clash_tier_list.txt', 'w+')
for skill in s3_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()



for skill in skills:
	skill.__lt__ = compare_raw

skills.sort(reverse=True)
tier_list = open('tier_lists/verbose_skill_damage_tier_list.txt', 'w+')
for skill in skills:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s1_list.sort(reverse=True)
tier_list = open('tier_lists/verbose_s1_damage_tier_list.txt', 'w+')
for skill in s1_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s2_list.sort(reverse=True)
tier_list = open('tier_lists/verbose_s2_damage_tier_list.txt', 'w+')
for skill in s2_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s3_list.sort(reverse=True)
tier_list = open('tier_lists/verbose_s3_damage_tier_list.txt', 'w+')
for skill in s3_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

print("Done!")