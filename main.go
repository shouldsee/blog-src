package main

import (
    "bytes"
    "fmt"
    "os"
    "log"
    "github.com/russross/blackfriday"
)


import (
    // "bytes"
    // "github.com/yuin/goldmark"
    // "io/ioutil"
    "github.com/yuin/goldmark"
    "github.com/yuin/goldmark/extension"
    "github.com/yuin/goldmark/parser"
    goldhtml "github.com/yuin/goldmark/renderer/html"

    "github.com/alecthomas/chroma/lexers"
    // "github.com/alecthomas/chroma/formatters"
    "github.com/alecthomas/chroma/styles"
    "github.com/alecthomas/chroma/formatters/html"
	"bufio"
	// "bytes"
	"github.com/PuerkitoBio/goquery"
	// "github.com/alecthomas/chroma/styles"
	// "github.com/russross/blackfriday"
	"html/template"
	"io/ioutil"
	// "log"
	// "os"
	"strings"

)



var source = []byte( `

section1
=================

section2
-------------

### Package

## Overview

- something else
  - blah
    - blah
- and other

1. something
2. something else

<code>
some code
</code>

`);
func main(){

md := goldmark.New(
          goldmark.WithExtensions(extension.GFM),
          goldmark.WithParserOptions(
              parser.WithAutoHeadingID(),
          ),
          goldmark.WithRendererOptions(
              goldhtml.WithHardWraps(),
              goldhtml.WithXHTML(),
              goldhtml.WithUnsafe(),
          ),
      )
  // _ = md;

  var buf bytes.Buffer

  // if err := md.Convert(source, &buf); err != nil {
  //  panic(err)
  // }

 // fmt.Fprintf(os.Stderr, "%s \n", buf.String())
 // fmt.Fprintf(os.Stdout, "%s \n", buf.String())


var source = `
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-us" lang="en-us">
    <head>
        <title>Syntax Highlighting from Markdown with Chroma</title>
        {{.Style}}
    </head>
    <body>
        {{.Content}}
    </body>
</html>`;


// // // write css
// // hlbuf := bytes.Buffer{}
// // hlw := bufio.NewWriter(&hlbuf)
// // formatter := html.New(html.WithClasses())
// // if err := formatter.WriteCSS(hlw, styles.MonokaiLight); err != nil {
// //     log.Fatal(err)
// // }
// // hlw.Flush()

// // replace code-parts with syntax-highlighted parts
// replaced, err := replaceCodeParts(htmlSrc)
// if err != nil {
//     log.Fatal(err)
// }
// // write html output
// if err := t.Execute(os.Stdout, struct {
//     Content template.HTML
//     CSS   template.CSS
// }{
//     Content: template.HTML(replaced),
//     Style:   template.CSS("<style>" + hlbuf.String() + "</style>"),
// }); err != nil {
//     log.Fatal(err)
// }


// style := styles.Get("swapoff")
// if style == nil {
//   style = styles.Fallback
// }
// formatter := formatters.Get("html")
// if formatter == nil {
//   formatter = formatters.Fallback
// }

// lexer := lexers.Get("python")

// // contents, err := ioutil.ReadAll(r)
// var contents  = `
// import python
// import blah
// def afunc():
//     pass
// `
// iterator,err := lexer.Tokenise(nil, string(contents))
// err = formatter.Format( &buf,  style, iterator)
// fmt.Fprintf(os.Stdout, "%s \n", buf.String())

// _ = err;
_ = buf;
_ = source;
_ = md;
// _ = err;

// readed,err := io.Reader("input.md")
readed, err := ioutil.ReadFile("./input.md")
if err!=nil{panic(err);}
// out := bytes.Buffer{}

out := blackfriday.MarkdownCommon(readed)
// err = md.Convert(readed,&out).Bytes();
// if err!=nil{panic(err)}

outt,err:=replaceCodeParts(out);
// fmt.Printf("%s \n",outt);
_ = fmt.Printf;
_ = err;

t, err := template.ParseFiles("./template.html")
if err != nil {
	log.Fatal(err)
}

// write css
hlbuf := bytes.Buffer{}
hlw := bufio.NewWriter(&hlbuf)
formatter := html.New(html.WithClasses(true))
if err := formatter.WriteCSS(hlw, styles.MonokaiLight); err != nil {
	log.Fatal(err)
}


err = t.Execute(os.Stdout, struct {
	Content template.HTML
	Style   template.CSS
}{
	// Content: template.HTML("something"),
	// Style:   template.CSS("else"),
	Content: template.HTML(outt),
	Style:   template.CSS(hlbuf.String()),
}); 

_ = os.Stdout;
_ = t;

if err != nil {
	log.Fatal(err)
}

// // write css
// hlbuf := bytes.Buffer{}
// hlw := bufio.NewWriter(&hlbuf)
// formatter := html.New(html.WithClasses())
// if err := formatter.WriteCSS(hlw, styles.MonokaiLight); err != nil {
// 	log.Fatal(err)
// }
// hlw.Flush()
// // write html output
// if err := t.Execute(os.Stdout, struct {
// 	Content template.HTML
// 	Style   template.CSS
// }{
// 	Content: template.HTML(replaced),
// 	Style:   template.CSS(hlbuf.String()),
// }); err != nil {
// 	log.Fatal(err)
// }

}


func replaceCodeParts(mdFile []byte) (string, error) {
	byteReader := bytes.NewReader(mdFile)
	doc, err := goquery.NewDocumentFromReader(byteReader)
	if err != nil {
		return "", err
	}
	// find code-parts via selector and replace them with highlighted versions
	var hlErr error
	doc.Find("code[class*=\"language-\"]").Each(func(i int, s *goquery.Selection) {
		if hlErr != nil {
			return
		}
		class, _ := s.Attr("class")
		lang := strings.TrimPrefix(class, "language-")
		oldCode := s.Text()
		lexer := lexers.Get(lang)
		formatter := html.New(html.WithClasses(true))
		iterator, err := lexer.Tokenise(nil, string(oldCode))
		if err != nil {
			hlErr = err
			return
		}
		b := bytes.Buffer{}
		buf := bufio.NewWriter(&b)
		if err := formatter.Format(buf, styles.GitHub, iterator); err != nil {
			hlErr = err
			return
		}
		if err := buf.Flush(); err != nil {
			hlErr = err
			return
		}
		s.SetHtml(b.String())
	})
	if hlErr != nil {
		return "", hlErr
	}
	new, err := doc.Html()
	if err != nil {
		return "", err
	}
	// replace unnecessarily added html tags
	return new, nil
}