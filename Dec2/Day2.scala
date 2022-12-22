import scala.io.Source

val input :String = "example.txt"

val Lines = Source.fromFile(input).getLines().toList
println(Lines)
println(Lines(0))
println(Lines(1))
println(Lines(2))

val m = Map("X" -> 1, "Y" -> 2, "Z" -> 3)

println(m("X"))
