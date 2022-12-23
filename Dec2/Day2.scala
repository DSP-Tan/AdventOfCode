import scala.io.Source

val input :String = "input.txt"
val Lines = Source.fromFile(input).getLines().toList
val Moves = for(line<-Lines) yield List(line(0),line(2))

val score_me  = Map('X'->1,  'Y'->2,  'Z'->3,
                   "AX"->3, "AY"->6, "AZ"->0,
                   "BX"->0, "BY"->3, "BZ"->6,
                   "CX"->6, "CY"->0, "CZ"->3)


// Part 1
var my_score: Int =0
for(move<-Moves)
    my_score += score_me(move(1)) + score_me(s"${move(0)}${move(1)}")
println(my_score)

// Part 2
val move_needed=Map("AX"->'C', "AY"->'A', "AZ"->'B',
                    "BX"->'A', "BY"->'B', "BZ"->'C',
                    "CX"->'B', "CY"->'C', "CZ"->'A')
val Moves2 = for(move<-Moves) yield List(move(0),move(1), move_needed( s"${move(0)}${move(1)}") )

val score2 = Map('A'->1, 'B'->2, 'C'->3, 'X'->0, 'Y'->3, 'Z'->6)
my_score=0
for(move<-Moves2)
    my_score += score2(move(1))+score2(move(2))
println(my_score)
