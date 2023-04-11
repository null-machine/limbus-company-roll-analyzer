import yaml
from os import listdir
from sinner import Sinner
from skill import Skill


message = '''Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies
- Generates charts of sinner skill winrates versus enemy single coin skills.
- Enemy offense level is assumed to be 30.
- Y-axis represents the chance of winning the clash.
- X-axis represents the power of the enemy single coin skill.
- Cyan, yellow and magenta lines are associated a chance of 0.7, 0.5 and 0.3 of rolling heads respectively.
- An additional chart will be generated for sinners reliant on ego passives, chain passives or conditionals.
- For sinners with arbitrary power limits, e.g. bodysack passive, read their sinner.yaml file to view which numbers were used.
'''
print(message)

read_me = open('charts/read_me.txt', 'w+')
read_me.write(message)
read_me.close()

# file = open('sinners/w_corp_don_quixote.yaml', 'w+')
# file.write(yaml.dump(w_corp_don_quixote))
# file.close()

files = [file for file in listdir('sinners')]

for file in files:
	stream = open(f'sinners/{file}', 'r')
	sinner = yaml.load(stream, yaml.Loader)
	plt = sinner.gen_chart()
	# if is_file(f'charts/{sinner.name}.png')
	plt.savefig(f'charts/{sinner.name}.png')
	plt.close()

