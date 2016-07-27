UNITS = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
HUNDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
THOUS = ["", "M", "MM", "MMM", "MMMM", "MMMMM", "MMMMM", "MMMMMM", "MMMMMMM", "MMMMMMMM", "MMMMMMMMM"]

def convert_to_roman(num)
  arr = num.to_s.chars.map(&:to_i)
  if arr.length === 1
    ans = UNITS[ [0, arr[0]].max ]
  elsif arr.length === 2
    ans = TENS[ [0, arr[0]].max ] + UNITS[ [0, arr[1]].max ]
  elsif arr.length === 3
    ans = HUNDS[ [0, arr[0]].max ] + TENS[ [0, arr[1]].max ] + UNITS[ [0, arr[2]].max ]
  elsif arr.length === 4
    ans = THOUS[ [0, arr[0]].max ] + HUNDS[ [0, arr[1]].max ] + TENS[ [0, arr[2]].max ] + UNITS[ [0, arr[3]].max ]
  end
end
