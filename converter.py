import yaml
from os import listdir
from sinner import Sinner
from skill import Skill
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sinners = []

# help(yaml.Dumper)

files = [file for file in listdir('sinners')]

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	if not sinner.name.endswith('_weak') and not sinner.name.endswith('_prime') and not sinner.name.endswith('_partial'):
		sinner.name += '_ut3'
		for skill in sinner.skills:
			skill.offense -= 35
			skill.stats = [skill.base_power, skill.coin_power, skill.coin_count, skill.offense]
			skill.damage_bonuses = [0, 0, 0, 0]
			skill.prime_bonuses = [0, 0, 0, 0]
			skill.prime_damage_bonuses = [0, 0, 0, 0]
			skill.weak_bonuses = [0, 0, 0, 0]
			skill.weak_damage_bonuses = [0, 0, 0, 0]
			# del skill.name
			del skill.base_power
			del skill.coin_power
			del skill.coin_count
			del skill.offense
		data = yaml.dump(sinner, sort_keys=False)
		output = open(f'sinners_ut3/{file}', 'w')
		output.write(data)