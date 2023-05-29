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

def gen_ranking(title, list, key):
	list.sort(reverse=True, key=key)
	file = open(f'tier_lists/{title}.txt', 'w+')
	for x in list:
		file.write(f'{x.gen_summary()}\n')
	file.close()
	

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

gen_ranking('ideal_sp_sinner_clash_ranking', sinners, lambda x: x.max_agg)
gen_ranking('ideal_sp_skill_clash_ranking', skills, lambda x: x.max_agg)
gen_ranking('ideal_sp_s1_clash_ranking', s1_list, lambda x: x.max_agg)
gen_ranking('ideal_sp_s2_clash_ranking', s2_list, lambda x: x.max_agg)
gen_ranking('ideal_sp_s3_clash_ranking', s3_list, lambda x: x.max_agg)

gen_ranking('zero_sp_sinner_clash_ranking', sinners, lambda x: x.min_agg + x.max_agg)
gen_ranking('zero_sp_skill_clash_ranking', skills, lambda x: x.min_agg + x.max_agg)
gen_ranking('zero_sp_s1_clash_ranking', s1_list, lambda x: x.min_agg + x.max_agg)
gen_ranking('zero_sp_s2_clash_ranking', s2_list, lambda x: x.min_agg + x.max_agg)
gen_ranking('zero_sp_s3_clash_ranking', s3_list, lambda x: x.min_agg + x.max_agg)

gen_ranking('ideal_sp_sinner_damage_ranking', sinners, lambda x: x.max_raw)
gen_ranking('ideal_sp_skill_damage_ranking', skills, lambda x: x.max_raw)
gen_ranking('ideal_sp_s1_damage_ranking', s1_list, lambda x: x.max_raw)
gen_ranking('ideal_sp_s2_damage_ranking', s2_list, lambda x: x.max_raw)
gen_ranking('ideal_sp_s3_damage_ranking', s3_list, lambda x: x.max_raw)

gen_ranking('zero_sp_sinner_damage_ranking', sinners, lambda x: x.min_raw + x.max_raw)
gen_ranking('zero_sp_skill_damage_ranking', skills, lambda x: x.min_raw + x.max_raw)
gen_ranking('zero_sp_s1_damage_ranking', s1_list, lambda x: x.min_raw + x.max_raw)
gen_ranking('zero_sp_s2_damage_ranking', s2_list, lambda x: x.min_raw + x.max_raw)
gen_ranking('zero_sp_s3_damage_ranking', s3_list, lambda x: x.min_raw + x.max_raw)

gen_ranking('ideal_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_max_agg)
gen_ranking('ideal_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_max_raw)
gen_ranking('zero_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_min_agg + x.turn_one_max_agg)
gen_ranking('zero_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_min_raw + x.turn_one_max_raw)

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

gen_ranking('verbose_ideal_sp_sinner_clash_ranking', sinners, lambda x: x.max_agg)
gen_ranking('verbose_ideal_sp_skill_clash_ranking', skills, lambda x: x.max_agg)
gen_ranking('verbose_ideal_sp_s1_clash_ranking', s1_list, lambda x: x.max_agg)
gen_ranking('verbose_ideal_sp_s2_clash_ranking', s2_list, lambda x: x.max_agg)
gen_ranking('verbose_ideal_sp_s3_clash_ranking', s3_list, lambda x: x.max_agg)

gen_ranking('verbose_zero_sp_sinner_clash_ranking', sinners, lambda x: x.min_agg + x.max_agg)
gen_ranking('verbose_zero_sp_skill_clash_ranking', skills, lambda x: x.min_agg + x.max_agg)
gen_ranking('verbose_zero_sp_s1_clash_ranking', s1_list, lambda x: x.min_agg + x.max_agg)
gen_ranking('verbose_zero_sp_s2_clash_ranking', s2_list, lambda x: x.min_agg + x.max_agg)
gen_ranking('verbose_zero_sp_s3_clash_ranking', s3_list, lambda x: x.min_agg + x.max_agg)

gen_ranking('verbose_ideal_sp_sinner_damage_ranking', sinners, lambda x: x.max_raw)
gen_ranking('verbose_ideal_sp_skill_damage_ranking', skills, lambda x: x.max_raw)
gen_ranking('verbose_ideal_sp_s1_damage_ranking', s1_list, lambda x: x.max_raw)
gen_ranking('verbose_ideal_sp_s2_damage_ranking', s2_list, lambda x: x.max_raw)
gen_ranking('verbose_ideal_sp_s3_damage_ranking', s3_list, lambda x: x.max_raw)

gen_ranking('verbose_zero_sp_sinner_damage_ranking', sinners, lambda x: x.min_raw + x.max_raw)
gen_ranking('verbose_zero_sp_skill_damage_ranking', skills, lambda x: x.min_raw + x.max_raw)
gen_ranking('verbose_zero_sp_s1_damage_ranking', s1_list, lambda x: x.min_raw + x.max_raw)
gen_ranking('verbose_zero_sp_s2_damage_ranking', s2_list, lambda x: x.min_raw + x.max_raw)
gen_ranking('verbose_zero_sp_s3_damage_ranking', s3_list, lambda x: x.min_raw + x.max_raw)

gen_ranking('verbose_ideal_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_max_agg)
gen_ranking('verbose_ideal_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_max_raw)
gen_ranking('verbose_zero_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_min_agg + x.turn_one_max_agg)
gen_ranking('verbose_zero_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_min_raw + x.turn_one_max_raw)

print("Done!")