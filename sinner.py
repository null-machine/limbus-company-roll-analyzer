import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, offense, skills):
		self.name = name
		self.offense = offense
		self.skills = skills
	
	def gen_summary(self):
		return f'{self.name} | agg: {round(self.agg, 2)} | raw: {round(self.raw, 2)} | var: {round(self.var, 2)}'
	
	def calibrate(self):
		for i in range(0, len(self.skills)):
			self.skills[i].user = self.name
			self.skills[i].type = f's{i}'
			self.skills[i].calibrate()
		
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1)
		
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
			ax[i].set_title(f'{self.skills[i].name} | agg: {round(self.skills[i].max_agg, 2)} | raw: {round(self.skills[i].max_raw, 2)} | var: {round(self.skills[i].var, 2)}')

		if self.name.endswith('_partial'):
			self.agg = (2 * self.skills[0].max_agg + 2 * self.skills[1].max_agg) / 4
			self.var = (2 * self.skills[0].var + 2 * self.skills[1].var) / 4
			self.raw = (2 * self.skills[0].max_raw + 2 * self.skills[1].max_raw) / 4
		else:
			self.agg = (2 * self.skills[0].max_agg + 2 * self.skills[1].max_agg + self.skills[2].max_agg) / 5
			self.var = (2 * self.skills[0].var + 2 * self.skills[1].var + self.skills[2].var) / 5
			self.raw = (2 * self.skills[0].max_raw + 2 * self.skills[1].max_raw + self.skills[2].max_raw) / 5
		
		fig.canvas.manager.set_window_title('Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies')
		fig.suptitle(self.gen_summary())
		fig.tight_layout()
		# plt.show()
		
		return plt
