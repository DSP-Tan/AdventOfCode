import scala.io.Source

/* This is an array of strings where the string is the list of itmes for each
   elf as a string like "345\n23432\n3434"                                    */
val elfString  =  scala.io.Source.fromFile("input.txt").mkString.split("\n\n")
// The array of strings is mapped to an array of arrays of Ints
val elves      =  elfString.map( s=>s.split("\n").map(s=>s.toInt ) )
// Each array of ints is summed, then we have an array of Ints.
val elfCals    =  elves.map(  s=>s.sum )
println(elfCals.max)
