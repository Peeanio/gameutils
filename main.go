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
			//else {
			//	c.JSON(http.StatusOK, gin.H{
			//		"ID": "Not found!",
			//	})
			//}
		}
	})
	
	
	log.Fatal(router.Run(":9000"))
}
