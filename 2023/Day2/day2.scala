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
    Lines.foreach(println)

    // Convert each draw into 3 numbers, and then check each of these three
    // for a condition. We can use a tuple: (R,G,B)
    val Games: List[Array[String]] = for(line<-Lines) yield line.split(":")(1).split(";")
    val tupTriplets =
      for (draws <- Games) yield for(draw<-draws) yield {
      val colours = draw.split(",")

      //colours.foreach(s=> printf("[%s] ",s))
      val red   = for(colour<-colours; if colour.contains("red"); letter<-colour;   if letter.isDigit) yield letter
      val blue  = for(colour<-colours; if colour.contains("blue"); letter<-colour;  if letter.isDigit) yield letter
      val green = for(colour<-colours; if colour.contains("green"); letter<-colour; if letter.isDigit) yield letter

      val redz   = if(red.isEmpty)   0 else red.mkString.toInt
      val bluez  = if(blue.isEmpty)  0 else blue.mkString.toInt
      val greenz = if(green.isEmpty) 0 else green.mkString.toInt
      (redz,bluez,greenz)
    }
    tupTriplets(1).foreach(println)

    // part 1
    val rMax = 12; val bMax = 14; val gMax = 13
    // maybe make a function and do a filter and then you can just
    // select out the possible games.
    for(tupTrip<-tupTriplets) {
      for(tuple<-tupTrip)
         tuple._1 <= rMax && tuple._2 <= bMax && tuple._3 <=gMax
    }


    }

}
