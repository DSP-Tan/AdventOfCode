import scala.io.Source

object Fart {

  val wordNums: Array[String] =
    Array("one","two","three","four","five","six","seven","eight","nine")

  val wordToNum =
    Map("one"->1,"two"->2,"three"->3,"four"->4,"five"->5,
        "six"->6,"seven"->7,"eight"->8,"nine"->9)

  // Count ints in a string
  def countInts(line: String): Int = {
    var count: Int = 0
    for ( letter <- line )
      if (letter.isDigit)
        count +=1
    return count
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

  def firstWordNum(line: String): (Int,String)= {
  /* In this function we use a placeholder array and fill it
  letter by letter from the line. For example, sliding over the pattern
  "abcdefghi", our array would be filled as:
  0. ('0','0','0','0','0')
  1. ('0','0','0','0','a')
  2. ('0','0','0','a','b')
  3. ('0','0','a','b','c')
  4. ('0','a','b','c','d')
  etc.
  Then we loop over the three possible word lengths 3, 4, 5
  I.E. we check if the last 3 letters is a word, the last 4,
  and then finally all of them. */

    var index = 0
    val wordbuff: Array[Char] = Array('0','0','0','0','0')
    // Add latest letter to word buffer and slide along
    for (letter <- line ){
      for (i <- 0 until 4) wordbuff(i)=wordbuff(i+1)
      wordbuff(4)=letter
      // println(wordbuff.mkString)
      for (i <- 0 until 3){
        val word = wordbuff.slice(2-i,5).mkString
        if ( wordNums.contains(word) )
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
        if ( wordNums.contains(word) )
          lasWord = (index, word)
        }
      index +=1
      }
    return lasWord
  }


  def main(args: Array[String] ):Unit = {
    val Lines = Source.fromFile(args(0)).getLines().toArray
    val combos: Array[(Int,Int)] = for {line <- Lines} yield {
      val Count = countInts(line)
      val wordFirst = firstWordNum(line)
      val wordLast  = lastNum(line)
      val intFirst  = firstInt(line)
      val intLast   = lastInt(line)

      val intOne = if (intFirst._1 < wordFirst._1) intFirst._2 else wordToNum(wordFirst._2)
      val intTwo = if (intLast._1  > wordLast._1 ) intLast._2  else wordToNum(wordLast._2 )

      val combo1 =  intFirst._2*10+intLast._2
      val combo2 =  intOne*10+intTwo
      //println(combo2)
      (combo1,combo2)
    }
    val combos1 = for( i<- combos) yield i._1
    val combos2 = for( i<- combos) yield i._2
    println(combos1.sum)
    println(combos2.sum)
  }

}
