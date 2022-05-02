// Gameutils API server

// Max Russell

package main

import (
		"fmt"
		"encoding/json"
		"net/http"
		"io"
		"log"
)

type Operation struct {
	ID string `json:"ID"`
	Title string `json:"Title"`
	Agent string `json:"Agent"`
	Status string `json:"Status"`
}

var Operations []Operation

func hello(res http.ResponseWriter, req *http.Request) {
	res.Header().Set(
		"Content-Type",
		"text/html",
	)
	io.WriteString(
		res,
		`<DOCTYPE html>
		<html>
			<head>
				<title>Hello, World</title>
			</head>
			<body>
				Hello, World!
			</body>
		</html>`,
	)
	fmt.Println("Endpoint hit: hello")
}

func handleRequests() {
	mux := http.NewServeMux()
	mux.HandleFunc("/hello", hello)
	mux.HandleFunc("/operations", returnAllOperations)
//	mux.HandleFunc("/operation/{id}", returnSingleOperation)
	//log.Fatal(http.ListenAndServe(":9000", nil))
	s := &http.Server{
		Addr: ":9000",
		Handler: mux,
	}
	log.Fatal(s.ListenAndServe())
}

func returnAllOperations(w http.ResponseWriter, r *http.Request){
	fmt.Println("Endpoint hit: returnAllOperations")
	json.NewEncoder(w).Encode(Operations)
}

//func createNewOperation(w http.ResponseWriter, r *http.Request) {
//	reqBody, _ := ioutil.ReadAll(r.body)
//	fmt.Fprintf(w, "%+v", string(reqBody))
//}

func main() {
	fmt.Println("HTTP API - Espionage v1")
	Operations = []Operation{
		Operation{ID: "1", Title: "SECOND CANCEL", Agent: "Jada Wiseman", Status: "Register"},
		Operation{ID: "2", Title: "TAUT BIRTHDAY", Agent: "Jaroslav Maanan", Status: "Choclate"},
	}
	handleRequests()
}
