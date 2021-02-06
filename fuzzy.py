import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#variable
pan_temp = ctrl.Antecedent(np.arange(0, 121, 0.5), 'pan_temp')
pan_weight = ctrl.Antecedent(np.arange(0, 3.1, 0.1), 'pan_weight')
heat_level = ctrl.Consequent(np.arange(0, 121, 0.5), 'heat_level')

#membership function
pan_temp['cold'] = fuzz.trimf(pan_temp.universe, [0, 0, 45])
pan_temp['warm'] = fuzz.trimf(pan_temp.universe, [30, 60, 90])
pan_temp['hot'] = fuzz.trimf(pan_temp.universe, [75, 105, 120])

pan_weight['low'] = fuzz.trimf(pan_weight.universe, [0, 0, 1.0])
pan_weight['medium'] = fuzz.trimf(pan_weight.universe, [0.5, 1.25, 2.0])
pan_weight['high'] = fuzz.trimf(pan_weight.universe, [1.5, 2.25, 3.0])

heat_level['low'] = fuzz.trimf(heat_level.universe, [0, 0, 60])
heat_level['medium'] = fuzz.trimf(heat_level.universe, [20, 60, 100])
heat_level['high'] = fuzz.trimf(heat_level.universe, [60, 100, 120])

pan_temp.view()
pan_weight.view()
heat_level.view()
plt.show()

#rules
r1 = ctrl.Rule(pan_temp['cold'] & pan_weight['low'], heat_level['medium'])
r2 = ctrl.Rule(pan_temp['cold'] & pan_weight['medium'], heat_level['medium'])
r3 = ctrl.Rule(pan_temp['cold'] & pan_weight['high'], heat_level['high'])
r4 = ctrl.Rule(pan_temp['warm'] & pan_weight['low'], heat_level['medium'])
r5 = ctrl.Rule(pan_temp['warm'] & pan_weight['medium'], heat_level['high'])
r6 = ctrl.Rule(pan_temp['warm'] & pan_weight['high'], heat_level['high'])
r7 = ctrl.Rule(pan_temp['hot'] & pan_weight['low'], heat_level['low'])
r8 = ctrl.Rule(pan_temp['hot'] & pan_weight['medium'], heat_level['low'])
r9 = ctrl.Rule(pan_temp['hot'] & pan_weight['high'], heat_level['low'])

heat_level_ctrl = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9])
heat_level_system = ctrl.ControlSystemSimulation(heat_level_ctrl)

# temp = input('Please enter the temperature.[°C]\n')
# weight = input('Please enter the weight of the pan.[kg]\n')

heat_level_system.input['pan_temp'] = 30
heat_level_system.input['pan_weight'] = 1.5
heat_level_system.compute()
print('result: heat level = ',heat_level_system.output['heat_level'],' °C')

heat_level.view(sim=heat_level_system)
pan_temp.view(sim=30)
pan_weight.view(sim=1.5)
plt.show()
