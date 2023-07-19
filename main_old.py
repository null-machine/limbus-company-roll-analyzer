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
	sinner.calibrate()
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime') and not sinner.name.endswith('_partial'):
		sinners.append(sinner)
		s1_list.append(sinner.skills[0])
		s2_list.append(sinner.skills[1])
		s3_list.append(sinner.skills[2])
		for i in range(0, len(sinner.skills)):
			skills.append(sinner.skills[i])

for sinner in sinners:
	sinner.competitor_count = len(sinners)

sinners.sort(reverse=True, key=lambda x: x.max_agg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_ideal_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.min_agg + x.max_agg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_zero_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.max_dmg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_ideal_damage_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.min_dmg + x.max_dmg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_zero_damage_rank = i + 1

sinners.sort(reverse=True, key=lambda x: x.turn_one_max_agg)
for i in range(0, len(sinners)):
	sinners[i].strong_bias_ideal_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.turn_one_max_agg + x.turn_one_min_agg)
for i in range(0, len(sinners)):
	sinners[i].strong_bias_zero_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.turn_one_max_dmg)
for i in range(0, len(sinners)):
	sinners[i].strong_bias_ideal_damage_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.turn_one_max_dmg + x.turn_one_min_dmg)
for i in range(0, len(sinners)):
	sinners[i].strong_bias_zero_damage_rank = i + 1

sinners.sort(reverse=True, key=lambda x: x.skills[0].max_agg)
for i in range(0, len(sinners)):
	sinners[i].s1_ideal_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[0].max_agg + x.skills[0].min_agg)
for i in range(0, len(sinners)):
	sinners[i].s1_zero_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[0].max_dmg)
for i in range(0, len(sinners)):
	sinners[i].s1_ideal_damage_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[0].max_dmg + x.skills[0].min_dmg)
for i in range(0, len(sinners)):
	sinners[i].s1_zero_damage_rank = i + 1

sinners.sort(reverse=True, key=lambda x: x.skills[1].max_agg)
for i in range(0, len(sinners)):
	sinners[i].s2_ideal_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[1].max_agg + x.skills[1].min_agg)
for i in range(0, len(sinners)):
	sinners[i].s2_zero_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[1].max_dmg)
for i in range(0, len(sinners)):
	sinners[i].s2_ideal_damage_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[1].max_dmg + x.skills[1].min_dmg)
for i in range(0, len(sinners)):
	sinners[i].s2_zero_damage_rank = i + 1

sinners.sort(reverse=True, key=lambda x: x.skills[2].max_agg)
for i in range(0, len(sinners)):
	sinners[i].s3_ideal_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[2].max_agg + x.skills[2].min_agg)
for i in range(0, len(sinners)):
	sinners[i].s3_zero_clash_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[2].max_dmg)
for i in range(0, len(sinners)):
	sinners[i].s3_ideal_damage_rank = i + 1
sinners.sort(reverse=True, key=lambda x: x.skills[2].max_dmg + x.skills[2].min_dmg)
for i in range(0, len(sinners)):
	sinners[i].s3_zero_damage_rank = i + 1

for sinner in sinners:
	plt = sinner.gen_chart()
	plt.savefig(f'charts/{sinner.name}.png')
	plt.close()

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

gen_ranking('ideal_sp_sinner_damage_ranking', sinners, lambda x: x.max_dmg)
gen_ranking('ideal_sp_skill_damage_ranking', skills, lambda x: x.max_dmg)
gen_ranking('ideal_sp_s1_damage_ranking', s1_list, lambda x: x.max_dmg)
gen_ranking('ideal_sp_s2_damage_ranking', s2_list, lambda x: x.max_dmg)
gen_ranking('ideal_sp_s3_damage_ranking', s3_list, lambda x: x.max_dmg)

