---
title: "[golang] learning note and resources"
date: 2020-05-15T03:16:09Z
tags: golang
category: thoughts
---

## Primers

- If you do know nothing, start from the nice CodeAcademy interactive course https://www.codecademy.com/learn/learn-go/.
- If you know some language already, “A Tour of Go” is of high quality https://tour.golang.org/list <!--more-->
- If you already know Python, refer to this dictoinary “learning go from python”  http://govspy.peterbe.com/
- https://github.com/qyuhen/book
- http://legendtkl.com/categories/golang/


## Semantic Statments

- Writing in a new language without learning is unrealistic
- Keep a list of useful types, useful methods and useful packages.
- Golang is not Python
  - Go documentation is furiously annoying if you are used to python documentation
  - You need to relearn Golang before you can do anything useful in Golang, even if you know python inside out.
  - Golang has pointers. Python does not have pointers.
  - Golang is on a lower level than Python.
  - golang does not allow dict init or set init using curly brackets
  - no you cannot use `import pdb;pdb.set_trace()` in go
  - no you canoot use `print(type(x))` in go
  - Introspection is different
- Golang is similar to Python
  - Because both offer type inference
  - both initialise variables at declaration.
  - both promotes open-source package ecosystem using import statements
- Golang is not C99
  - Golang does not force semicolon
  - Golang does not need to malloc() and free()
- Golang’s literal is quite complex
- Not used error:
  - annoying
  - solution
  ```
  import _ fmt
  var x="not used"; _ = x
  ```

## Notes

### keywords

```
    package
    import
    func
    type
    interface
    var
    const
    range
    switch
    case
```

### Concurrency and goroutine [TBC]

### Printf format [TBC]

### methods and interfaces

- methods are just functions with a receiver
- methods is not function because receiver is not in the normal input specifier, different from python where the receiver is the first element in the normal input specifier.
- You can only declare a method with a receiver whose type is defined in the same package as the method. If "int" is not defined within you package, you cannot put it in your receiver
- Use keyword “type” to solve this. `type MyFloat float64`
- you can pass receiver by copy or by reference. Use a pointer receiver if passing by ref.
- go is ambihuous about pointer to structs
  - Go automatically dereferences a pointer before dot property
  - This seems a very bad idea to me because it cast the type of the variable implicitly.
  - Dangerous pitfall that should be disabled “Go interprets the statement `v.Scale(5)` as `(&v).Scale(5)` since the Scale method has a pointer receiver.”
  - Error is raised only at interface casting at compiling time, so I guess it’s kind of a minor problem.

```
func ScaleFunc(v *Vertex, f float64) {
  (*v).X = (*v).X * f
  v.Y = v.Y * f
}
```

- Type assertion
  - `val, ok :=interface.(mytype)`
- type switches
  - `if type(val)==str`
  - `switch val := input.(typ){ case int: fmt.Printf("%s\n","isInt");}`
- `Stringer.String() <=> def repr(self):`
  - use a value receiver to implement Stringer.
- error.Error()
- io.Reader()


### Interface

- Interface is used to define a meta-type that meets a criteria about its methods. Any type meets this criteria can then be casted into this interface.
- Interface describe type compatibility
- zero-method interface can hold any type.
- examine interface with describe()
   ```
   func describe(i I) {
   fmt.Printf("(%v, %T)\n", i, i)
   }
   ```
- `type(x)` equivalent is `fmt.Printf("%T\n",x)`

### moretypes

### Variadic functions [TBC]

### Closures
- are functions that reference an external variable
- akin to python’s decorator

### Functions

- function has types as func(input_type,input_type2) output_type
- `var foofunc func(int,int) int;`
- anonymous function can be defined by `anf := func(int,int) int{return 1;};`
- and can be called immediately

### Maps

init value:

- maps declared but not inited in `var m map[string]int;` will be a nil map that cant be 
mutated. This is because the map has not been initialised

```
make(map[key_type]value_type)

x = map[key_type]value_type{};

delete(map,key)

map[key]
```

### Arrays and Slice

- Slice is like a pointer
- Slice literal would create an Array, but only return a Slice.
- access with a[0]
- var a[10]int
- An array’s length is part of its type, so arrays cannot be resized.
- Both Array and Slice is implicitly declared.
- How is slice implemented?
- `__init__(arr, start, end)`
- Methods
  - init
  - getitem
  - setitem
  - len()
  - cap()
  - make() dynamically sized.
  - append()
  - range, a literal for for-loop
- A nil slice has a length and capacity of 0 and has no underlying array.
- Slices of slices. pointer to pointers. [PRACTICE] create an np.eye(3) matrix, and mutate it into a gaussian filter.


## Exercises

### range, a literal for for-loop

```golang
package main

import "golang.org/x/tour/pic"
import "fmt";
func Pic(dx, dy int) (out[][]uint8) {
out = make([][]uint8, dx)
xs := make([]int, dx);
ys := make([]int, dy);
for i,_ := range xs{
  out[i] = make([]uint8, dy)
  for j,_:=range ys{
    out[i][j] = (uint8)(i+j);
  }
  }
  fmt.Println("Called","Pic",dx,dy);
return;
}

func main() {
	pic.Show(Pic) // [IMAGE not showing correctly]
}
```

### getiem

```golang
package main

import "fmt"

func main() {
	var s []int;
	a := []int{2, 3, 5, 7, 11, 13}
	s = a;
	s = a[1:4]
	fmt.Println(s)

	s = a[:2]
	fmt.Println(s)

	s = a[1:]
	fmt.Println(s)

    s = a[1:len(a)]
	fmt.Println(s)

	s = a[1 : len(a)-1]
	fmt.Println(s)
}
```

