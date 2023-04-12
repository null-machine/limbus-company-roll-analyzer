from scipy.stats import binom

class Skill:

	def __init__(self, name, base_power, coin_count, coin_power):
		self.name = name
		self.base_power = base_power
		self.coin_count = coin_count
		self.coin_power = coin_power
		self.user = ''
		self.type = ''
	
	def __lt__(self, other):
		if self.max_aggregate == other.max_aggregate:
			return self.variance > other.variance
		return self.max_aggregate < other.max_aggregate
		# if self.variance == other.variance:
		# 	return self.aggregate < other.aggregate
		# return self.variance > other.variance

	def __gt__(self, other):
		return other.__lt__(self)

	def __eq__(self, other):
		return self.max_aggregate == other.max_aggregate and self.variance == other.variance

	def gen_display_str(self):
		return f'{self.type} {self.user} | {self.name} | aggregate: {round(self.max_aggregate, 2)} | variance: {round(self.variance, 2)}'

	def gen_breakpoints(self, offense, enemy_offense=35):
		offense_power = (offense - enemy_offense) / 5
		effective_base_power = self.base_power + offense_power
		breakpoints = []
		max_chance = []
		reg_chance = []
		min_chance = []
		breakpoints.append(0)
		max_chance.append(1)
		reg_chance.append(1)
		min_chance.append(1)
		self.max_aggregate = 0
		self.reg_aggregate = 0
		self.min_aggregate = 0
		for i in range(self.coin_count + 1):
			breakpoints.append(effective_base_power + i * self.coin_power)
			max_chance.append(self.eval_chance(0.95, i))
			reg_chance.append(self.eval_chance(0.5, i))
			min_chance.append(self.eval_chance(0.05, i))
			# max_chance.append(self.eval_chance(0.7, i))
			# reg_chance.append(self.eval_chance(0.5, i))
			# min_chance.append(self.eval_chance(0.3, i))
			delta_x = effective_base_power + i * self.coin_power - breakpoints[i]
			self.max_aggregate += delta_x * max_chance[i + 1]
			self.reg_aggregate += delta_x * reg_chance[i + 1]
			self.min_aggregate += delta_x * min_chance[i + 1]
		self.variance = (self.max_aggregate - self.min_aggregate) / self.max_aggregate
		return breakpoints, min_chance, reg_chance, max_chance
	
	def eval_chance(self, heads_chance, required_heads):
		if required_heads <= 0:
			return 1
		chance = 0
		coins_remaining = self.coin_count
		while coins_remaining >= required_heads:
			k = coins_remaining - required_heads
			chance += (1 - chance) * (binom.cdf(k, coins_remaining, 1 - heads_chance))
			coins_remaining -= 1
		return chance