gen_ranking('zero_sp_sinner_damage_ranking', sinners, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('zero_sp_skill_damage_ranking', skills, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('zero_sp_s1_damage_ranking', s1_list, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('zero_sp_s2_damage_ranking', s2_list, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('zero_sp_s3_damage_ranking', s3_list, lambda x: x.min_dmg + x.max_dmg)

gen_ranking('ideal_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_max_agg)
gen_ranking('ideal_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_max_dmg)

gen_ranking('zero_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_min_agg + x.turn_one_max_agg)
gen_ranking('zero_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_min_dmg + x.turn_one_max_dmg)

gen_ranking('ideal_sp_no_s1_sinner_clash_ranking', sinners, lambda x: 2 * x.skills[1].max_agg + x.skills[2].max_agg)
gen_ranking('ideal_sp_no_s1_sinner_damage_ranking', sinners, lambda x: 2 * x.skills[1].max_dmg + x.skills[2].max_dmg)

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	sinner.calibrate()
	if sinner.name.endswith('_weak') or sinner.name.endswith('_prime') or sinner.name.endswith('_partial'):
		sinners.append(sinner)
		s1_list.append(sinner.skills[0])
		s2_list.append(sinner.skills[1])
		s3_list.append(sinner.skills[2])
		for i in range(0, len(sinner.skills)):
			skills.append(sinner.skills[i])

sinners.sort(reverse=True, key=lambda x: x.max_agg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_ideal_clash_rank = i + 1
	sinners[i].full_deck_competitor_count = len(sinners)
sinners.sort(reverse=True, key=lambda x: x.min_agg + x.max_agg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_zero_clash_rank = i + 1
	sinners[i].full_deck_competitor_count = len(sinners)
sinners.sort(reverse=True, key=lambda x: x.max_dmg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_ideal_damage_rank = i + 1
	sinners[i].full_deck_competitor_count = len(sinners)
sinners.sort(reverse=True, key=lambda x: x.min_dmg + x.max_dmg)
for i in range(0, len(sinners)):
	sinners[i].full_deck_zero_damage_rank = i + 1
	sinners[i].full_deck_competitor_count = len(sinners)

sinners.sort(reverse=True, key=lambda x: x.turn_one_max_agg)
for i in range(0, len(sinners)):
	sinners[i].strong_bias_ideal_clash_rank = i + 1
	sinners[i].strong_bias_competitor_count = len(sinners)

sinners.sort(reverse=True, key=lambda x: x.turn_one_max_agg + x.turn_one_min_agg)
for i in range(0, len(sinners)):
	sinners[i].strong_bias_zero_clash_rank = i + 1
	sinners[i].strong_bias_competitor_count = len(sinners)

for sinner in sinners:
	if sinner.name.endswith('_weak') or sinner.name.endswith('_prime') or sinner.name.endswith('_partial'):
		plt = sinner.gen_chart()
		plt.savefig(f'charts/{sinner.name}.png')
		plt.close()

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

gen_ranking('verbose_ideal_sp_sinner_damage_ranking', sinners, lambda x: x.max_dmg)
gen_ranking('verbose_ideal_sp_skill_damage_ranking', skills, lambda x: x.max_dmg)
gen_ranking('verbose_ideal_sp_s1_damage_ranking', s1_list, lambda x: x.max_dmg)
gen_ranking('verbose_ideal_sp_s2_damage_ranking', s2_list, lambda x: x.max_dmg)
gen_ranking('verbose_ideal_sp_s3_damage_ranking', s3_list, lambda x: x.max_dmg)

gen_ranking('verbose_zero_sp_sinner_damage_ranking', sinners, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('verbose_zero_sp_skill_damage_ranking', skills, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('verbose_zero_sp_s1_damage_ranking', s1_list, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('verbose_zero_sp_s2_damage_ranking', s2_list, lambda x: x.min_dmg + x.max_dmg)
gen_ranking('verbose_zero_sp_s3_damage_ranking', s3_list, lambda x: x.min_dmg + x.max_dmg)

gen_ranking('verbose_ideal_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_max_agg)
gen_ranking('verbose_ideal_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_max_dmg)
gen_ranking('verbose_zero_sp_turn_one_sinner_clash_ranking', sinners, lambda x: x.turn_one_min_agg + x.turn_one_max_agg)
gen_ranking('verbose_zero_sp_turn_one_sinner_damage_ranking', sinners, lambda x: x.turn_one_min_dmg + x.turn_one_max_dmg)

print("Done!")