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

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	sinners.append(sinner)
	plt = sinner.gen_chart()
	# if is_file(f'charts/{sinner.name}.png')
	plt.savefig(f'charts/{sinner.name}.png')
	plt.close()
	
sinners.sort(reverse=True)

tier_list = open('tier_list.txt', 'w+')
for sinner in sinners:
	tier_list.write(f'{sinner.gen_display_str()}\n')
tier_list.close()

# stream = open(f'sinners/gregor_g_corp.yaml', 'r')
# sinner = yaml.load(stream, yaml.Loader)
# plt = sinner.gen_chart()
# plt.savefig(f'charts/{sinner.name}.png')
# plt.close()