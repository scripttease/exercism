module BookKeeping
  VERSION = 4
end

class Complement
  DNAtoRNA = {
    "G" => "C",
    "C" => "G",
    "T" => "A",
    "A" => "U",
  }

  class InvalidBase < RuntimeError
  end

  # DNAtoRNA.default_proc = -> (hash, key) { raise InvalidBase, "#{key} is not a DNA base!" }

  VERSION = 1
  def self.of_dna(strand)
    strand.split("")
      .map { |dna| DNAtoRNA[dna] || (break []) }
      .join

    # rescue InvalidBase
    # ""
  end
end

# Given a DNA strand, its transcribed RNA strand is formed by replacing
# each nucleotide with its complement:

# * `G` -> `C`
# * `C` -> `G`
# * `T` -> `A`
# * `A` -> `U`
