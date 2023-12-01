import scala.io.Source

val n_elves: Int= Source.fromFile(filename).getLines.toList.count(_=="")+1

def calorific(input:String): Int ={
   val lines = Source.fromFile(input).getLines.toList
   var count :Int = 0
   var max   :Int = 0
   for(line<-lines)
       if(line !=""){
           count = count + line.toInt
       }else{
           if(max<count){
              max=count
              }
           count=0
           }
   return max
   }

println(calorific("example.txt"))
println(calorific("input.txt")  )

def top_3_cals(input:String): Int ={
   val lines = Source.fromFile(input).getLines.toList
   var count  :Int = 0
   var max1   :Int = 0
   var max2   :Int = 0
   var max3   :Int = 0
   for(line<-lines)
       if(line !=""){
           count = count + line.toInt
        } else if(max1<count){
        max1=count
        count=0
        } else if(max1>count && count < max2){
        max2=count
        count=0
        } else if(max2>count && count < max3){
        max3=count
        count=0
        }
   return max1+max2+max3
   }
println(top_3_cals("example.txt"))
println(top_3_cals("input.txt")  )