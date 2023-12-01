val root     : String  = "/"
var position : String = root

//position = position + "a/"

val example : List[String] = List("$ cd /","$ ls","dir a",
"14848514 b.txt","8504156 c.dat","dir d","$ cd a","$ ls","dir e","29116 f",
"2557 g","62596 h.lst","$ cd e","$ ls","584 i","$ cd ..","$ cd ..","$ cd d",
"$ ls","4060174 j","8033020 d.log","5626152 d.ext","7214296 k")

//printf("\nThere are %2d commands in example\n",example.length)
//printf("Here is example(0):\n %s\n",example(0))

//example(0).contains("$ cd")
//example(0).indexOf("d")

println( example(0).slice(example(0).indexOf("d")+2, example(0).length()))

var cmd : String = " "
for( line <- example )
    if (line.contains("$ cd") && true ){
       cmd = line.split(" ")(2) 
       println(line)
       println(s"This is a cd to $cmd")
    } else if (line.contains("$ ls")){
       println(line)
       println("This is an ls command")
    } else if (line.contains("dir")) {
       println(line)
       println("This is a directory.")
    } else 
       println(s"${line}\nThis is a file.")
       
// Make a mutable map with the name of a directory and then all the files in that directory.
// Then loop over all the other directories that contain the name of this directory, 
// and add their files to it.    