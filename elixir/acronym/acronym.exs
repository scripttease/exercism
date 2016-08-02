defmodule Acronym do
  @doc """
  Generate an acronym from a string.
  "This is a string" => "TIAS"
  """
  @spec abbreviate(String.t()) :: String.t()
  def abbreviate(string) do
    Regex.scan(~r/\b([A-Za-z])\B|[A-Z]/, string, capture: :first)
    |> Enum.join("")
    |> String.upcase
  end
end