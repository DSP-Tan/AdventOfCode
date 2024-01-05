import scala.io.Source

def max_below(input:String, below: Int): Int ={
  val Lines = Source.fromFile(input).getLines().toList
  var cals  :Int = 0
  var max   :Int = 0
  for(line<-Lines)
    if( !line.isBlank() ){
      cals +=  line.toInt
      }else{
        if(max<cals && cals < below)
          max=cals
        cals =0
        }
  return max
  }

def sum_maxes(input: String, maxes: Int): Int ={
  var init: Int=99999
  var sum:  Int=0
  for(i<-Range(0,maxes)){
    init = max_below(input,init)
    sum +=init      }
  return sum
  }

// Part 1
println(sum_maxes("input.txt", 1))

//Part 2
println(sum_maxes("input.txt",3))
