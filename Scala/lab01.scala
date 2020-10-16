import java.io.{BufferedReader, FileReader}

import scala.io.Source
import scala.math.sqrt
import scala.util.Random

//scalar product of two vectors xs and ys
def scalarUgly(xs: List[Int], ys: List[Int]): List[Int] = {
  if (xs.size != ys.size || xs.isEmpty || ys.isEmpty)
    throw new IllegalArgumentException("Vectors should be of same size and not empty")
  var i = 0
  val rs: Array[Int] = Array.ofDim[Int](xs.size)
  while (i < xs.size) {
    rs(i) = xs(i) * ys(i)
    i = i + 1
  }
  rs.toList
}

//scalar product of two vectors xs and ys
def scalar(xs: List[Int], ys: List[Int]): List[Int] = {
  if (xs.size != ys.size || xs.isEmpty || ys.isEmpty)
    throw new IllegalArgumentException("Vectors should be of same size and not empty")
  else {
    for ((x, y) <- xs zip ys) yield x * y
  }
}

//quicksort algorithm
def sortUgly(xs: List[Int]): List[Int] = {
  var arr = xs.toArray

  def sort(l: Int, r: Int) {
    val pivot = arr((l + r) / 2)
    var i = l
    var j = r
    while (i <= j) {
      while (arr(i) < pivot) i += 1
      while (arr(j) > pivot) j -= 1
      if (i <= j) {
        val temp = arr(i)
        arr(i) = arr(j)
        arr(j) = temp
        i += 1
        j -= 1
      }
    }
    if (l < j) sort(l, j)
    if (j < r) sort(i, r)
  }

  sort(0, arr.length - 1)
  arr.toList
}

def sort(xs: List[Int]): List[Int] = {
  if (xs.size <= 1) xs
  else {
    val pivot: Int = Random.between(0, xs.size)
    sort(xs.filter(_ < xs(pivot))) ::: xs(pivot) :: sort(xs.filter(_ > xs(pivot)))
  }
}

//checks if n is prime
def isPrimeUgly(n: Int): Boolean = {
  if (n == 2 || n == 3) return true
  if (n < 2 || n % 2 == 0) return false
  var i: Int = 3
  while (i <=[Int] sqrt(n)) {
    if (n % i == 0) return false
    i = i + 2
  }
  true
}
def isPrime(n: Int): Boolean =
  (n > 1) && !(2 to scala.math.sqrt(n).toInt).exists(x => n % x == 0)


//for given positive integer n, find all pairs of integers i and j, where 1 ≤ j < i < n such that i + j is prime
def primePairsUgly(n: Int): List[(Int, Int)] = {
  var i = 2
  var res: List[(Int, Int)] = List()
  while (i < n) {
    var j = 1
    while (j < i) {
      if (isPrimeUgly(i + j))
        res = (i, j) :: res
      j = j + 1
    }
    i = i + 1
  }
  res

}
def primePairs(n: Int): List[(Int, Int)] = {
  val rs = for {
    i <- 2 to n
    j <- 1 to n
    if j < i && isPrime(i + j)
  } yield (i, j)
  rs.toList
}

//create a list with all lines from given file
val filesHere = new java.io.File(".").listFiles
def fileLinesUgly(file: java.io.File): List[String] = {
  var res: List[String] = List()

  val br: BufferedReader = new BufferedReader(new FileReader(file))
  var str: String = br.readLine()
  while (str != null) {
    str = br.readLine()
    res = str :: res
  }

  res.reverse
}
def fileLines(file: java.io.File): List[String] = Source.fromFile(file).getLines().toList

//print names of all .scala files which are in filesHere & are non empty
def printNonEmptyUgly(pattern: String): Unit = {
  var i = 0
  while(i < filesHere.size){
    if(filesHere(i).getName.endsWith(".scala") && filesHere(i).length() != 0){
      println(filesHere(i).getName)
    }
    i = i + 1
  }
}
def printNonEmpty(pattern: String): Unit = {
  for{
    file <- filesHere
    if file.getName.endsWith(".scala")
    if file.length() != 0
  }yield println(file.getName)
}