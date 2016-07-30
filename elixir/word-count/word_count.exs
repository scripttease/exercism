defmodule Words do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t) :: map
  def count(sentence) do
    sentence
    |> String.split(~r/[\s_,\.!&@"'%$^:]/, trim: true)
    |> Enum.group_by(&String.downcase/1)
    |> Enum.map(fn({k, v}) -> {k, length(v)} end)
    |> Enum.into(%{})
  end
end
