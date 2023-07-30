import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, skills):
		self.name = name
		self.skills = skills
	
	def gen_summary(self, variant, weighting):
		# return self.name
		variant_name = ''
		if variant == 0:
			variant_name = 'adverse'
		elif variant == 1:
			variant_name = 'expected'
		elif variant == 2:
			variant_name = 'prime'
		ceil = max(self.skills[0].score_matrix[variant][4], self.skills[1].score_matrix[variant][4], self.skills[2].score_matrix[variant][4])

		if weighting == 'elite_bias':
			return f'{self.name} ({variant_name}) | clash: {round(self.elite_bias_score_matrix[variant][0], 2)}~{round(self.elite_bias_score_matrix[variant][1], 2)} | dmg: {round(self.elite_bias_score_matrix[variant][2], 2)}~{round(self.elite_bias_score_matrix[variant][3], 2)}, OL {round(self.elite_bias_score_matrix[variant][4], 2)} | ceil: {round(ceil, 2)}'
		elif weighting == 'full_deck':
			return f'{self.name} ({variant_name}) | clash: {round(self.full_deck_score_matrix[variant][0], 2)}~{round(self.full_deck_score_matrix[variant][1], 2)} | dmg: {round(self.full_deck_score_matrix[variant][2], 2)}~{round(self.full_deck_score_matrix[variant][3], 2)}, OL {round(self.full_deck_score_matrix[variant][4], 2)} | ceil: {round(ceil, 2)}'
	
	def gen_chart(self, variant):
	
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1, figsize=(11, 6))
		# plt.figure()
		
		for i in range(0, len(self.skills)):
			if self.skills[i].coin_type == 'minus':
				colors = ['#00ffff', '#95d8ff', '#c6aeff', '#e77aff', '#ff00ff']
			else:
				colors = ['#ff00ff', '#e77aff', '#c6aeff', '#95d8ff', '#00ffff']
			for j in range(0, 5):
				chances = []
				for k in self.skills[i].chance_tensor[variant]:
					chances.append(k[j])
				ax[i].step(self.skills[i].breakpoint_matrix[variant], chances, color=colors[j])
				
			ax[i].set(ylim=(0, 1.1), xlim=(0, 40), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 40.1, 2))
			ax[i].yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
			# ax[i].set_title(self.skills[i].gen_display(variant), fontsize=12, loc='right')
			ax[i].set_title(self.skills[i].gen_display(variant), fontsize=12)
		
		# fig.suptitle(self.gen_summary(variant))
		fig.tight_layout()
		# plt.subplots_adjust(right=0.72)
		plt.subplots_adjust(left=0.3)
		
		variant_name = ''
		if variant == 0:
			variant_name = 'adverse'
		elif variant == 1:
			variant_name = 'expected'
		elif variant == 2:
			variant_name = 'prime'
		
		
		title_text = ''
		title_text += f'{self.name}\n'
		title_text += f'({variant_name} state)\n'
		title_text += f'\n'
		
		side_text = ''
		side_text += f'elite bias rankings\n'
		side_text += f'ideal sp clash: {self.elite_bias_rank_matrix[variant][1]}/{self.competitor_count} ({round(self.elite_bias_rank_matrix[variant][1] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'ideal sp damage: {self.elite_bias_rank_matrix[variant][3]}/{self.competitor_count} ({round(self.elite_bias_rank_matrix[variant][3] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'worst sp clash: {self.elite_bias_rank_matrix[variant][0]}/{self.competitor_count} ({round(self.elite_bias_rank_matrix[variant][0] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'worst sp damage: {self.elite_bias_rank_matrix[variant][2]}/{self.competitor_count} ({round(self.elite_bias_rank_matrix[variant][2] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'\n'
		side_text += f'full deck rankings\n'
		side_text += f'ideal sp clash: {self.full_deck_rank_matrix[variant][1]}/{self.competitor_count} ({round(self.full_deck_rank_matrix[variant][1] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'ideal sp damage: {self.full_deck_rank_matrix[variant][3]}/{self.competitor_count} ({round(self.full_deck_rank_matrix[variant][3] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'worst sp clash: {self.full_deck_rank_matrix[variant][0]}/{self.competitor_count} ({round(self.full_deck_rank_matrix[variant][0] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'worst sp damage: {self.full_deck_rank_matrix[variant][2]}/{self.competitor_count} ({round(self.full_deck_rank_matrix[variant][2] / self.competitor_count * 100, 1)}%)\n'
		side_text += f'\n'
		for i in range(0, 3):
			side_text += f's{i + 1} rankings\n'
			side_text += f'ideal sp clash: {self.skills[i].rank_matrix[variant][1]}/{self.skills[i].competitor_count} ({round(self.skills[i].rank_matrix[variant][1] / self.skills[0].competitor_count * 100, 1)}%)\n'
			side_text += f'ideal sp damage: {self.skills[i].rank_matrix[variant][3]}/{self.skills[i].competitor_count} ({round(self.skills[i].rank_matrix[variant][3] / self.skills[0].competitor_count * 100, 1)}%)\n'
			side_text += f'worst sp clash: {self.skills[i].rank_matrix[variant][0]}/{self.skills[i].competitor_count} ({round(self.skills[i].rank_matrix[variant][0] / self.skills[0].competitor_count * 100, 1)}%)\n'
			side_text += f'worst sp damage: {self.skills[i].rank_matrix[variant][2]}/{self.skills[i].competitor_count} ({round(self.skills[i].rank_matrix[variant][2] / self.skills[0].competitor_count * 100, 1)}%)\n'
			side_text += f'clash ceiling: {self.skills[i].rank_matrix[variant][4]}/{self.skills[i].competitor_count} ({round(self.skills[i].rank_matrix[variant][4] / self.skills[0].competitor_count * 100, 1)}%)\n'
			side_text += f'\n'
			
		plt.gcf().text(0.02, 0.83, title_text, fontsize=13)
		plt.gcf().text(0.02, 0.01, side_text, fontsize=9)
		
		
		# plt.show()
		return plt
	
	def calibrate(self):
		for i in range(0, len(self.skills)):
			self.skills[i].calibrate(self.name, f's{i + 1}')
		
		self.has_prime = not all(not x.has_prime for x in self.skills)
		self.has_weak = not all(not x.has_weak for x in self.skills)
		
		# [min clash, max clash, min damage, max damage, offense]
		self.full_deck_score_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		self.elite_bias_score_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		
		self.elite_bias_rank_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		self.full_deck_rank_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		
		for i in range(0, 3):
			self.full_deck_score_matrix[i][0] = (3 * self.skills[0].score_matrix[i][0] + 2 * self.skills[1].score_matrix[i][0] + self.skills[2].score_matrix[i][0]) / 6
			self.full_deck_score_matrix[i][1] = (3 * self.skills[0].score_matrix[i][1] + 2 * self.skills[1].score_matrix[i][1] + self.skills[2].score_matrix[i][1]) / 6
			self.full_deck_score_matrix[i][2] = (3 * self.skills[0].score_matrix[i][2] + 2 * self.skills[1].score_matrix[i][2] + self.skills[2].score_matrix[i][2]) / 6
			self.full_deck_score_matrix[i][3] = (3 * self.skills[0].score_matrix[i][3] + 2 * self.skills[1].score_matrix[i][3] + self.skills[2].score_matrix[i][3]) / 6
			self.elite_bias_score_matrix[i][0] = (self.skills[0].score_matrix[i][0] + 2 * self.skills[1].score_matrix[i][0] + self.skills[2].score_matrix[i][0]) / 4
			self.elite_bias_score_matrix[i][1] = (self.skills[0].score_matrix[i][1] + 2 * self.skills[1].score_matrix[i][1] + self.skills[2].score_matrix[i][1]) / 4
			self.elite_bias_score_matrix[i][2] = (self.skills[0].score_matrix[i][2] + 2 * self.skills[1].score_matrix[i][2] + self.skills[2].score_matrix[i][2]) / 4
			self.elite_bias_score_matrix[i][3] = (self.skills[0].score_matrix[i][3] + 2 * self.skills[1].score_matrix[i][3] + self.skills[2].score_matrix[i][3]) / 4
			
			if i == 0:
				self.full_deck_score_matrix[i][4] = (3 * self.skills[0].stats[3] + self.skills[0].weak_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].weak_bonuses[3] + self.skills[2].stats[3] + self.skills[2].weak_bonuses[3]) / 6
				self.elite_bias_score_matrix[i][4] = (self.skills[0].stats[3] + self.skills[0].weak_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].weak_bonuses[3] + self.skills[2].stats[3] + self.skills[2].weak_bonuses[3]) / 4
			elif i == 1:
				self.full_deck_score_matrix[i][4] = (3 * self.skills[0].stats[3] + 2 * self.skills[1].stats[3] + self.skills[2].stats[3]) / 6
				self.elite_bias_score_matrix[i][4] = (self.skills[0].stats[3] + 2 * self.skills[1].stats[3] + self.skills[2].stats[3]) / 4
			elif i == 2:
				self.full_deck_score_matrix[i][4] = (3 * self.skills[0].stats[3] + self.skills[0].prime_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].prime_bonuses[3] + self.skills[2].stats[3] + self.skills[2].prime_bonuses[3]) / 6
				self.elite_bias_score_matrix[i][4] = (self.skills[0].stats[3] + self.skills[0].prime_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].prime_bonuses[3] + self.skills[2].stats[3] + self.skills[2].prime_bonuses[3]) / 4
			

		# self.offense = (3 * self.skills[0].offense + 2 * self.skills[1].offense + self.skills[2].offense) / 6
