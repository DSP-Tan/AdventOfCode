import scala.io.Source

val input :String = "example.txt"

val Lines = Source.fromFile(input).getLines().toList
println(Lines)
val Moves = for(line<-Lines) yield List(line(0),line(2))
println(Moves)

for(move<-Moves)
  println(f"${move(0)} ${move(1)}")


//println(Lines(0))
//println(Lines(1))
//println(Lines(2))
//println( Lines(2)(0) )

//val m = Map("X" -> 1, "Y" -> 2, "Z" -> 3)
//val P1_dic = Map("A":1, "B":2, "C":3)
//val P2_dic = Map("X":1, "Y":2, "Z":3)
//val score_elf = Map("A":1, "B":2, "C":3,
//                   "AX":3, "AY":0, "AZ":6,
//                   "BX":6, "BY":3, "BZ":0,
//                   "CX":0, "CY":6, "CZ":3)
//
//val score_me  = Map("X":1,  "Y":2,  "Z":3,
//               "AX":3, "AY":6, "AZ":0,
//               "BX":0, "BY":3, "BZ":6,
//               "CX":6, "CY":0, "CZ":3)
//
//println(m("X"))
