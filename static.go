package main;
import (
  "log"
  "net/http"
)

func main() {
  fs := http.FileServer(http.Dir("./public"))
  http.Handle("/blog/", http.StripPrefix("/blog/", fs))

  log.Println("Listening on :3001...")
  err := http.ListenAndServe(":3001", nil)
  if err != nil {
    log.Fatal(err)
  }
}
