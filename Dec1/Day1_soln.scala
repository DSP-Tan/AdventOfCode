// This is the official solution from the scala website:
// https://scalacenter.github.io/scala-advent-of-code/2022/puzzles/day01

import scala.math.Ordering

object Official {

  def part1(input: String): Int =
    maxInventories(scanInventories(input), 1).head

  def part2(input: String): Int =
    maxInventories(scanInventories(input), 3).sum

  case class Inventory(items: List[Int])

  def scanInventories(input: String): List[Inventory] = {
    val inventories = List.newBuilder[Inventory]
    var items = List.newBuilder[Int]
    for (line <- input.linesIterator) {
      if (line.isEmpty) {
        inventories += Inventory(items.result())
        items = List.newBuilder
      } else items += line.toInt
    }
    inventories.result()
  }

  def maxInventories(inventories: List[Inventory], n: Int): List[Int] =
    inventories.map(inventory => inventory.items.sum).sorted(Ordering.Int.reverse).take(n)

  def main(args: Array[String] ) = {
    println("Part 1: " + part1( args(0) ) )
    println("Part 2: " + part2( args(0) ) )
  }

}
