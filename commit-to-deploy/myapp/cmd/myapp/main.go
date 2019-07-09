package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	hostname, ok := os.LookupEnv("HOSTNAME")
	if !ok {
		hostname = "no hostname"
	}

	secretByte, err := ioutil.ReadFile("/secrets/secret.txt")
        secret := string(secretByte)
	switch {
	case os.IsNotExist(err):
		secret = "no secret found"
	case os.IsPermission(err):
		secret = "unable to access secret"
	case err != nil:
		secret = fmt.Sprintf("unable to load secret: %s", err)
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "# myapp\n\n")
		fmt.Fprint(w, "an incredible application.\n\n")
		fmt.Fprintf(w, "hostname: %s\n", hostname)
		fmt.Fprintf(w, "secret:   %s\n", secret)
	})
	http.ListenAndServe(":8080", nil)

}
