#the actual combat function will be in the player class had it written here
#at first but my dumb brain delete the function instead of copy paste
#should have it back by end of the day
class Combat(object):
  def __init__(self, name, hp, atk, end, mag, res, agi):
    self.name = name
    self.hp = hp
    #might drop mp, as stats are random for player if there magic is best they
    #could have a hard time if they can't use magic anymore
##    self.mp = 0
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
      self.defeat()
  
##  @property
##  def mp(self):
##    return self._mp
##
##  @mp.setter
##  def mp(self, val):
##    if (val > 0):
##      self._mp = val
##    else:
##      return "Not enough mp"
  
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