### Structure literal

- is not a function call
- this is slightly uncomfortable

```golang
type Vertex struct {
	X, Y int
}
var v1 Vertex   =  Vertex{X: 1, Y: 2}
var v2 int      =  int( 5 );

var v3          =  Vertex{X: 1, Y: 2}
var v4          =  int( 5 );

// var v5       =  {X: 1, Y: 2} /// gives an error!
var v6          =  5;
```


### exercise-slices.go

```golang
package main

import "golang.org/x/tour/pic"
import "fmt";
func Pic(dx, dy int) (out[][]uint8) {
out = make([][]uint8, dx)
xs := make([]int, dx);
ys := make([]int, dy);
for i,_ := range xs{
  out[i] = make([]uint8, dy)
  for j,_:=range ys{
    out[i][j] = (uint8)(i+j);
  }
  }
  fmt.Println("Called","Pic",dx,dy);
return;
}

func main() {
  pic.Show(Pic)
}
```

### exercise-maps.go

```golang
package main

import (
  "golang.org/x/tour/wc"
//  "fmt"
  "strings"
)

func WordCount(s string) map[string]int {
  out := map[string]int{};
  for i,w :=  range strings.Fields(s){
    _ = i
  out[w] +=1;
  }
  return out
}

func main() {
  wc.Test(WordCount)
}

exercise-stringer.go

package main

import "fmt"

type IPAddr [4]byte

// TODO: Add a "String() string" method to IPAddr.

func main() {
  hosts := map[string]IPAddr{
    "loopback":  {127, 0, 0, 1},
    "googleDNS": {8, 8, 8, 8},
  }
  for name, ip := range hosts {
    fmt.Printf("%v: %v\n", name, ip)
  }
}
```

### exercise-images.go

```golang
package main

import "golang.org/x/tour/pic"
import "image"
import "image/color"

//type Image image.Image
type Image struct{
minX int
maxX int
minY int
maxY int
}

func (x *Image) Bounds() (image.Rectangle){

return image.Rect( x.minX, x.minY, x.maxX,x.maxY)
}

func (x *Image) ColorModel() (color.Model){
return color.RGBAModel
}

func (im *Image) At(x int, y int) color.Color{
pic := Pic( im.maxX, im.maxY)
return color.RGBA{pic[x][y],pic[x][y], 255, 255}
}

func Pic(dx, dy int) (out[][]uint8) {
out = make([][]uint8, dx)
xs := make([]int, dx);
ys := make([]int, dy);
for i,_ := range xs{
  out[i] = make([]uint8, dy)
  for j,_:=range ys{
    out[i][j] = (uint8)(i+j);
  }
  }
//  fmt.Println("Called","Pic",dx,dy);
return out;
}

func main() {
  m := Image{0,200,0,200}
  pic.ShowImage(&m)
}
package main

import "golang.org/x/tour/pic"
import "image"
import "image/color"

//type Image image.Image
type Image struct{
minX int
maxX int
minY int
maxY int
}

func (x *Image) Bounds() (image.Rectangle){

return image.Rect( x.minX, x.minY, x.maxX,x.maxY)
}

func (x *Image) ColorModel() (color.Model){
return color.RGBAModel
}

func (im *Image) At(x int, y int) color.Color{
pic := Pic( im.maxX, im.maxY)
return color.RGBA{pic[x][y],pic[x][y], 255, 255}
}

func Pic(dx, dy int) (out[][]uint8) {
out = make([][]uint8, dx)
xs := make([]int, dx);
ys := make([]int, dy);
for i,_ := range xs{
  out[i] = make([]uint8, dy)
  for j,_:=range ys{
    out[i][j] = (uint8)(i+j);
  }
  }
//  fmt.Println("Called","Pic",dx,dy);
return out;
}

func main() {
  m := Image{0,200,0,200}
  pic.ShowImage(&m)
}
```

### exercise-rot-reader.go

```golang
package main

import (
  "io"
  "os"
  "strings"
  "fmt"
)

type rot13Reader struct {
  r io.Reader
}

func (r rot13Reader) Read (bts []byte) (int, error){
    intVal,e :=r.r.Read(bts)
  //fmt.Println(bts);
  for i:=0;i<intVal;i++{
     x:=bts[i]
     var y byte;
     if (x>=65 && x<97){
       y = (x - 65 + 13)%26 + 65
     }else if(x >= 97){
       y = (x -97 + 13)%26 + 97     
     }else{
       y = x+13;
       fmt.Println(x,y);
     }
     bts[i] = y
  }
  
  return intVal,e
}

func main() {
  s := strings.NewReader("Lbh penpxrq gur pbqr!")
  r := rot13Reader{s}
    io.Copy(os.Stdout, &r)
  return;
//var buf []byte;
  buf := make([]byte,100);
  for {
   i,e := r.Read(buf)
   _ = e
   _ = i 
   fmt.Printf("%s\n",buf)
   if e==io.EOF{
       break
   }
  }
  return 
    io.Copy(os.Stdout, &r)
}
```

### Dependency management

## Summary

### Grammar

- Long if-else chain <=> Switch with no condition
- Defer multiline functions https://stackoverflow.com/questions/32541870/multiple-defers-vs-deferred-anonymous-function
- Init a null pointer: [TBC] nothing found so far.


## Next Topics

### Vocabularies. FileIO, strings, OrderedDict, Json, Yaml, Html, Regex
- strings.Fields

### Packaging and Testing
### Profiling and Concurrency
### Debugging and Tracing