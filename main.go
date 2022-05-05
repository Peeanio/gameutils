// Gameutils API server

// Max Russell

package main

import (
		"fmt"
		//"encoding/json"
		"net/http"
		//"io"
		"log"
		"github.com/gin-gonic/gin"
		"strconv"
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


func main() {
	Operations[1] = Operation{ID: "1", Title: "SECOND CANCEL", Agent: Agent{CodeName: "Burn", RealName: "Jada Wiseman"}, Status: "Register"}
	Operations[2] = Operation{ID: "2", Title: "TAUT BIRTHDAY", Agent: Agent{CodeName: "Convert", RealName: "Jaroslav Maanan"}, Status: "Choclate"}
	
	fmt.Println(Operations)
	fmt.Println("HTTP API - Espionage v2")
	router := gin.Default()
	
	router.GET("/hello", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "World",
		})
	})
	
	router.GET("/operations/:id", func(c *gin.Context) {
		fmt.Println("Endpoint hit: returnOperation")
		calledId := c.Params.ByName("id")
		idInt, err := strconv.Atoi(calledId)
		if err != nil {
			fmt.Println(err)
		}
		for _, operation := range Operations {
			if operation.ID == calledId {
				c.JSON(http.StatusOK, gin.H{
				"Operation": Operations[idInt],
				})
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
		//updates an operation
		fmt.Println("Endpoint hit: delete an Operation")
		calledId := c.Params.ByName("id")
		idInt, err := strconv.Atoi(calledId)
		if err != nil {
			fmt.Println(err)
		}
		Operations[idInt] = Operation{}

		c.JSON(http.StatusOK, gin.H{"Operation": Operations[idInt]})
	})
	
	log.Fatal(router.Run(":9000"))
}
