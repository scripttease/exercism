 
// Import Gleam StdLib modules here.
import gleam/list
import gleam/string
import gleam/io

pub fn hello_world() -> String {
  "Hello, from rna_transcription!"
}

fn transcribe(char: String) -> String {
  case char {
    "G" -> "C"
    "C" -> "G"
    "T" -> "A"
    "A" -> "U"
    _ -> ""
  }
}

// When making PR to lang track, remove the transcribe fn
// Also use commented out fn head below
// remove the to_rna fn

// pub fn to_rna(dna: String) -> String {
  // Delete the line below and insert your own code.
  // "C"
// }

pub fn to_rna(dna: String) -> String {
  // Delete the line below and insert your own code.
  // "C"

  dna
  |> string.to_graphemes()
  |> list.map(fn(char) { 
transcribe(char)
  })
  |> string.concat()
  |> io.debug()
}
