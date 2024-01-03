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

    for(line<-Lines){
      println(line)
      val Draws = line.split(":")(1).split(";")
    }

    }

}
