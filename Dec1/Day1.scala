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

var max1= max_below("example.txt", 99999999)
var max2= max_below("example.txt", max1)
var max3= max_below("example.txt", max2)
//println(max1)
//println(max1+max2+max3)

max1= max_below("input.txt", 99999999)
println(max1)
max2= max_below("input.txt", max1)
max3= max_below("input.txt", max2)
println(max1+max2+max3)