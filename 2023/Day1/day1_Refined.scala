import scala.io.Source

object Main {
  def getInts(line: String): Array[Char] =
    for (letter <- line.toArray if letter.isDigit) yield letter

  val wordNums: Array[String] =
    Array("one","two","three","four","five","six","seven","eight","nine")
  val wordToNum =
    Map("zero"->0, "one"->1,"two"->2,"three"->3,"four"->4,
        "five"->5,"six"->6,"seven"->7,"eight"->8,"nine"->9)

  def getNextWord(start:Int, line:String): (Int,String) = {
    val wordBuff: Array[Char] = Array('0','0','0','0','0')
    for (i <- start until line.length ) {
      for (j <- 0 until 4) wordBuff(j) = wordBuff(j + 1)
      wordBuff(4) = line(i)
      for (j <- 0 until 3) {
        val word = wordBuff.slice(2 - j, 5).mkString
        if (wordNums.contains(word))
          return (i, word)
        }
      }
    (-1,wordBuff.mkString)
  }

  def recurseCount( line:String, start:Int, count:Int ): Int = {
    val wordI = getNextWord(start, line)._1
    if( wordI != -1 ) recurseCount(line, wordI, count+1)
    else count
  }

  def recurseGet( line:String, start:Int, words:Array[(Int,String)] ): Array[(Int,String)] = {
    val word = getNextWord(start, line)
    if( word._1 != -1 )
      recurseGet(line, word._1 , words :+ word)
    else
      words
  }

  def main(args: Array[String]): Unit = {

    val Lines: Array[String] =
      if   (args.length > 0) Source.fromFile(args(0)).getLines.toArray
      else Array[String]()

    if (Lines.length == 0){
      println("Please enter file name")
      scala.sys.exit(1)
      }

    // Let's iterate through the lines and test all our functions
    //for (line<- Lines) {
    //  println(line)
    //  val words = recurseGet( line, 0, Array[(Int,String)]() )
    //  words.foreach(s=>printf("%s ",s._2))
    //  println
    //}

    val combs1: Array[Int] = for (line<- Lines) yield {
      val numbers  = getInts(line)
      val intFirst = numbers(0).toInt -48
      val intLast  = numbers.last.toInt -48
      intFirst*10+intLast
      }
    println("Part 1:")
    println(combs1.sum)

    val combs2: Array[Int] = for (line<- Lines) yield {
      val numbers  = getInts(line)
      val intFirst = numbers(0).toInt -48
      val intLast  = numbers.last.toInt -48
      val iFirst   = line.indexOf(numbers(0))
      val iLast    = line.length-1-line.reverse.indexOf(numbers.last)

      val words = recurseGet( line, 0, Array[(Int,String)]() )
      val wordFirst = if (words.length >0 ) words(0)   else (iFirst+1,"zero")
      val wordLast  = if (words.length >0 ) words.last else (-1,"zero")

      val intOne = if (iFirst < wordFirst._1) intFirst else wordToNum(wordFirst._2)
      val intTwo = if (iLast  > wordLast._1 ) intLast  else wordToNum(wordLast._2 )

      intOne*10+intTwo
      }
    println("Part 2:")
    println(combs2.sum)
    }

}
