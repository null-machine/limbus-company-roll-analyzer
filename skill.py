from scipy.stats import binom
import math

class Skill:

	def __init__(self, name, coin_type, stats, damage_bonuses, prime_bonuses, prime_damage_bonuses, weak_bonuses, weak_damage_bonuses):
		self.name = name
		self.coin_type = coin_type
		self.stats = stats
		self.damage_bonuses = damage_bonuses
		self.prime_bonuses = prime_bonuses
		self.prime_damage_bonuses = prime_damage_bonuses
		self.weak_bonuses = weak_bonuses
		self.weak_damage_bonuses = weak_damage_bonuses
	
	def gen_summary(self, variant):
		return f'{self.type} {self.user} | {self.gen_display(variant)}'
	
	def gen_display(self, variant):
		# return self.name
		offense = self.stats[3]
		if variant == 0:
			offense += self.weak_bonuses[3]
		elif variant == 2:
			offense += self.prime_bonuses[3]
		return f'{self.name} | clash: {round(self.score_matrix[variant][0], 2)}~{round(self.score_matrix[variant][1], 2)} | dmg: {round(self.score_matrix[variant][2], 2)}~{round(self.score_matrix[variant][3], 2)} @ {offense} | ceil: {round(self.score_matrix[variant][4], 2)}'
		
	def calibrate(self, user, slot):
		self.user = user
		self.slot = slot
		
		self.has_prime = not all(x == 0 for x in self.prime_bonuses) or not all(x == 0 for x in self.prime_damage_bonuses)
		self.has_weak = not all(x == 0 for x in self.weak_bonuses) or not all(x == 0 for x in self.weak_damage_bonuses)
		
		# scores are used for sinner comparison
		# [min clash, max clash, min damage, max damage, ceil]
		self.score_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		self.rank_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		
		# breakpoints and chances are used to generate scores and charts
		# [weak[], expected[], prime[]]
		self.breakpoint_matrix = [[], [], []]
		# [weak[[sanity levels]], expected[[sanity levels]], prime[[sanity levels]]] (sanity levels are 0.05 to 0.95)
		self.chance_tensor = [[], [], []]
		
		for i in range(0, 4):
			self.prime_damage_bonuses[i] += self.damage_bonuses[i]
			self.weak_damage_bonuses[i] += self.damage_bonuses[i]
		
		self.calibrate_variant(0, self.stats[0] + self.weak_bonuses[0], self.stats[1] + self.weak_bonuses[1], self.stats[2] + self.weak_bonuses[2], self.stats[3] + self.weak_bonuses[3], self.weak_damage_bonuses)
		self.calibrate_variant(1, self.stats[0], self.stats[1], self.stats[2], self.stats[3], self.damage_bonuses)
		self.calibrate_variant(2, self.stats[0] + self.prime_bonuses[0], self.stats[1] + self.prime_bonuses[1], self.stats[2] + self.prime_bonuses[2], self.stats[3] + self.prime_bonuses[3], self.prime_damage_bonuses)
		
		
		return
		
	def calibrate_variant(self, variant, base_power, coin_power, coin_count, offense, damage_bonuses):
		effective_base_power = base_power + offense / 3
		self.breakpoint_matrix[variant].append(0)
		if effective_base_power > 0:
			self.chance_tensor[variant].append([1, 1, 1, 1, 1])
		else:
			self.chance_tensor[variant].append([0, 0, 0, 0, 0])
		for i in range(coin_count + 1):
			self.breakpoint_matrix[variant].append(effective_base_power + i * coin_power)
			if self.coin_type == 'minus':
				self.chance_tensor[variant].append([self.eval_chance_minus(coin_count, 0.05, i), self.eval_chance_minus(coin_count, 0.275, i), self.eval_chance_minus(coin_count, 0.5, i), self.eval_chance_minus(coin_count, 0.725, i), self.eval_chance_minus(coin_count, 0.95, i)])
			else:
				self.chance_tensor[variant].append([self.eval_chance(coin_count, 0.05, i), self.eval_chance(coin_count, 0.275, i), self.eval_chance(coin_count, 0.5, i), self.eval_chance(coin_count, 0.725, i), self.eval_chance(coin_count, 0.95, i)])
			delta_x = effective_base_power + i * coin_power - self.breakpoint_matrix[variant][i]
			self.score_matrix[variant][0] += delta_x * self.chance_tensor[variant][i + 1][0] # min clash += dx * min chance
			self.score_matrix[variant][1] += delta_x * self.chance_tensor[variant][i + 1][4] # max clash += dx * max chance
		
		self.score_matrix[variant][4] += effective_base_power + coin_count * coin_power
		
		base_power += damage_bonuses[0]
		coin_power += damage_bonuses[1]
		coin_count += damage_bonuses[2]
		offense += damage_bonuses[3]
		
		for i in range(coin_count + 1):
			if i > 0:
				if self.coin_type == 'minus':
					self.score_matrix[variant][2] += base_power + (i - 1) * coin_power if base_power + (i - 1) * coin_power > 0 else 0
					self.score_matrix[variant][3] += base_power + coin_count * coin_power
				else:
					self.score_matrix[variant][2] += base_power
					self.score_matrix[variant][3] += base_power + i * coin_power
		
		return
	
	def eval_chance(self, coin_count, heads_chance, required_heads):
		if required_heads <= 0:
			return 1
		chance = 0
		coins_remaining = coin_count
		while coins_remaining >= required_heads:
			k = coins_remaining - required_heads
			chance += (1 - chance) * (binom.cdf(k, coins_remaining, 1 - heads_chance))
			coins_remaining -= 1
		return chance
	
	def eval_chance_minus(self, coin_count, heads_chance, required_heads):
		if required_heads < coin_count:
			return 1
		final_chance = 0
		coins_remaining = coin_count
		while coins_remaining > 0:
			chance = math.pow(heads_chance, coins_remaining)
			temp = 1 - final_chance
			final_chance += chance * temp
			coins_remaining -= 1
		return final_chance
		
	