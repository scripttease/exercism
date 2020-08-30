import rna_transcription
import gleam/should

pub fn hello_world_test() {
  rna_transcription.hello_world()
  |> should.equal("Hello, from rna_transcription!")
}

// Test rna_transcription
pub fn transcribes_guanine_to_cytosine_test() {
  rna_transcription.to_rna("G")
  |> should.equal("C")
}

pub fn transcribes_cytosine_to_gueanine_test() {
  rna_transcription.to_rna("C")
  |> should.equal("G")
}

pub fn transcribes_thymidine_to_adenine_test() {
  rna_transcription.to_rna("T")
  |> should.equal("A")
}

pub fn transcribes_adenine_to_uracil_test() {
  rna_transcription.to_rna("A")
  |> should.equal("U")
}

pub fn transcribes_all_nucleotides_test() {
  rna_transcription.to_rna("ACGTGGTCTTAA")
|> should.equal("UGCACCAGAAUU")
}

pub fn does_not_transcribe_spaces_test() {
  rna_transcription.to_rna("C CC")
|> should.equal("GGG")
}

pub fn empty_string_returns_empty_string_test() {
  rna_transcription.to_rna("")
|> should.equal("")
}

pub fn ingnore_incorrect_dna_nucleotides_test() {
  rna_transcription.to_rna("XGG")
|> should.equal("CC")
}


// # Note that this requires the return type to be different and makes problem far more complex

// pub fn incorrect_dna_bases_return_an_error_message() {
//   rna_transcription.to_rna("XCG")
// |> should.equal(Error("There was an error in your dna sequence"))
// }
