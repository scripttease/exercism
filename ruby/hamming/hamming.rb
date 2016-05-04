class Hamming
VERSION = 1
 def self.compute(strand1, strand2)
    if strand1.length != strand2.length
      raise ArgumentError
    end
   array1 = strand1.scan(/./)
   array2 = strand2.scan(/./)
   array3 = array1.zip(array2)
   array3.reduce(0){|acc,elem| elem[0] == elem[1] ? acc : acc+1 }
 end
end

  # split strand 1 and strand 2 into lists of characters eg agaa becomes a,g,a,a
  # strand1[n] == strand2[n] ?
  # if false, do hamml_distance +1
  # hamml_distance = 0
  # n=0, n++
  # return hamml_distance
 # 
 # fucntional
 # use inject
 # [array].inject(0) {|result, element| result + element}
 # result of body is always reyrned to the next iteration of inject
 # result must be therefor the hamml_difference (so the initial value is (0) )
 # the final return value is the overall return value for inject method
 # element needs to somehow increment if the stands do not match...
