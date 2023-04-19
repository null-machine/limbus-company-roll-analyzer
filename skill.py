from scipy.stats import binom
import math

class Skill:

	def __init__(self, name, base_power, coin_count, coin_power):
		self.name = name
		self.base_power = base_power
		self.coin_count = coin_count
		self.coin_power = coin_power
		self.user = ''
		self.type = ''
	
	def gen_display_str(self):
		return f'{self.type} {self.user} | {self.name} | agg: {round(self.aggregate, 2)} | raw: {round(self.damage, 2)} | var: {round(self.variance, 2)}'

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
		self.aggregate = 0
		self.reg_aggregate = 0
		self.min_aggregate = 0
		self.damage = 0
		self.min_damage = 0
		for i in range(self.coin_count + 1):
			breakpoints.append(effective_base_power + i * self.coin_power)
			if i > 0:
				# self.damage += self.base_power + i * self.coin_power
				self.damage += effective_base_power + i * self.coin_power
				self.min_damage += effective_base_power
			max_chance.append(self.eval_chance(0.95, i))
			reg_chance.append(self.eval_chance(0.5, i))
			min_chance.append(self.eval_chance(0.05, i))
			# max_chance.append(self.eval_chance(0.7, i))
			# reg_chance.append(self.eval_chance(0.5, i))
			# min_chance.append(self.eval_chance(0.3, i))
			delta_x = effective_base_power + i * self.coin_power - breakpoints[i]
			self.aggregate += delta_x * max_chance[i + 1]
			self.reg_aggregate += delta_x * reg_chance[i + 1]
			self.min_aggregate += delta_x * min_chance[i + 1]
		# self.variance = (self.aggregate - self.min_aggregate) / self.aggregate
		self.variance = (self.damage - self.min_damage) / self.damage
		# damage_multiplier = 1 + (offense - enemy_offense) / (abs(offense - enemy_offense) + 25)
		# damage_multiplier = 0.5 + 0.5 * math.sqrt(offense / 25) # https://www.desmos.com/calculator/sjvjbrsu5f
		damage_multiplier = 1 + offense / 100 - 0.25 # https://www.desmos.com/calculator/zqwq99r9i9
		self.damage *= damage_multiplier
		self.min_damage *= damage_multiplier
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