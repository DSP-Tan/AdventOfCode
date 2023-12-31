import scala.io.Source

object Main {
  def getInts(line: String): Array[Char] =
    for (letter <- line.toArray if letter.isDigit) yield letter

  val wordNums: Array[String] =
    Array("one","two","three","four","five","six","seven","eight","nine")
  val wordToNum =
    Map("one"->1,"two"->2,"three"->3,"four"->4,"five"->5,"six"->6,"seven"->7,"eight"->8,"nine"->9)

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

  def countWords( line:String ): Int = {
    var wordI = getNextWord(0, line)._1
    var count = 0
    while( wordI != -1 ){
      count +=1
      wordI = getNextWord(wordI, line)._1
    }
    return count
  }

  def recurseCount( line:String, start:Int, count:Int ): Int = {
    val wordI = getNextWord(start, line)._1
    if( wordI != -1 ) recurseCount(line, wordI, count+1)
    return count
  }

  def recurseGet( line:String, start:Int, words:Array[String] ): Array[String] = {
    val word = getNextWord(start, line)
    if( word._1 != -1 ){
      //println(word._2)
      //(words :+ word._2).foreach(s=>printf("%s ",s))
      println(s"In recurseGet, length: ${words.length}")
      recurseGet(line, word._1 , words :+ word._2)
    }
    println(s"End recurseGet, length: ${words.length}")
    println(s"End recurseGet, index: ${word._1}")
    words
  }

  //def getWordNums(line:String): Array[(String,Int)] = {
  //  var i = 0
  //  do {
  //    val iWord = getNextWord(i,line)
  //    i+=1
  //    iWord
  //  } while ( iWord._1 != -1)
  //  Array((fart._1, fart._2))

  //}

  def main(args: Array[String]): Unit = {

    val Lines: Array[String] =
      if   (args.length > 0) Source.fromFile(args(0)).getLines.toArray
      else Array[String]()

    if (Lines.length == 0){
      println("Please enter file name")
      scala.sys.exit(1)
      }

    // Let's iterate through the lines and test all our functions
    for (line<- Lines) {
      println(line)
      //val numbers= getInts(line)
      //numbers.foreach(s=>printf("%c ",s))
      //println
      //val N_words = countWords(line)
      //val Nr_words = recurseCount(line,0,0)
      //println(s"Imperative count ${N_words} words")
      //println(s"Recursive  count ${N_words} words")
      val words = recurseGet(line, 0, Array[String]())
      words.foreach(s=>printf("%s ",s))
      println(words.length)
    }

    //val combs1: Array[Int] = for (line<- Lines) yield {
    //  val numbers  = getInts(line)
    //  val intFirst = numbers(0).toInt -48
    //  val intLast  = numbers.last.toInt -48
    //  intFirst*10+intLast
    //  //1
    //  }
    //println(combs1.sum)

    //val combs2: Array[Int] = for (line<- Lines) yield {
    //  val numbers  = getInts(line)
    //  //val intFirst = numbers(0).toInt -48
    //  //val intLast  = numbers.last.toInt -48
    //  //val iFirst   = line.indexOf(numbers(0))
    //  //val iLast    = line.indexOf(numbers.last)
    //  //val intComb  = intFirst*10+intLast
    //  val fart: (Int,String) = getNextWord(0,line)
    //  println(line)
    //  println(s"${fart._1}")
    //  println(s"${fart._2}")
    //  1
    //  //intComb
    //  }
    //println(combs2.sum)
    }

}
