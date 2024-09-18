# Use the Alpine image with OpenJDK 17
FROM openjdk:17-alpine

# Install Maven via apk (Alpine Linux)
RUN apk add --no-cache maven

# Create the working directory in the container
WORKDIR /app

# # Copy only the pom.xml and download the dependencies
# COPY ./project/pom.xml /app/

# # Download the dependencies to make the build faster if only the code changes
# RUN mvn dependency:go-offline

# # Copy the rest of the source code into the working directory
# COPY ./project/src /app/src

# # Build the project and generate the JAR file
# RUN mvn package

COPY ./project/target/kotlinServer.jar /app/target/kotlinServer.jar

EXPOSE 8080

CMD ["java", "-jar", "target/kotlinServer.jar"]
#CMD ["tail", "-f", "/dev/null"]

# run with: 
# docker build -t kotlinserver .
# docker run --name KotlinServer -p 8080:8080 -it kotlinserver
