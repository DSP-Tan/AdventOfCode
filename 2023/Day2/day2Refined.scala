import scala.io.Source

object Main {

  def main(args: Array[String]): Unit = {

    val Lines: List[String] =
      if   (args.length > 0) Source.fromFile(args(0)).getLines.toList
      else Nil

    if (Lines.length == 0){
      println("Please enter file name")
      scala.sys.exit(1)
      }

    // Convert each draw into 3 numbers, and then check each of these three
    // for a condition. We can use a tuple: (R,G,B)
    val Games: List[Array[String]] = for(line<-Lines) yield line.split(":")(1).split(";")
    val tupTriplets =
      for (draws <- Games) yield for(draw<-draws) yield {
      val colours = draw.split(",")

      val RGB: List[Array[Char]] =
        for(col<-List("red","blue","green") ) yield
          for(colour<-colours; if colour.contains(col); ch<-colour; if ch.isDigit) yield ch
      RGB.map(s=> if(s.isEmpty) 0 else s.mkString.toInt)
      }

    // part 1
    val rMax = 12; val bMax = 14; val gMax = 13
    def possGame(tupArray: Array[List[Int]]) : Boolean =
      tupArray.forall(s=> s(0) <= rMax && s(1) <= bMax && s(2) <=gMax)

    val possibleAndIndex = tupTriplets.zipWithIndex.filter(s => possGame(s._1) )
    println(possibleAndIndex.map(_._2+1).sum)

    // part 2
    def maxPower(tupArray: Array[List[Int]] ) : Int =
      tupArray.map(_(0)).max*tupArray.map(_(1)).max*tupArray.map(_(2)).max
    println(tupTriplets.map(maxPower(_)).sum )


    }

}
