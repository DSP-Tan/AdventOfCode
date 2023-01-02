import scala.io.Source
val Sacks = Source.fromFile("input.txt").getLines().toList

//println(Sacks)

def priority(c: Char) :Int =  if(c.toInt>90) c.toInt - 96 else c.toInt - 38

var tot: Int=0
var half: Int=0
for(sack<- Sacks){
  half=sack.size/2
  for(j<- ( Set( sack.slice(0,half) ).intersect( Set(sack.slice(half, sack.size ) ) ) ).toString )
    // This doesn't work becuse it is a set of one element which is a string.
    // We need a set of separate chars, and that is not done this way.
    tot
    // += priority(j)
  }
println(tot)

// var flort :Set[Char]= Set()
// for(i<-"flangus""){
//     | flort +=i
//     | }

println(priority('A'))
