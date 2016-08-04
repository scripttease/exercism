require "prime"
class Raindrops
  Version = 1
  def self.convert(n)
    pmax = ((Math.sqrt(n))+1).ceil
    if n <= 1 
      n
    elsif
      for pn in 2..pmax
        if n %  pn == 0 then
          next 
        end
        pn + Raindrops.convert(n/pn)
      end
      n
      # puts "pling #{n}" 
      # Louis this returns nil i can't do anything with the n unless i just put n
    else
      n
    end
  end

  def numrange(n)
    for pn in 0..10
      if n % pn == 0 then
        next
      end
      puts "loop#{n}"
    end
  end

end

# for pn in ( 2..(((Math.sqrt(n))+1).ceil) )
