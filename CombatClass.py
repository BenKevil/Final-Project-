class Combat(object):
  def __init__(self, name, hp, atk, end, mag, res, agi):
    self.name = name
    self.hp = hp
    self.atk = atk
    self.end = end
    self.mag = mag
    self.res = res
    self.agi = agi

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, val):
    self._name = val
  
  @property
  def hp(self):
    return self._hp

  @hp.setter
  def hp(self, val):
    if (val > 0):
      self._hp = val
    else:
      self._hp = 0
  
  @property
  def atk(self):
    return self._atk

  @atk.setter
  def atk(self, val):
    self._atk = val
  
  @property
  def end(self):
    return self._end

  @end.setter
  def end(self, val):
    self._end = val
  
  @property
  def mag(self):
    return self._mag

  @mag.setter
  def mag(self, val):
    self._mag = val
  
  @property
  def res(self):
    return self._res

  @res.setter
  def res(self, val):
    self._res = val
  
  @property
  def agi(self):
    return self._agi

  @agi.setter
  def agi(self, val):
    self._agi = val
