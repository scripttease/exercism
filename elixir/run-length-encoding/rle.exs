defmodule RunLengthEncoder do
  @doc """
  Generates a string where consecutive elements are represented as a data value and count.
  "HORSE" => "1H1O1R1S1E"
  For this example, assume all input are strings, that are all uppercase letters.
  It should also be able to reconstruct the data into its original form.
  "1H1O1R1S1E" => "HORSE"
  """
  @spec encode(String.t) :: String.t
  def encode(string) do
    string
    |> String.split("", trim: true)
    |> Enum.chunk_by(fn char -> char end)
    |> Enum.map(fn char -> Enum.join(char)end)
    |> Enum.reduce("", fn(char, acc) -> acc <> to_string(String.length(char)) <> String.first(char) end)
  end

  @spec decode(String.t) :: String.t
  def decode(string) do
    string
    |> String.split(~r/(?:(?i)(?<=^|\d)(?=[a-z])|(?<=[a-z])(?=$|\d))/, trim: true)
    |> Enum.chunk(2)
    |> Enum.map(fn pair -> List.to_tuple(pair)end)
    |> Enum.map(fn({k, v}) -> Tuple.duplicate(v, String.to_integer(k)) end)
    |> Enum.map(fn arg -> Tuple.to_list(arg) end)
    |> Enum.map(fn arg -> Enum.join(arg) end)
    |> Enum.join("")
  end
end
