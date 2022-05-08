// Gameutils API server

// Max Russell

package main

import (
		"bytes"
		"fmt"
		"encoding/json"
		"os/exec"
		"net/http"
		//"io"
		"log"
		"github.com/gin-gonic/gin"
		"strconv"
		"strings"
)

type Operation struct {
	ID string `json:"ID"`
	Title string `json:"Title"`
	Agent Agent `json:"Agent"`
	Status string `json:"Status"`
}

type Agent struct {
	CodeName string `json:"CodeName"`
	RealName string `json:"RealName"`
}
	

var Operations [3]Operation

func returnOpString(zero string, one string, two string, three string, four string, five string, six string, seven string) string {
	//returns a string from the codename string with eight positions in the commdn
	cmd:= exec.Command(one, two, three, four, five, six, seven)
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	if err != nil {
		fmt.Println(err)
	}
	result:= strings.TrimSuffix(out.String(), "\n")
	return result
}

func createOperation(id string) Operation {
	//input a command, return a string
	 title := returnOpString("python3", "./codename.py", "-q", "-u", "-o", "", "", "")
	 codeName := returnOpString("python3", "./codename.py", "-q", "-c", "-u", "", "", "")
	 realName := returnOpString("python3", "./codename.py", "-q", "-a", "firstnames.txt", "-n", "surnames.txt", "-o")
	 status := returnOpString("python3", "./codename.py", "-q", "-u", "-c", "", "", "")
	 op := Operation{ID: id, Title: title, Agent: Agent{CodeName: codeName, RealName: realName}, Status: status}
	 return op
	 
}

func operationRouters(router *gin.Engine) {
	//all /operation endpoints
	router.GET("/operations/:id", func(c *gin.Context) {
		fmt.Println("Endpoint hit: returnOperation")
		calledId := c.Params.ByName("id")
		idInt, err := strconv.Atoi(calledId)
		if err != nil {
			fmt.Println(err)
		}
		for _, operation := range Operations {
			if operation.ID == calledId {
				//c.JSON(http.StatusOK, gin.H{
				//"Operation": Operations[idInt],
				//})
				op, err := json.Marshal(Operations[idInt])
				if err != nil {
					fmt.Println(err)
				}
				c.String(http.StatusOK, string(op)) 
			} 
		}
	})
	
	router.GET("/operations/all", func(c *gin.Context) {
		fmt.Println("Endpoint hit: returnAllOperation")
		c.JSON(http.StatusOK, gin.H{
			"Operations": Operations}) 
	})
	
	router.POST("/operations/:id", func(c *gin.Context) {
		//creates an operation
		fmt.Println("Endpoint hit: create an Operation")
		var json Operation
		calledId := c.Params.ByName("id")
		idInt, err := strconv.Atoi(calledId)
		if err != nil {
			fmt.Println(err)
		}
		if Operations[idInt].ID != "" {
			c.JSON(http.StatusBadRequest, gin.H{"error": "operation exists!"})
			return
		}
		if err := c.ShouldBindJSON(&json); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		Operations[idInt] = Operation{ID: json.ID, Title: json.Title, Agent: Agent{CodeName: json.Agent.CodeName, RealName: json.Agent.RealName}, Status: json.Status}

		c.JSON(http.StatusOK, gin.H{"Operation": Operations[idInt]})
	})
	
	router.PUT("/operations/:id", func(c *gin.Context) {
		//updates an operation
		fmt.Println("Endpoint hit: update an Operation")
		var json Operation
		calledId := c.Params.ByName("id")
		idInt, err := strconv.Atoi(calledId)
		if err != nil {
			fmt.Println(err)
		}
		if err := c.ShouldBindJSON(&json); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		Operations[idInt] = Operation{ID: json.ID, Title: json.Title, Agent: Agent{CodeName: json.Agent.CodeName, RealName: json.Agent.RealName}, Status: json.Status}

		c.JSON(http.StatusOK, gin.H{"Operation": Operations[idInt]})
	})
	
	router.DELETE("/operations/:id", func(c *gin.Context) {
		//REDACTS an operation, all elements changed
		fmt.Println("Endpoint hit: delete an Operation")
		calledId := c.Params.ByName("id")
		idInt, err := strconv.Atoi(calledId)
		if err != nil {
			fmt.Println(err)
		}
		Operations[idInt] = Operation{ID: "REDACTED", Title: "REDACTED", Agent: Agent{CodeName: "REDACTED", RealName: "REDACTED"}, Status: "REDACTED"}

		c.JSON(http.StatusOK, gin.H{c.Params.ByName("id"): "deleted"})
	})

}

func main() {
	Operations[0] = createOperation("0")
	Operations[1] = createOperation("1")
	Operations[2] = createOperation("2")
	
	//debug to see the operations
	//op, err := json.Marshal(Operations[1])
	//if err != nil {
		//fmt.Println(err)
	//}
	//fmt.Println(string(op))
	//fmt.Println(Operations)
	fmt.Println("HTTP API - Espionage v2")
	router := gin.Default()
	
	router.GET("/hello", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "World",
		})
	})
	
	operationRouters(router)
	
	log.Fatal(router.Run(":9000"))
}
