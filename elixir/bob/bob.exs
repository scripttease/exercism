defmodule Bob do
  def hey(input) do
    cond do
        Regex.match?(~r/.+\?$/m, input) -> "Sure."
        Regex.match?(~r/^\s*$/m, input) -> "Fine. Be that way!"
        input == String.upcase(input) && input != String.downcase(input) -> "Whoa, chill out!"
        true -> "Whatever."

    end
  end
end
