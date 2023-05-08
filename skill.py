from scipy.stats import binom
import math

class Skill:

	def __init__(self, name, offense, base_power, coin_count, coin_power, coin_type):
		self.name = name
		self.offense = offense
		self.base_power = base_power
		self.coin_count = coin_count
		self.coin_power = coin_power
		self.coin_type = coin_type
	
	def gen_summary(self):
		return f'{self.type} {self.user} | {self.gen_display()}'
	
	def gen_display(self):
		return f'{self.name} | agg: {round(self.min_agg, 2)}~{round(self.max_agg, 2)} | raw: {round(self.min_raw, 2)}~{round(self.max_raw, 2)} @ {self.offense}'

	def calibrate(self, enemy_offense=35):
		offense_delta = self.offense - enemy_offense
		effective_base_power = self.base_power + offense_delta / 5
		breakpoints = []
		max_chance = []
		reg_chance = []
		min_chance = []
		pos_chance = []
		neg_chance = []
		breakpoints.append(0)
		if effective_base_power > 0:
			max_chance.append(1)
			reg_chance.append(1)
			min_chance.append(1)
			pos_chance.append(1)
			neg_chance.append(1)
		else:
			max_chance.append(0)
			reg_chance.append(0)
			min_chance.append(0)
			pos_chance.append(0)
			neg_chance.append(0)
		self.max_agg = 0
		self.min_agg = 0
		self.max_raw = 0
		self.min_raw = 0
		base_for_raw = 0 if self.base_power < 0 else self.base_power
		for i in range(self.coin_count + 1):
			breakpoints.append(effective_base_power + i * self.coin_power)
			if i > 0:
				if self.coin_type == 'minus':
					self.max_raw += self.base_power + self.coin_count * self.coin_power
					self.min_raw += self.base_power + (i - 1) * self.coin_power if self.base_power + (i - 1) * self.coin_power > 0 else 0
				else:
					self.max_raw += self.base_power + i * self.coin_power
					self.min_raw += self.base_power
			if self.coin_type == 'minus':
				max_chance.append(self.eval_chance_minus(0.95, i))
				reg_chance.append(self.eval_chance_minus(0.5, i))
				min_chance.append(self.eval_chance_minus(0.05, i))
				pos_chance.append(self.eval_chance_minus(0.725, i))
				neg_chance.append(self.eval_chance_minus(0.275, i))
			else:
				max_chance.append(self.eval_chance(0.95, i))
				reg_chance.append(self.eval_chance(0.5, i))
				min_chance.append(self.eval_chance(0.05, i))
				pos_chance.append(self.eval_chance(0.725, i))
				neg_chance.append(self.eval_chance(0.275, i))
			# max_chance.append(self.eval_chance(0.7, i))
			# reg_chance.append(self.eval_chance(0.5, i))
			# min_chance.append(self.eval_chance(0.3, i))
			delta_x = effective_base_power + i * self.coin_power - breakpoints[i]
			self.max_agg += delta_x * max_chance[i + 1]
			self.min_agg += delta_x * min_chance[i + 1]
		# self.var = (self.max_agg - self.min_agg) / self.max_agg
		self.var = (self.max_raw - self.min_raw) / self.max_raw
		# raw_multiplier = 1 + (offense - enemy_offense) / (abs(offense - enemy_offense) + 25)
		
		# raw_multiplier = 1 + offense_delta / 100 # https://www.desmos.com/calculator/ftlrxxrzai
		raw_multiplier = 1
		self.max_raw *= raw_multiplier
		self.min_raw *= raw_multiplier
		return breakpoints, max_chance, reg_chance, min_chance, pos_chance, neg_chance
	
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
	
	def eval_chance_minus(self, heads_chance, required_heads):
		if required_heads < self.coin_count:
			return 1
		final_chance = 0
		coins_remaining = self.coin_count
		while coins_remaining > 0:
			chance = math.pow(heads_chance, coins_remaining)
			temp = 1 - final_chance
			final_chance += chance * temp
			coins_remaining -= 1
		return final_chance