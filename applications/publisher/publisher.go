package main

import (
	"fmt"
	"net/http"
	"github.com/julienschmidt/httprouter"
	log "github.com/sirupsen/logrus"
	"github.com/streadway/amqp"
	"os"
)

var rabbit_host = os.Getenv("RABBIT_HOST")
var rabbit_port = os.Getenv("RABBIT_PORT")
var rabbit_user = os.Getenv("RABBIT_USERNAME")
var rabbit_pasword = os.Getenv("RABBIT_PASSWORD")

func main(){
	router:= httprouter.New()

	router.POST("/publish/:message", func(w http.ResponseWriter, r *http.Request, p httprouter.Params){

		submit(w,r,p)

		fmt.Println("Running...")
		log.Fatal(http.ListenAndServe(":80", router))
	})
}