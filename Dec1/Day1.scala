import scala.io.Source

def max_below(input:String, below: Int): Int ={
   val Lines = Source.fromFile(input).getLines.toList
   var cals  :Int = 0
   var max   :Int = 0
   for(line<-Lines)
      if( !line.isBlank() ){
        cals = cals + line.toInt
      }else{ 
        if(max<cals && cals < below)
           max=cals
        cals =0
        }
    return max
    }

// Part 1
var init: Int=99999
var sum: Int=0
for(i<-Range(0,1)){
    init= max_below("input.txt",init)
    sum +=init
    }
println(sum)

//Part 2
var init: Int=99999
var sum: Int=0
for(i<-Range(0,3)){
    init= max_below("input.txt",init)
    sum +=init
    }
println(sum)
