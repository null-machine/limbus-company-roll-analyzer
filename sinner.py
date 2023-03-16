import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Sinner:

	def __init__(self, name, s1, s2, s3):
		self.name = name
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
	
	def gen_chart(self):
		plt.style.use('dark_background')
		matplotlib.rcParams['font.family'] = ['DejaVu Sans Mono', 'monospace']
		fig, ax = plt.subplots(3, 1)

		s1_breakpoints, s1_min_chance, s1_reg_chance, s1_max_chance = self.s1.gen_breakpoints()
		ax[0].step(s1_breakpoints, s1_min_chance, color='magenta')
		ax[0].step(s1_breakpoints, s1_reg_chance, color='yellow')
		ax[0].step(s1_breakpoints, s1_max_chance, color='cyan')
		ax[0].set(ylim=(0, 1.1), xlim=(0, 30), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 30.1, 2))
		ax[0].set_title(f'{self.s1.name}')

		s2_breakpoints, s2_min_chance, s2_reg_chance, s2_max_chance = self.s2.gen_breakpoints()
		ax[1].step(s2_breakpoints, s2_min_chance, color='magenta')
		ax[1].step(s2_breakpoints, s2_reg_chance, color='yellow')
		ax[1].step(s2_breakpoints, s2_max_chance, color='cyan')
		ax[1].set(ylim=(0, 1.1), xlim=(0, 30), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 30.1, 2))
		ax[1].set_title(f'{self.s2.name}')

		s3_breakpoints, s3_min_chance, s3_reg_chance, s3_max_chance = self.s3.gen_breakpoints()
		ax[2].step(s3_breakpoints, s3_min_chance, color='magenta')
		ax[2].step(s3_breakpoints, s3_reg_chance, color='yellow')
		ax[2].step(s3_breakpoints, s3_max_chance, color='cyan')
		ax[2].set(ylim=(0, 1.1), xlim=(0, 30), yticks=np.arange(0, 1.1, 0.25), xticks=np.arange(0, 30.1, 2))
		ax[2].set_title(f'{self.s3.name}')

		fig.suptitle(f'{self.name}', fontsize=24)
		fig.canvas.manager.set_window_title('Sinner Ultimate Scientific Analysis Model Of Generally Unknown Strategies')
		fig.tight_layout()
		# plt.show()
		return plt
