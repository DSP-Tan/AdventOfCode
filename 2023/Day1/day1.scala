import scala.io.Source

object Fart {

  val numwords: Array[String] =
    Array("one","two","three","four","five","six","seven","eight","nine")

  val wordNum =
    Map("one"->1,"two"->2,"three"->3,"four"->4,"five"->5,
        "six"->6,"seven"->7,"eight"->8,"nine"->9)

  def countInts(line: String): Int = {
    var count: Int = 0
    for ( letter <- line )
      if (letter.isDigit)
        count +=1
    return count
  }

  def firstNum(line: String): (Int,String)= {
    var index = 0
    val wordbuff: Array[Char] = Array('0','0','0','0','0')
    // Add latest letter to word buffer and slide along
    for (letter <- line ){
      for (i <- 0 until 4) wordbuff(i)=wordbuff(i+1)
      wordbuff(4)=letter
      //println(wordbuff.mkString)
      // So we loop over the three possible word lenghts 3, 4, 5
      for (i <- 0 until 3){
        val word = wordbuff.slice(2-i,5).mkString
        if ( numwords.contains(word) )
          return (index, word)
        }
      index +=1
      }
    return (100000,"")
  }

  def lastNum(line: String): (Int,String)= {
    var index = 0
    var lasWord = (-1,"")
    val wordbuff: Array[Char] = Array('0','0','0','0','0')

    for (letter <- line ){
      for (i <- 0 until 4) wordbuff(i)=wordbuff(i+1)
      wordbuff(4)=letter
      for (i <- 0 until 3){
        val word = wordbuff.slice(2-i,5).mkString
        if ( numwords.contains(word) )
          lasWord = (index, word)
        }
      index +=1
      }
    return lasWord
  }

  def firstInt(line: String): (Int,Int) = {
    var index = 0
    for ( letter <- line ) {
      if (letter.isDigit)
        return (index, letter.toInt -48)
      index +=1
    }
    return (100000,-1)
  }

  def lastInt(line: String): (Int,Int) = {
    var index = 0
    var dig = (-1,-1)
    for ( letter <- line ){
      if (letter.isDigit)
        dig =  (index, letter.toInt -48)
      index +=1
    }
    return dig
  }

  def main(args: Array[String] ):Unit = {
    val Lines = Source.fromFile(args(0)).getLines().toArray
    val combos: Array[Int] = for {line <- Lines} yield {
      println(line)
      val Count = countInts(line)
      val wordFirst = firstNum(line)
      val wordLast  = lastNum(line)
      val intFirst  = firstInt(line)
      val intLast   = lastInt(line)

      val intOne = if (intFirst._1 < wordFirst._1) intFirst._2 else wordNum(wordFirst._2)
      val intTwo = if (intLast._1 > wordLast._1) intLast._2 else wordNum(wordLast._2)

      val combo =  intOne*10+intTwo
      println(combo)
      combo
    }
    println(combos.sum)
  }

}
