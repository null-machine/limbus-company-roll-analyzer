import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, skills):
		self.name = name
		self.skills = skills
	
	def gen_summary(self):
		return f'{self.name} | agg: {round(self.min_agg, 2)}~{round(self.max_agg, 2)} | dmg: {round(self.min_dmg, 2)}~{round(self.max_dmg, 2)} @ {round(self.offense, 2)}'
	
	def gen_chart(self):
	
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1, figsize=(9, 5))
		# plt.figure()
		
		for i in range(0, len(self.skills)):
			if self.skills[i].coin_type == 'minus':
				min_color = '#00ffff'
				max_color = '#ff00ff'
				pos_color = '#e77aff'
				neg_color = '#95d8ff'
			else:
				min_color = '#ff00ff'
				max_color = '#00ffff'
				pos_color = '#95d8ff'
				neg_color = '#e77aff'
			ax[i].step(self.skills[i].breakpoints, self.skills[i].pos_chance, color=pos_color)
			ax[i].step(self.skills[i].breakpoints, self.skills[i].neg_chance, color=neg_color)
			ax[i].step(self.skills[i].breakpoints, self.skills[i].reg_chance, color='#c6aeff')
			ax[i].step(self.skills[i].breakpoints, self.skills[i].min_chance, color=min_color)
			ax[i].step(self.skills[i].breakpoints, self.skills[i].max_chance, color=max_color)
			ax[i].set(ylim=(0, 1.1), xlim=(0, 40), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 40.1, 2))
			ax[i].yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
			ax[i].set_title(self.skills[i].gen_display()) # fontsize=10
		
		fig.canvas.manager.set_window_title('Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies')
		fig.suptitle(self.gen_summary())
		fig.tight_layout()
		plt.subplots_adjust(right=0.7)
		
		
		if self.name.endswith('_weak') or self.name.endswith('_prime') or self.name.endswith('_partial'):
			side_text = "prime, weak and partial\n"
			side_text += "chart rankings require\n"
			side_text += "more interpretation than\n"
			side_text += "usual, so they are\n"
			side_text += "not printed here to\n"
			side_text += "avoid being misleading.\n"
			plt.gcf().text(0.74, 0.4, side_text, fontsize=9)
		else:
			side_text = f"3x|2x|1x average rankings\n"
			side_text += f"ideal sp clash: {self.full_deck_ideal_clash_rank}/{self.competitor_count} ({round(self.full_deck_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp clash: {self.full_deck_zero_clash_rank}/{self.competitor_count} ({round(self.full_deck_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"ideal sp damage: {self.full_deck_ideal_damage_rank}/{self.competitor_count} ({round(self.full_deck_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp damage: {self.full_deck_zero_damage_rank}/{self.competitor_count} ({round(self.full_deck_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"\n"
			side_text += f"1x|2x|1x average rankings\n"
			side_text += f"ideal sp clash: {self.strong_bias_ideal_clash_rank}/{self.competitor_count} ({round(self.strong_bias_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp clash: {self.strong_bias_zero_clash_rank}/{self.competitor_count} ({round(self.strong_bias_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"ideal sp damage: {self.strong_bias_ideal_damage_rank}/{self.competitor_count} ({round(self.strong_bias_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp damage: {self.strong_bias_zero_damage_rank}/{self.competitor_count} ({round(self.strong_bias_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"\n"
			side_text += f"s1 rankings\n"
			side_text += f"ideal sp clash: {self.s1_ideal_clash_rank}/{self.competitor_count} ({round(self.s1_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp clash: {self.s1_zero_clash_rank}/{self.competitor_count} ({round(self.s1_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"ideal sp damage: {self.s1_ideal_damage_rank}/{self.competitor_count} ({round(self.s1_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp damage: {self.s1_zero_damage_rank}/{self.competitor_count} ({round(self.s1_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"\n"
			side_text += f"s2 rankings\n"
			side_text += f"ideal sp clash: {self.s2_ideal_clash_rank}/{self.competitor_count} ({round(self.s2_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp clash: {self.s2_zero_clash_rank}/{self.competitor_count} ({round(self.s2_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"ideal sp damage: {self.s2_ideal_damage_rank}/{self.competitor_count} ({round(self.s2_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp damage: {self.s2_zero_damage_rank}/{self.competitor_count} ({round(self.s2_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"\n"
			side_text += f"s3 rankings\n"
			side_text += f"ideal sp clash: {self.s3_ideal_clash_rank}/{self.competitor_count} ({round(self.s3_ideal_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp clash: {self.s3_zero_clash_rank}/{self.competitor_count} ({round(self.s3_zero_clash_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"ideal sp damage: {self.s3_ideal_damage_rank}/{self.competitor_count} ({round(self.s3_ideal_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"zero sp damage: {self.s3_zero_damage_rank}/{self.competitor_count} ({round(self.s3_zero_damage_rank / self.competitor_count * 100, 1)}%)\n"
			side_text += f"\n"
			plt.gcf().text(0.73, -0.02, side_text, fontsize=9)
		
		
		# plt.show()
		return plt
		return 0
	
	def calibrate(self):
		for i in range(0, len(self.skills)):
			self.skills[i].calibrate(self.name, f's{i + 1}')
			
		# self.turn_one_max_agg = (1 * self.skills[0].max_agg + 2 * self.skills[1].max_agg + self.skills[2].max_agg) / 6
		# self.turn_one_min_agg = (1 * self.skills[0].min_agg + 2 * self.skills[1].min_agg + self.skills[2].min_agg) / 6
		# self.turn_one_max_dmg = (1 * self.skills[0].max_dmg + 2 * self.skills[1].max_dmg + self.skills[2].max_dmg) / 6
		# self.turn_one_min_dmg = (1 * self.skills[0].min_dmg + 2 * self.skills[1].min_dmg + self.skills[2].min_dmg) / 6
		# self.turn_one_offense = (1 * self.skills[0].offense + 2 * self.skills[1].offense + self.skills[2].offense) / 6
		
		# self.max_agg = (3 * self.skills[0].max_agg + 2 * self.skills[1].max_agg + self.skills[2].max_agg) / 6
		# self.min_agg = (3 * self.skills[0].min_agg + 2 * self.skills[1].min_agg + self.skills[2].min_agg) / 6
		# self.max_dmg = (3 * self.skills[0].max_dmg + 2 * self.skills[1].max_dmg + self.skills[2].max_dmg) / 6
		# self.min_dmg = (3 * self.skills[0].min_dmg + 2 * self.skills[1].min_dmg + self.skills[2].min_dmg) / 6
		# self.offense = (3 * self.skills[0].offense + 2 * self.skills[1].offense + self.skills[2].offense) / 6
