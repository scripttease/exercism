Louis Pop (louispopinjay@gmail.com)
So you can use arr.each.with_index
And then when you iterate you get each thing
but also the index they're on
irb(main):003:0> [:a, :b, :c].each.with_index do |item, index|
irb(main):004:1* puts "item: #{item}, index: #{index}"
irb(main):005:1> end
item: a, index: 0
item: b, index: 1
item: c, index: 2
=> [:a, :b, :c]
Then you can tell how far you're into the array
Me
ahhhhhh yep yep, cool. abit like foreach i guess?
Louis Pop (louispopinjay@gmail.com)
Yeah just like that
Then you can have an accumulator that you mutate
Me
yukkkkk
Louis Pop (louispopinjay@gmail.com)
or you can use arr.reduce.with_index
Me
ooooooh
😀

