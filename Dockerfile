FROM public.ecr.aws/bitnami/golang:1.12 AS build
#Install git
RUN apk add --no-cache git
#Get the hello world package from a GitHub repository
RUN go get github.com/aimanh22/Cloud-Continuous-Delivery-of-Microservice-Project
WORKDIR /go/src/github.com/aimanh22/Cloud-Continuous-Delivery-of-Microservice-Project
# Build the project and send the output to /bin/App
RUN go build -o /bin/App

FROM public.ecr.aws/bitnami/golang:1.12
#Copy the build's output binary from the previous build container
COPY --from=build /bin/App /bin/App
ENTRYPOINT ["/bin/App"]
