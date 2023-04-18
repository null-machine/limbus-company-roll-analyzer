import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, offense, s1, s2, s3):
		self.name = name
		self.offense = self.offense
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
	
	def __lt__(self, other):
		if self.aggregate == other.aggregate:
			return self.variance > other.variance
		return self.aggregate < other.aggregate
		# if self.variance == other.variance:
		# 	return self.aggregate < other.aggregate
		# return self.variance > other.variance

	def __gt__(self, other):
		return other.__lt__(self)

	def __eq__(self, other):
		return self.aggregate == other.aggregate and self.variance == other.variance
	
	def gen_display_str(self):
		return f'{self.name} | agg: {round(self.aggregate, 2)} | var: {round(self.variance, 2)} | raw: {round(self.damage, 2)}'
		
	def gen_chart(self):
		self.s1.user = self.name
		self.s1.type = 's1'
		self.s2.user = self.name
		self.s2.type = 's2'
		self.s3.user = self.name
		self.s3.type = 's3'
		
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1)

		s1_breakpoints, s1_min_chance, s1_reg_chance, s1_max_chance = self.s1.gen_breakpoints(self.offense)
		ax[0].step(s1_breakpoints, s1_min_chance, color='magenta')
		ax[0].step(s1_breakpoints, s1_reg_chance, color='yellow')
		ax[0].step(s1_breakpoints, s1_max_chance, color='cyan')
		ax[0].set(ylim=(0, 1.1), xlim=(0, 30), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 30.1, 2))
		ax[0].set_title(f'{self.s1.name} | agg: {round(self.s1.max_aggregate, 2)} | var: {round(self.s1.variance, 2)} | raw: {round(self.s1.damage, 2)}')

		s2_breakpoints, s2_min_chance, s2_reg_chance, s2_max_chance = self.s2.gen_breakpoints(self.offense)
		ax[1].step(s2_breakpoints, s2_min_chance, color='magenta')
		ax[1].step(s2_breakpoints, s2_reg_chance, color='yellow')
		ax[1].step(s2_breakpoints, s2_max_chance, color='cyan')
		ax[1].set(ylim=(0, 1.1), xlim=(0, 30), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 30.1, 2))
		ax[1].set_title(f'{self.s2.name} | agg: {round(self.s2.max_aggregate, 2)} | var: {round(self.s2.variance, 2)} | raw: {round(self.s2.damage, 2)}')

		s3_breakpoints, s3_min_chance, s3_reg_chance, s3_max_chance = self.s3.gen_breakpoints(self.offense)
		ax[2].step(s3_breakpoints, s3_min_chance, color='magenta')
		ax[2].step(s3_breakpoints, s3_reg_chance, color='yellow')
		ax[2].step(s3_breakpoints, s3_max_chance, color='cyan')
		ax[2].set(ylim=(0, 1.1), xlim=(0, 30), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 30.1, 2))
		ax[2].set_title(f'{self.s3.name} | agg: {round(self.s3.max_aggregate, 2)} | var: {round(self.s3.variance, 2)} | raw: {round(self.s3.damage, 2)}')

		self.aggregate = (2 * self.s1.max_aggregate + 2 * self.s2.max_aggregate + self.s3.max_aggregate) / 5
		self.variance = (2 * self.s1.variance + 2 * self.s2.variance + self.s3.variance) / 5
		self.damage = (2 * self.s1.damage + 2 * self.s2.damage + self.s3.damage) / 5
		
		fig.suptitle(self.gen_display_str())
		fig.canvas.manager.set_window_title('Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies')
		fig.tight_layout()
		# plt.show()
		
		return plt
