import yaml
from os import listdir
from sinner import Sinner
from skill import Skill


message = '''# Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies
- Generates charts of sinner skill winrates versus enemy single coin skills.
- Enemy offense level is assumed to be 35.
- Y-axis represents the chance of winning the clash.
- X-axis represents the power of the enemy single coin skill.
- Cyan, yellow and magenta lines are associated a chance of 0.95, 0.5 and 0.05 of rolling heads respectively.
- An additional chart will be generated for sinners with passives or conditionals that can be reasonably met.
- View sinner.yaml files to see chosen numbers.
'''
print(message)

read_me = open('README.md', 'w+')
read_me.write(message)
read_me.close()

files = [file for file in listdir('sinners')]

sinners = []
skills = []
s1_list = []
s2_list = []
s3_list = []
s1_average = 0
s2_average = 0
s3_average = 0

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	plt = sinner.gen_chart()
	# plt.savefig(f'charts/{sinner.name}.png')
	plt.close()
	sinners.append(sinner)
	skills.append(sinner.s1)
	s1_list.append(sinner.s1)
	s1_average += sinner.s1.max_aggregate
	skills.append(sinner.s2)
	s2_list.append(sinner.s2)
	s2_average += sinner.s2.max_aggregate
	skills.append(sinner.s3)
	s3_list.append(sinner.s3)
	s3_average += sinner.s3.max_aggregate

s1_average /= len(s1_list)
s2_average /= len(s2_list)
s3_average /= len(s3_list)

sinners.sort(reverse=True)
tier_list = open('sinner_tier_list.txt', 'w+')
for sinner in sinners:
	tier_list.write(f'{sinner.gen_display_str()}\n')
tier_list.close()

skills.sort(reverse=True)
tier_list = open('skill_tier_list.txt', 'w+')
for skill in skills:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s1_list.sort(reverse=True)
tier_list = open('s1_tier_list.txt', 'w+')
for skill in s1_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s2_list.sort(reverse=True)
tier_list = open('s2_tier_list.txt', 'w+')
for skill in s2_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

s3_list.sort(reverse=True)
tier_list = open('s3_tier_list.txt', 'w+')
for skill in s3_list:
	tier_list.write(f'{skill.gen_display_str()}\n')
tier_list.close()

# averages = open('skill_averages.txt', 'w+')
# averages.write(f'{s1_average} {s2_average} {s3_average}')
# averages.close()

# stream = open(f'sinners/gregor_g_corp.yaml', 'r')
# sinner = yaml.load(stream, yaml.Loader)
# plt = sinner.gen_chart()
# plt.savefig(f'charts/{sinner.name}.png')
# plt.close()