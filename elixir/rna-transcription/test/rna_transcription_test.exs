defmodule RnaTranscriptionTest do
  use ExUnit.Case

  # @tag :pending
  test "transcribes guanine to cytosine" do
    assert RnaTranscription.to_rna('G') == 'C'
  end

  # @tag :pending
  test "transcribes cytosine to guanine" do
    assert RnaTranscription.to_rna('C') == 'G'
  end

  # @tag :pending
  test "transcribes thymidine to adenine" do
    assert RnaTranscription.to_rna('T') == 'A'
  end

  # @tag :pending
  test "transcribes adenine to uracil" do
    assert RnaTranscription.to_rna('A') == 'U'
  end

  # @tag :pending
  test "it transcribes all dna nucleotides to rna equivalents" do
    assert RnaTranscription.to_rna('ACGTGGTCTTAA') == 'UGCACCAGAAUU'
  end

  # My tests
  test "passed nothing, returns nothing" do
    assert RnaTranscription.to_rna('') == ''
  end

  test "given spaces input, ignored in output" do
    assert RnaTranscription.to_rna('GAG CC') == 'CUCGG'
  end

  test "given incorrect nucleotides returns nothing" do
    assert RnaTranscription.to_rna('XYZ') == ''
  end
end
