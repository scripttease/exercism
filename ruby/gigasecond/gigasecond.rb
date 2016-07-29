require 'date'
require 'time'
class Gigasecond
  VERSION = 1
  def self.from(time)
    t = Time.parse(time.to_s).utc.to_i
    t_gs = t + 1000000000
    gs = Time.at(t_gs)
  end
end

# convert given time to integer
#
# Tip: Instead of converting time to an integer, convert it to one of the time objects ☺
# Then add seconds to it
