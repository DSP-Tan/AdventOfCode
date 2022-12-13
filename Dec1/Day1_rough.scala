import scala.io.Source

val filename = "example.txt"
for (line <- Source.fromFile(filename).getLines)
    println(line)

val lines = Source.fromFile(filename).getLines.toList
//val lines = Source.fromFile(filename).getLines.toArray

val n_elves: Int= Source.fromFile(filename).getLines.toList.count(_=="")+1
//var cal_elf: List[Int] = 

var count :Int = 0
var max   :Int = 0
for(line<-lines)
    if(line!=""){
        count = count + line.toInt
    }else 
        if(max<count){
           max=count
           count=0
           }
println(max)



val lines = Source.fromFile(input).getLines.toList
var count  :Int = 0
var max1   :Int = 0
var max2   :Int = 0
var max3   :Int = 0
for(line<-lines)
    if(line !=""){
        count = count + line.toInt
     } else {
        if(max1 < count)
           max1=count
        if(max1 > count && max2 < count)
           max2=count
        if(max2 > count && max3 < count)
           max3=count
        println(count)
        count=0
        }
println(f"max1: $max1")
println(f"max2: $max2")
println(f"max3: $max3")

// This isn't working because max1 isn't yet the max as you run through the loop.
// So what we gotta do is a recursive function, which takes the previous maximum.
// First time it takes 0 and returns max1, then it takes max1 and returns max 2,
// then it takes max 2 and returns max 3. This is also nice and scala style.