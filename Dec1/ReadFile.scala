import scala.io.Source

val filename = "Day1.scala"
for (line <- Source.fromFile(filename).getLines) {
    println(line)
}