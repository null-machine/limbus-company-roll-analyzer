import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, skills):
		self.name = name
		self.skills = skills
	
	def gen_summary(self):
		return f'{self.name} | agg: {round(self.min_agg, 2)}~{round(self.max_agg, 2)} | raw: {round(self.min_raw, 2)}~{round(self.max_raw, 2)} ({round(self.offense, 2)})'
	
	def calibrate(self):
		for i in range(0, len(self.skills)):
			self.skills[i].user = self.name
			self.skills[i].type = f's{i}'
			self.skills[i].calibrate()
		
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1, figsize=(7, 5))
		# plt.figure()
		
		for i in range(0, len(self.skills)):
			breakpoints, max_chance, reg_chance, min_chance = self.skills[i].calibrate()
			if self.skills[i].coin_type == 'minus':
				min_color = 'cyan'
				max_color = 'magenta'
			else:
				min_color = 'magenta'
				max_color = 'cyan'
			ax[i].step(breakpoints, min_chance, color=min_color)
			ax[i].step(breakpoints, reg_chance, color='grey')
			ax[i].step(breakpoints, max_chance, color=max_color)
			ax[i].set(ylim=(0, 1.1), xlim=(0, 40), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 40.1, 2))
			ax[i].yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
			ax[i].set_title(self.skills[i].gen_display()) # fontsize=10

		if self.name.endswith('_partial'):
			self.max_agg = (3 * self.skills[0].max_agg + 2 * self.skills[1].max_agg) / 5
			self.min_agg = (3 * self.skills[0].min_agg + 2 * self.skills[1].min_agg) / 5
			self.max_raw = (3 * self.skills[0].max_raw + 2 * self.skills[1].max_raw) / 5
			self.min_raw = (3 * self.skills[0].min_raw + 2 * self.skills[1].min_raw) / 5
			self.offense = (3 * self.skills[0].offense + 2 * self.skills[1].offense) / 5
		else:
			self.max_agg = (3 * self.skills[0].max_agg + 2 * self.skills[1].max_agg + self.skills[2].max_agg) / 6
			self.min_agg = (3 * self.skills[0].min_agg + 2 * self.skills[1].min_agg + self.skills[2].min_agg) / 6
			self.max_raw = (3 * self.skills[0].max_raw + 2 * self.skills[1].max_raw + self.skills[2].max_raw) / 6
			self.min_raw = (3 * self.skills[0].min_raw + 2 * self.skills[1].min_raw + self.skills[2].min_raw) / 6
			self.offense = (3 * self.skills[0].offense + 2 * self.skills[1].offense + self.skills[2].offense) / 6
		
		fig.canvas.manager.set_window_title('Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies')
		fig.suptitle(self.gen_summary())
		fig.tight_layout()
		# plt.show()
		
		return plt
