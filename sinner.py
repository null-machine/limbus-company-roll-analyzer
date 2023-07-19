import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, skills):
		self.name = name
		self.skills = skills
	
	def gen_summary(self, variant):
		# return self.name
		variant_name = ''
		if variant == 0:
			variant_name = "no bonuses"
		elif variant == 1:
			variant_name = "expected"
		elif variant == 2:
			variant_name = "prime"
		return f'{self.name} ({variant_name}) | clash: {round(self.elite_bias_scores_matrix[variant][0], 2)}~{round(self.elite_bias_scores_matrix[variant][1], 2)} | dmg: {round(self.elite_bias_scores_matrix[variant][2], 2)}~{round(self.elite_bias_scores_matrix[variant][3], 2)} @ {round(self.elite_bias_scores_matrix[variant][4], 2)}'
	
	def gen_chart(self, variant):
	
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1, figsize=(9, 5))
		# plt.figure()
		
		for i in range(0, len(self.skills)):
			if self.skills[i].coin_type == 'minus':
				colors = ['#00ffff', '#95d8ff', '#c6aeff', '#e77aff', '#ff00ff']
			else:
				colors = ['#ff00ff', '#e77aff', '#c6aeff', '#95d8ff', '#00ffff']
			for j in range(0, 5):
				chances = []
				for k in self.skills[i].chances_tensor[variant]:
					chances.append(k[j])
				ax[i].step(self.skills[i].breakpoints_matrix[variant], chances, color=colors[j])
				
			ax[i].set(ylim=(0, 1.1), xlim=(0, 40), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 40.1, 2))
			ax[i].yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
			ax[i].set_title(self.skills[i].gen_display(variant))
		
		fig.suptitle(self.gen_summary(variant))
		fig.tight_layout()
		plt.subplots_adjust(right=0.7)
		
		side_text = ''
		side_text += f"1x|2x|1x average rankings\n"
		side_text += f"ideal sp clash: {self.elite_bias_ranks_matrix[variant][1]}/{self.competitor_count} ({round(self.elite_bias_ranks_matrix[variant][1] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"worst sp clash: {self.elite_bias_ranks_matrix[variant][0]}/{self.competitor_count} ({round(self.elite_bias_ranks_matrix[variant][0] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"ideal sp damage: {self.elite_bias_ranks_matrix[variant][3]}/{self.competitor_count} ({round(self.elite_bias_ranks_matrix[variant][3] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"worst sp damage: {self.elite_bias_ranks_matrix[variant][2]}/{self.competitor_count} ({round(self.elite_bias_ranks_matrix[variant][2] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"\n"
		side_text += f"3x|2x|1x average rankings\n"
		side_text += f"ideal sp clash: {self.full_deck_ranks_matrix[variant][1]}/{self.competitor_count} ({round(self.full_deck_ranks_matrix[variant][1] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"worst sp clash: {self.full_deck_ranks_matrix[variant][0]}/{self.competitor_count} ({round(self.full_deck_ranks_matrix[variant][0] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"ideal sp damage: {self.full_deck_ranks_matrix[variant][3]}/{self.competitor_count} ({round(self.full_deck_ranks_matrix[variant][3] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"worst sp damage: {self.full_deck_ranks_matrix[variant][2]}/{self.competitor_count} ({round(self.full_deck_ranks_matrix[variant][2] / self.competitor_count * 100, 1)}%)\n"
		side_text += f"\n"
		# side_text += f"s1 rankings\n"
		# side_text += f"ideal sp clash: {self.s1_ideal_clash_rank}/{self.competitor_count} ({round(self.s1_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"worst sp clash: {self.s1_zero_clash_rank}/{self.competitor_count} ({round(self.s1_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"ideal sp damage: {self.s1_ideal_damage_rank}/{self.competitor_count} ({round(self.s1_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"worst sp damage: {self.s1_zero_damage_rank}/{self.competitor_count} ({round(self.s1_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"\n"
		# side_text += f"s2 rankings\n"
		# side_text += f"ideal sp clash: {self.s2_ideal_clash_rank}/{self.competitor_count} ({round(self.s2_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"worst sp clash: {self.s2_zero_clash_rank}/{self.competitor_count} ({round(self.s2_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"ideal sp damage: {self.s2_ideal_damage_rank}/{self.competitor_count} ({round(self.s2_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"worst sp damage: {self.s2_zero_damage_rank}/{self.competitor_count} ({round(self.s2_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"\n"
		# side_text += f"s3 rankings\n"
		# side_text += f"ideal sp clash: {self.s3_ideal_clash_rank}/{self.competitor_count} ({round(self.s3_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"worst sp clash: {self.s3_zero_clash_rank}/{self.competitor_count} ({round(self.s3_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"ideal sp damage: {self.s3_ideal_damage_rank}/{self.competitor_count} ({round(self.s3_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"worst sp damage: {self.s3_zero_damage_rank}/{self.competitor_count} ({round(self.s3_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
		# side_text += f"\n"
		# plt.gcf().text(0.73, -0.02, side_text, fontsize=9)
		# plt.gcf().text(0.73, 0.2, side_text, fontsize=9)
		
		
		# plt.show()
		return plt
	
	def calibrate(self):
		for i in range(0, len(self.skills)):
			self.skills[i].calibrate(self.name, f's{i + 1}')
		
		# [min clash, max clash, min damage, max damage, offense]
		self.full_deck_scores_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		self.elite_bias_scores_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		self.elite_bias_ranks_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		self.full_deck_ranks_matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
		
		for i in range(0, 3):
			self.full_deck_scores_matrix[i][0] = (3 * self.skills[0].scores_matrix[i][0] + 2 * self.skills[1].scores_matrix[i][0] + self.skills[2].scores_matrix[i][0]) / 6
			self.full_deck_scores_matrix[i][1] = (3 * self.skills[0].scores_matrix[i][1] + 2 * self.skills[1].scores_matrix[i][1] + self.skills[2].scores_matrix[i][1]) / 6
			self.full_deck_scores_matrix[i][2] = (3 * self.skills[0].scores_matrix[i][2] + 2 * self.skills[1].scores_matrix[i][2] + self.skills[2].scores_matrix[i][2]) / 6
			self.full_deck_scores_matrix[i][3] = (3 * self.skills[0].scores_matrix[i][3] + 2 * self.skills[1].scores_matrix[i][3] + self.skills[2].scores_matrix[i][3]) / 6
			self.elite_bias_scores_matrix[i][0] = (self.skills[0].scores_matrix[i][0] + 2 * self.skills[1].scores_matrix[i][0] + self.skills[2].scores_matrix[i][0]) / 4
			self.elite_bias_scores_matrix[i][1] = (self.skills[0].scores_matrix[i][1] + 2 * self.skills[1].scores_matrix[i][1] + self.skills[2].scores_matrix[i][1]) / 4
			self.elite_bias_scores_matrix[i][2] = (self.skills[0].scores_matrix[i][2] + 2 * self.skills[1].scores_matrix[i][2] + self.skills[2].scores_matrix[i][2]) / 4
			self.elite_bias_scores_matrix[i][3] = (self.skills[0].scores_matrix[i][3] + 2 * self.skills[1].scores_matrix[i][3] + self.skills[2].scores_matrix[i][3]) / 4
			
			if i == 0:
				self.full_deck_scores_matrix[i][4] = (3 * self.skills[0].stats[3] + self.skills[0].weak_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].weak_bonuses[3] + self.skills[2].stats[3] + self.skills[2].weak_bonuses[3]) / 6
				self.elite_bias_scores_matrix[i][4] = (self.skills[0].stats[3] + self.skills[0].weak_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].weak_bonuses[3] + self.skills[2].stats[3] + self.skills[2].weak_bonuses[3]) / 4
			elif i == 1:
				self.full_deck_scores_matrix[i][4] = (3 * self.skills[0].stats[3] + 2 * self.skills[1].stats[3] + self.skills[2].stats[3]) / 6
				self.elite_bias_scores_matrix[i][4] = (self.skills[0].stats[3] + 2 * self.skills[1].stats[3] + self.skills[2].stats[3]) / 4
			elif i == 2:
				self.full_deck_scores_matrix[i][4] = (3 * self.skills[0].stats[3] + self.skills[0].prime_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].prime_bonuses[3] + self.skills[2].stats[3] + self.skills[2].prime_bonuses[3]) / 6
				self.elite_bias_scores_matrix[i][4] = (self.skills[0].stats[3] + self.skills[0].prime_bonuses[3] + 2 * self.skills[1].stats[3] + self.skills[1].prime_bonuses[3] + self.skills[2].stats[3] + self.skills[2].prime_bonuses[3]) / 4
			

		# self.offense = (3 * self.skills[0].offense + 2 * self.skills[1].offense + self.skills[2].offense) / 6
