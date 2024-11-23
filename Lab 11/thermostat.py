class Thermostat:
  def __init__(self, default_temperature=68):
    self.default_temperature = default_temperature
    self.schedules = {}
  
  def add_schedule(self, time, temperature):
    self.schedules[time] = temperature
  
  def  __str__(self):
    result = f"Default temperature: {self.default_temperature} degrees"
    sorted_times = sorted(self.schedules)
    for time in sorted_times:
      temperature = self.schedules[time]
      result += f"\n{time} {temperature} degrees"
    return result
  
  def get_target_temperature(self, time):
    sorted_schedule= sorted(self.schedules)
    if not sorted_schedule or time<sorted_schedule[0]:
      return self.default_temperature

    target_temp=0
    for moment in sorted_schedule:
      if time >= moment:
        target_temp = self.schedules[moment]
      else:
        break
    return target_temp